from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from attendees.persons.models import Utility, Note
from model_utils.models import TimeStampedModel, SoftDeletableModel

from . import Organization


class Division(TimeStampedModel, SoftDeletableModel, Utility):
    link_notes = GenericRelation(Note)
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    organization = models.ForeignKey(Organization, null=False, blank=False, on_delete=models.SET(0))
    display_name = models.CharField(max_length=50, blank=False, null=False)
    slug = models.SlugField(max_length=50, blank=False, null=False, unique=True)
    attendings = models.ManyToManyField('persons.Attending', through='persons.AttendingDivision')

    class Meta:
        db_table = 'whereabouts_divisions'

    def __str__(self):
        return '%s' % self.display_name

