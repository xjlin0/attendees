from django.db import models
from model_utils.models import TimeStampedModel, SoftDeletableModel
from . import Utility


class AttendingDivision(TimeStampedModel, SoftDeletableModel, Utility):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    attending = models.ForeignKey('Attending', on_delete=models.SET(0), null=False, blank=False)
    division = models.ForeignKey('whereabouts.Division', on_delete=models.SET(0), null=False, blank=False)

    class Meta:
        db_table = 'persons_attending_divisions'
        constraints = [
            models.UniqueConstraint(fields=['attending', 'division'], name="attending_division")
        ]

    def __str__(self):
        return '%s %s' % (self.attending, self.division)
