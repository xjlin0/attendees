from django.db import models
from model_utils.models import TimeStampedModel, SoftDeletableModel
from . import Utility


class AttendingMeet(TimeStampedModel, SoftDeletableModel, Utility):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    attending = models.ForeignKey('Attending', on_delete=models.SET(0), null=False, blank=False)
    meet = models.ForeignKey('occasions.Meet', on_delete=models.SET(0), null=False, blank=False)
    character = models.ForeignKey('occasions.Character', null=False, blank=False, on_delete=models.SET(0))
    category = models.CharField(max_length=20, default='primary', blank=False, null=False, help_text='primary, secondary, etc (primary will be displayed first)')

    class Meta:
        db_table = 'persons_attending_meets'
        constraints = [
            models.UniqueConstraint(fields=['attending', 'meet'], name="attending_meet")
        ]

    def __str__(self):
        return '%s %s' % (self.attending, self.meet)
