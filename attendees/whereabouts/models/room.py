from django.db import models
from django.urls import reverse
from django.contrib.contenttypes.fields import GenericRelation
from model_utils.models import TimeStampedModel, SoftDeletableModel

from attendees.persons.models import Utility, Note


class Room(TimeStampedModel, SoftDeletableModel, Utility):
    notes = GenericRelation(Note)
    # program_session = GenericRelation('ProgramSession')
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    display_name = models.CharField(max_length=50, blank=False, null=False, db_index=True)
    suite = models.ForeignKey('Suite', null=True, on_delete=models.SET_NULL)
    label = models.CharField(max_length=20, blank=True)
    accessibility = models.IntegerField(default=0, blank=False, null=False)

    class Meta:
        db_table = 'whereabouts_rooms'

    def get_absolute_url(self):
        return reverse('room_detail', args=[str(self.id)])

    def __str__(self):
        return '%s %s %s' % (self.suite.display_name, self.display_name, self.label or '')
