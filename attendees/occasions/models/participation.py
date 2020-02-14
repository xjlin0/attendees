from django.db import models
from django.urls import reverse
from django.utils.functional import cached_property
from django.contrib.contenttypes.fields import GenericRelation
from model_utils.models import TimeStampedModel, SoftDeletableModel

from attendees.persons.models import Utility, Note


class Participation(TimeStampedModel, SoftDeletableModel, Utility):
    notes = GenericRelation(Note)
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    start = models.DateTimeField(null=True, blank=True, help_text='optional')
    finish = models.DateTimeField(null=True, blank=True, help_text='optional')
    gathering = models.ForeignKey('Gathering', null=False, blank=False, on_delete=models.SET(0))
    team = models.ForeignKey('Team', default=None, null=True, blank=True, on_delete=models.SET_NULL, help_text="empty for main meet")
    attending = models.ForeignKey('persons.Attending', null=False, blank=False, on_delete=models.SET(0))
    character = models.ForeignKey('Character', null=False, blank=False, on_delete=models.SET(0))
    free = models.IntegerField(default=0, blank=True, null=True, help_text="multitasking: the person cannot join other gatherings if negative")
    category = models.CharField(max_length=20, null=False, blank=False, db_index=True, default="normal", help_text="normal, leave, remote, etc")

    @cached_property
    def participation_info(self):
        gathering = self.gathering
        return gathering.meet.display_name + gathering.start.strftime(" @ %b.%d'%y")

    def get_absolute_url(self):
        return reverse('participation_detail', args=[str(self.id)])

    class Meta:
        db_table = 'occasions_participations'

    def __str__(self):
        return '%s %s %s' % (self.gathering, self.character, self.team or '')

