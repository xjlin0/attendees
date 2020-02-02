from django.db import models
from model_utils.models import TimeStampedModel, SoftDeletableModel
from . import Utility


class AttendeeAddress(TimeStampedModel, SoftDeletableModel, Utility):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    attendee = models.ForeignKey('Attendee', on_delete=models.SET(0), null=False, blank=False)
    address = models.ForeignKey('whereabouts.Address', on_delete=models.SET(0), null=False, blank=False)

    class Meta:
        db_table = 'persons_attendee_addresses'
        constraints = [
            models.UniqueConstraint(fields=['attendee', 'address'], name="attendee_address")
        ]

    def __str__(self):
        return '%s %s' % (self.attendee, self.address)