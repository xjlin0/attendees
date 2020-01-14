from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.contenttypes.fields import GenericRelation

from model_utils.models import TimeStampedModel, SoftDeletableModel

from . import GenderEnum, Note, Utility


class Attendee(Utility, TimeStampedModel, SoftDeletableModel):
    notes = GenericRelation(Note)
    relations = models.ManyToManyField('self', through='Relationship', symmetrical=True, related_name='related_to+')
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    first_name = models.CharField(max_length=25, db_index=True, null=True, blank=True)
    last_name = models.CharField(max_length=25, db_index=True, null=True, blank=True)
    first_name2 = models.CharField(max_length=12, db_index=True, null=True, blank=True)
    last_name2 = models.CharField(max_length=8, db_index=True, null=True, blank=True)
    other_name = models.CharField(max_length=20, db_index=True, null=True, blank=True)
    gender = models.CharField(max_length=11, blank=False, null=False, default=GenderEnum.UNSPECIFIED, choices=GenderEnum.choices())
    actual_birthday = models.DateTimeField(blank=True, null=True)
    estimated_birthday = models.DateTimeField(blank=True, null=True)
    medical_concern = models.CharField(max_length=50, null=False, blank=False, default="Food allergy: nothing")

    def __str__(self):
        return '%s %s %s %s' % (self.first_name or '', self.last_name or '', self.last_name2 or '', self.first_name2 or '')

    def clean(self):
        if not (self.last_name or self.last_name2):
            raise ValidationError("You must specify a last_name")

    class Meta:
        db_table = 'persons_attendees'
        ordering = ['last_name', 'first_name']