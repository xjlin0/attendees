from django.db import models
from django.urls import reverse
from django.contrib.contenttypes.fields import GenericRelation

from model_utils.models import TimeStampedModel, SoftDeletableModel, TimeFramedModel

from attendees.persons.models import Utility, Note
# from attendees.whereabouts.models import Division


class Event(TimeStampedModel, SoftDeletableModel, TimeFramedModel, Utility):
    notes = GenericRelation(Note)
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    addresses = models.ManyToManyField('whereabouts.Address', through='EventAddress')
    display_name = models.CharField(max_length=50, blank=False, null=False)
    key = models.CharField(max_length=50, blank=False, null=False, unique=True)
    division = models.ForeignKey('whereabouts.Division', null=False, blank=False, on_delete=models.SET(0))

    def get_absolute_url(self):
        return reverse('event_detail', args=[str(self.id)])

    class Meta:
        db_table = 'occasions_events'
        ordering = ('-start',)

    def __str__(self):
        return '%s' % self.display_name

    # def get_addresses(self):
    #     return "\n".join([a.street1 + a.city for a in self.addresses.all()])


# from rest_framework import serializers
#
#
# class EventSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Event
#         fields = ['id', 'name', 'division', 'ttttt']

# from mainsite.models.event import EventSerializer
# k2=Event.objects.get(pk=2)
# serializer=EventSerializer(k2)
# serializer.data
# #=> {'id': 2, 'name': '2019 Fall kid programs', 'division': 'none', 'ttttt': 'ttttt'}
