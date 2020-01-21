from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from model_utils.models import TimeStampedModel, SoftDeletableModel

from attendees.persons.models import Utility, Note


class Team(TimeStampedModel, SoftDeletableModel, Utility):
    notes = GenericRelation(Note)
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    group = models.ForeignKey('Group', null=False, blank=False, on_delete=models.SET(0))
    key = models.CharField(max_length=50, blank=False, null=False, unique=True)
    display_name = models.CharField(max_length=50, blank=True, null=True)
    display_order = models.IntegerField(default=0, blank=True, null=True)

    class Meta:
        db_table = 'occasions_teams'

    def __str__(self):
        return '%s %s' % (self.group, self.display_name or '')

