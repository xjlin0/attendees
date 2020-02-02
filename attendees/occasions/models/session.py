from django.db import models
from django.urls import reverse
from django.contrib.contenttypes.fields import GenericRelation, GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from model_utils.models import TimeStampedModel, SoftDeletableModel, TimeFramedModel

from attendees.persons.models import Utility, Note


class Session(TimeStampedModel, SoftDeletableModel, TimeFramedModel, Utility):
    notes = GenericRelation(Note)
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    gathering = models.ForeignKey('Gathering', on_delete=models.SET(0), null=False, blank=False)
    attendings = models.ManyToManyField('persons.Attending', through='Participation')
    display_name = models.CharField(max_length=50, blank=True, help_text="The Rock, Little Foot, singspiration, etc")
    link = models.CharField(max_length=254, blank=True)
    site_type = models.ForeignKey(ContentType, on_delete=models.SET(0), help_text='location: django_content_type id for table name')
    site_id = models.BigIntegerField()
    location = GenericForeignKey('site_type', 'site_id')

    # from itertools import groupby
    # from operator import attrgetter
    #
    # ordered_program_sessions = ProgramSession.objects.order_by('program_group', 'start_at')
    # program_sessions_grouped_by_program_groups = {
    #     k: list(v)
    #     for k, v in groupby(ordered_program_sessions, attrgetter('program_group'))
    # } #=> {<ProgramGroup: The Rock  >: [<ProgramSession: The Rock #1...>, <ProgramSession: The Rock #2...>]}

    def get_absolute_url(self):
        return reverse('session_detail', args=[str(self.id)])

    class Meta:
        db_table = 'occasions_sessions'
        ordering = ['gathering', 'start']
        constraints = [
            models.UniqueConstraint(fields=['gathering_id', 'site_type_id', 'site_id', 'start'], name='uniq_gathering_location_time')
        ]

    def __str__(self):
        return '%s %s %s %s' % (self.gathering, self.start, self.display_name or '', self.location or '')
