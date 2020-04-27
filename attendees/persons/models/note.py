from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from model_utils.models import TimeStampedModel, SoftDeletableModel


class Note(TimeStampedModel, SoftDeletableModel):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    content_type = models.ForeignKey(ContentType, on_delete=models.SET(0))
    object_id = models.BigIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    category = models.CharField(max_length=20, default='normal', blank=False, null=False, db_index=True, help_text="normal, for-address, etc")
    display_order = models.SmallIntegerField(default=0, blank=False, null=False)
    body = models.TextField()

    def __str__(self):
        return '%s %s %s' % (self.content_type, self.content_object, self.body)

    class Meta:
        db_table = 'persons_notes'
        ordering = ('display_order', '-modified',)

    # @property
    # def iso_updated_at(self):
    #     return self.modified.isoformat()
