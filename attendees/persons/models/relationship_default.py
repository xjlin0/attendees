from django.db import models
from model_utils.models import TimeStampedModel, SoftDeletableModel


class RelationshipDefault(TimeStampedModel, SoftDeletableModel):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    from_relation_role = models.ForeignKey('persons.RelationRole', related_name='from_relation_role', on_delete=models.SET(0))
    to_relation_role = models.ForeignKey('persons.RelationRole', related_name='to_relation_role', on_delete=models.SET(0))
    slug = models.SlugField(max_length=50, blank=False, null=False, unique=True, help_text="uniq key")
    display_name = models.CharField(max_length=50, blank=True, null=True, help_text="from_relation_role would call to_relation_role what?")
    display_order = models.SmallIntegerField(default=0, blank=False, null=False, db_index=True)
    emergency_contact = models.BooleanField(null=False, blank=False, default=False, help_text="to_relation is from_relation's emergency_contact?")
    scheduler = models.BooleanField(null=False, blank=False, default=False, help_text="to_relation is from_relation's scheduler?")

    def __str__(self):
        return '%s %s %s' % (self.from_relation_role, self.to_relation_role, self.display_order)

    class Meta:
        db_table = 'persons_relationship_defaults'
        ordering = ('display_order', '-modified',)
        constraints = [
            models.UniqueConstraint(fields=['from_relation_role', 'to_relation_role'], name="from_relation_to_relation_role")
        ]

