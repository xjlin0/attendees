from django.db import models
from model_utils.models import TimeStampedModel, SoftDeletableModel


class RelationRole(TimeStampedModel, SoftDeletableModel):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    corresponding_relations = models.ManyToManyField('self', through='RelationshipDefault', symmetrical=False, related_name='corresponding_relations+')
    slug = models.SlugField(max_length=50, blank=False, null=False, unique=True, help_text="uniq key")
    display_name = models.CharField(max_length=50, blank=True, null=True)
    display_order = models.SmallIntegerField(default=0, blank=False, null=False, db_index=True)

    def __str__(self):
        return '%s' % self.display_name

    class Meta:
        db_table = 'persons_relation_roles'
        ordering = ('display_order', '-modified',)

