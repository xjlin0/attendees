from django.db import models
from django.urls import reverse
from django.contrib.contenttypes.fields import GenericRelation
from model_utils.models import TimeStampedModel, SoftDeletableModel

from attendees.persons.models import Utility, Note
from attendees.occasions.models import Session


class Campus(TimeStampedModel, SoftDeletableModel, Utility):
    notes = GenericRelation(Note)
    session = GenericRelation(Session)
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    display_name = models.CharField(max_length=50, blank=False, null=False, db_index=True)
    key = models.CharField(max_length=50, blank=False, null=False, unique=True)
    address = models.ForeignKey('Address', null=True, on_delete=models.SET_NULL)

    class Meta:
        db_table = 'whereabouts_campus'
        verbose_name_plural = 'Campuses'

    def get_absolute_url(self):
        return reverse('campus_detail', args=[str(self.id)])

    def __str__(self):
        return '%s' % self.display_name
