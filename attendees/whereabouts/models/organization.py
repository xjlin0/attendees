from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from attendees.persons.models import Utility, Note
from model_utils.models import TimeStampedModel, SoftDeletableModel


class Organization(TimeStampedModel, SoftDeletableModel, Utility):
    notes = GenericRelation(Note)
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    key = models.CharField(max_length=50, blank=False, null=False, unique=True, help_text="alphanumeric only")
    display_name = models.CharField(max_length=50, blank=False, null=False)


    class Meta:
        db_table = 'whereabouts_organizations'

    def __str__(self):
        return '%s' % self.display_name

