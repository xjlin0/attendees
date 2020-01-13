from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from model_utils.models import TimeStampedModel, SoftDeletableModel
from . import Utility, Attendee


class Relationship(TimeStampedModel, SoftDeletableModel, Utility):
    link_notes = GenericRelation('Note')
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    from_attendee = models.ForeignKey(Attendee, related_name='from_attendee', on_delete=models.SET(0))
    to_attendee = models.ForeignKey(Attendee, related_name='to_attendee', on_delete=models.SET(0))
    relation = models.CharField(max_length=32, null=False, blank=False, db_index=True)

    class Meta:
        db_table = 'persons_relationships'
        constraints = [
            models.UniqueConstraint(fields=['from_attendee', 'to_attendee'], name="from_attendee_to_attendee")
        ]

    def __str__(self):
        return '%s %s %s' % (self.from_attendee, self.to_attendee, self.relation)
