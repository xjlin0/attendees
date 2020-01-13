from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from model_utils.models import TimeStampedModel, SoftDeletableModel


class Note(TimeStampedModel, SoftDeletableModel):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    content_type = models.ForeignKey(ContentType, on_delete=models.SET(0))
    object_id = models.BigIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    note_type = models.CharField(max_length=20, blank=True, null=True)
    note_text = models.TextField()

    def __str__(self):
        return '%s %s %s' % (self.content_type, self.content_object, self.note_text)

    class Meta:
        db_table = 'persons_notes'
        ordering = ('-modified',)

    # @property
    # def iso_updated_at(self):
    #     return self.modified.isoformat()
