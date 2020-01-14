from django.db import models
from django.contrib.contenttypes.fields import GenericRelation

from model_utils.models import TimeStampedModel, SoftDeletableModel

from attendees.persons.models import Utility, Note
# from attendees.whereabouts.models import Address

from . import Event


class EventAddress(TimeStampedModel, SoftDeletableModel, Utility):
    notes = GenericRelation(Note)
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    event = models.ForeignKey(Event, on_delete=models.SET(0), null=False, blank=False)
    address = models.ForeignKey('whereabouts.Address', on_delete=models.SET(0), null=False, blank=False)
    category = models.CharField(max_length=20, null=True, help_text="primary, backup, etc")


    class Meta:
        db_table = 'occasions_event_addresses'
        constraints = [
            models.UniqueConstraint(fields=['event', 'address'], name="event_address")
        ]

    def __str__(self):
        return '%s %s' % (self.event, self.address or '')
