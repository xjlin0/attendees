from django.db import models
from model_utils.models import TimeStampedModel, SoftDeletableModel


class Relation(TimeStampedModel, SoftDeletableModel):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    slug = models.SlugField(max_length=50, blank=False, null=False, unique=True, help_text="uniq key")
    display_name = models.CharField(max_length=50, blank=True, null=True)
    display_order = models.SmallIntegerField(default=0, blank=False, null=False, db_index=True)
    emergency_contact = models.BooleanField(null=False, blank=False, default=False, help_text="default emergency contact")
    scheduler = models.BooleanField(null=False, blank=False, default=False, help_text="default scheduler")

    def __str__(self):
        return '%s %s %s' % (self.display_name, self.slug, self.display_order)

    class Meta:
        db_table = 'persons_relations'
        ordering = ('display_order', '-modified',)

