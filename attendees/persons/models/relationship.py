from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from model_utils.models import TimeStampedModel, SoftDeletableModel
from . import Utility, Note, Attendee


class Relationship(TimeStampedModel, SoftDeletableModel, Utility):
    notes = GenericRelation(Note)
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    from_attendee = models.ForeignKey(Attendee, related_name='from_attendee', on_delete=models.SET(0))
    to_attendee = models.ForeignKey(Attendee, related_name='to_attendee', on_delete=models.SET(0))
    relation = models.ForeignKey('persons.Relation', related_name='relation', null=False, blank=False, on_delete=models.SET(0), verbose_name='to_attendee is', help_text="[Title] What would from_attendee call to_attendee?")
    emergency_contact = models.BooleanField('to_attendee is the emergency contact?', null=False, blank=False, default=False, help_text="[from_attendee decide:] Notify to_attendee of from_attendee's emergency?")
    scheduler = models.BooleanField('to_attendee is the scheduler?', null=False, blank=False, default=False, help_text="[from_attendee decide:] to_attendee can view/change the schedules of the from_attendee?")
    in_family = models.ForeignKey('persons.Family', null=True, blank=True, on_delete=models.SET_NULL, related_name="in_family")
    finish = models.DateTimeField(blank=False, null=False, default=Utility.forever, help_text="The relation will be ended at when")

    class Meta:
        db_table = 'persons_relationships'
        constraints = [
            models.UniqueConstraint(fields=['from_attendee', 'to_attendee', 'relation'], name="attendee_relation")
        ]

    def __str__(self):
        return '%s %s %s' % (self.from_attendee, self.to_attendee, self.relation)
