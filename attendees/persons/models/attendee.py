from django.db import models

from django.core.exceptions import ValidationError
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.postgres.fields.jsonb import JSONField
from django.utils.functional import cached_property
from django.db.models import Q, Value as V
from django.db.models.functions import Concat

from model_utils.models import TimeStampedModel, SoftDeletableModel

from . import GenderEnum, Note, Utility


class Attendee(Utility, TimeStampedModel, SoftDeletableModel):
    notes = GenericRelation(Note)
    relations = models.ManyToManyField('self', through='Relationship', symmetrical=False, related_name='related_to+')
    addresses = models.ManyToManyField('whereabouts.Address', through='AttendeeAddress', related_name='addresses')
    user = models.OneToOneField('users.User', default=None, null=True, blank=True, on_delete=models.SET_NULL)
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    first_name = models.CharField(max_length=25, db_index=True, null=True, blank=True)
    last_name = models.CharField(max_length=25, db_index=True, null=True, blank=True)
    first_name2 = models.CharField(max_length=12, db_index=True, null=True, blank=True)
    last_name2 = models.CharField(max_length=8, db_index=True, null=True, blank=True)
    other_name = models.CharField(max_length=20, db_index=True, null=True, blank=True)
    public_name = models.CharField(max_length=20, null=True, blank=True, help_text='for unlogged in pages so please use safe terms, suggestion: first born, youngest, mom, etc')
    gender = models.CharField(max_length=11, blank=False, null=False, default=GenderEnum.UNSPECIFIED, choices=GenderEnum.choices())
    actual_birthday = models.DateTimeField(blank=True, null=True)
    estimated_birthday = models.DateTimeField(blank=True, null=True)
    infos = JSONField(null=True, blank=True, default=dict, help_text='Example: {"food allergy": "peanuts"}. Please keep {} here even no data')

    @property
    def display_label(self):
        return (self.first_name or '') + ' ' + (self.last_name or '') + (self.last_name2 or '') + ' ' + (self.first_name2 or '')

    @cached_property
    def all_email_addresses(self):
        emails = sum(self.addresses.values_list('email1', 'email2'), ())
        return ', '.join(email for email in emails if email)

    @cached_property
    def parents_kids_names(self):
        relation_keywords = ['parent', 'guardian']
        return ', '.join(list(
                            self.relations.filter(
                                Q(to_attendee__relation__in=relation_keywords)
                                |
                                Q(from_attendee__relation__in=relation_keywords)
                            ).annotate(
                                full_name=Concat(
                                    'first_name',
                                    V(' '),
                                    'first_name2',
                                    V(' '),
                                    'last_name',
                                    V(' '),
                                    'last_name2',
                                ),
                            ).values_list(
                                'full_name',
                                flat=True
                            )
                        )
                    )

    def get_relatives(self, relation_keywords):
        return self.relations.filter(
                    Q(to_attendee__relation__in=relation_keywords)
                    |
                    Q(from_attendee__relation__in=relation_keywords)
                )

    def __str__(self):
        return self.display_label

    # def all_relations(self): #cannot import Relationship, probably needs native query
    #     return dict(((r.from_attendee, r.relation) if r.to_attendee == self else (r.to_attendee, r.relation) for r in Relationship.objects.filter(Q(from_attendee=self.id) | Q(to_attendee=self.id))))
    # switching to symmetrical False with Facebook model (but add relationship both ways and need add/remove_relationship methods) http://charlesleifer.com/blog/self-referencing-many-many-through/
    # also attendee.relations will return deleted relationship, so extra filter is required (.filter(relationship__is_removed = False))

    def clean(self):
        if not (self.last_name or self.last_name2):
            raise ValidationError("You must specify a last_name")

    class Meta:
        db_table = 'persons_attendees'
        ordering = ['last_name', 'first_name']
