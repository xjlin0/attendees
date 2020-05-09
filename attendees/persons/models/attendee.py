from django.db import models

from django.core.exceptions import ValidationError
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.postgres.fields.jsonb import JSONField
from django.contrib.postgres.indexes import GinIndex
from django.utils.functional import cached_property
from datetime import datetime, timezone
from model_utils.models import TimeStampedModel, SoftDeletableModel

from . import GenderEnum, Note, Utility


class Attendee(Utility, TimeStampedModel, SoftDeletableModel):
    # RELATIVES_KEYWORDS = ['parent', 'mother', 'guardian', 'father', 'caregiver']
    # AS_PARENT_KEYWORDS = ['notifier', 'caregiver']  # to find attendee's parents/caregiver in cowokers view of all activities
    # BE_LISTED_KEYWORDS = ['care receiver']  # let the attendee's attendance showed in their parent/caregiver account

    notes = GenericRelation(Note)
    related_ones = models.ManyToManyField('self', through='Relationship', symmetrical=False, related_name='related_to+')
    addresses = models.ManyToManyField('whereabouts.Address', through='AttendeeAddress', related_name='addresses')
    user = models.OneToOneField('users.User', default=None, null=True, blank=True, on_delete=models.SET_NULL)
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    families = models.ManyToManyField('persons.Family', through='FamilyAttendee', related_name='families')
    first_name = models.CharField(max_length=25, db_index=True, null=True, blank=True)
    last_name = models.CharField(max_length=25, db_index=True, null=True, blank=True)
    first_name2 = models.CharField(max_length=12, db_index=True, null=True, blank=True)
    last_name2 = models.CharField(max_length=8, db_index=True, null=True, blank=True)
    gender = models.CharField(max_length=11, blank=False, null=False, default=GenderEnum.UNSPECIFIED, choices=GenderEnum.choices())
    actual_birthday = models.DateTimeField(blank=True, null=True)
    estimated_birthday = models.DateTimeField(blank=True, null=True)
    progressions = JSONField(null=True, blank=True, default=dict, help_text='Example: {"Christian": true, "baptized": {"time": "12/31/2020", "place":"SF"}}. Please keep {} here even no data')
    # photo = PrivateFileField("File") #https://github.com/edoburu/django-private-storage
    infos = JSONField(null=True, blank=True, default=dict, help_text='Example: {"food allergy": "peanuts", "public_name": "John", "other_name": "Apostle"}. Please keep {} here even no data')

    @property
    def display_label(self):
        return (self.first_name or '') + ' ' + (self.last_name or '') + (self.last_name2 or '') + ' ' + (self.first_name2 or '')

    @cached_property
    def family_members(self):
        return self.__class__.objects.filter(families__in=self.families.all())

    @cached_property
    def self_phone_numbers(self):
        return self.self_addresses_for_fields_of(['phone1', 'phone2'])

    @cached_property
    def self_email_addresses(self):
        return self.self_addresses_for_fields_of(['email1', 'email2'])

    def self_addresses_for_fields_of(self, fields):
        items = sum(self.addresses.values_list(*fields), ())
        return ', '.join(
            item for item in items if item
        )

    @cached_property
    def caregiver_email_addresses(self):
        return self.caregiver_addresses_for_fields_of(['email1', 'email2'])

    @cached_property
    def caregiver_phone_numbers(self):
        return self.caregiver_addresses_for_fields_of(['phone1', 'phone2'])

    def caregiver_addresses_for_fields_of(self, fields):
        return ', '.join(
            a.self_addresses_for_fields_of(fields) for a in
                self.get_relative_emergency_contacts()
        )

    def get_relative_emergency_contacts(self):
        return self.related_ones.filter(
                    to_attendee__relation__relative=True,
                    to_attendee__relation__emergency_contact=True,
                    to_attendee__finish__gte=datetime.now(timezone.utc),
                )

    @cached_property
    def parents_notifiers_names(self):
        """
        :return: attendees' names of their parents/caregiviers
        """
        return ', '.join(list(
                            self.get_relative_emergency_contacts().annotate(
                                full_name=models.functions.Concat(
                                    'first_name',
                                    models.Value(' '),
                                    'first_name2',
                                    models.Value(' '),
                                    'last_name',
                                    models.Value(' '),
                                    'last_name2',
                                ),
                            ).order_by(
                                '-to_attendee__relation__display_order',
                            ).values_list(
                                'full_name',
                                flat=True
                            )
                        )
                    )

    def __str__(self):
        return self.display_label

    # def all_relations(self): #cannot import Relationship, probably needs native query
    #     return dict(((r.from_attendee, r.relation) if r.to_attendee == self else (r.to_attendee, r.relation) for r in Relationship.objects.filter(Q(from_attendee=self.id) | Q(to_attendee=self.id))))
    # switching to symmetrical False with Facebook model (but add relationship both ways and need add/remove_relationship methods) http://charlesleifer.com/blog/self-referencing-many-many-through/
    # also attendee.related_ones will return deleted relationship, so extra filter is required (.filter(relationship__is_removed = False))

    def clean(self):
        if not (self.last_name or self.last_name2):
            raise ValidationError("You must specify a last_name")

    class Meta:
        db_table = 'persons_attendees'
        ordering = ['last_name', 'first_name']
        indexes = [
            GinIndex(fields=['infos'], name='attendee_infos_gin', ),
            GinIndex(fields=['progressions'], name='attendee_progressions_gin', ),
        ]
