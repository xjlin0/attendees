from django.db import models
from model_utils.models import TimeStampedModel, SoftDeletableModel


class FamilyAttendee(TimeStampedModel, SoftDeletableModel):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    family = models.ForeignKey('persons.Family', null=False, blank=False, on_delete=models.SET(0), related_name="family")
    attendee = models.ForeignKey('persons.Attendee', null=False, blank=False, on_delete=models.SET(0), related_name="attendee")
    role = models.ForeignKey('persons.Relation', related_name='role', null=False, blank=False, on_delete=models.SET(0), verbose_name='attendee is', help_text="[Title] the family role of the attendee?")
    display_order = models.SmallIntegerField(default=0, blank=False, null=False, db_index=True)

    def __str__(self):
        return '%s %s %s' % (self.family, self.role, self.attendee)

    class Meta:
        db_table = 'persons_family_attendees'
        ordering = ('display_order', '-modified',)
        constraints = [
            models.UniqueConstraint(fields=['family', 'attendee'], name="family_attendee")
        ]

#0012_family_attendee_m2m
