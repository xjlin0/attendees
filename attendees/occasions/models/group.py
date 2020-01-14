from django.db import models
from django.urls import reverse
from django.contrib.contenttypes.fields import GenericRelation
from model_utils.models import TimeStampedModel, SoftDeletableModel

from attendees.persons.models import Utility, Note


class Group(TimeStampedModel, SoftDeletableModel, Utility):
    notes = GenericRelation(Note)
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    division = models.ForeignKey('whereabouts.Division', null=True, blank=True, on_delete=models.SET_NULL)
    display_name = models.CharField(max_length=50, blank=True, null=False, db_index=True, help_text="The Rock, Little Foot, singspiration, A/V control, etc.")
    key = models.CharField(max_length=50, blank=False, null=False, unique=True)
    info = models.CharField(max_length=255, blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=False)

    def get_absolute_url(self):
        return reverse('character_detail', args=[str(self.id)])

    class Meta:
        db_table = 'occasions_groups'

    def __str__(self):
        return '%s %s %s' % (self.display_name, self.info or '', self.url)
