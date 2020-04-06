from django.db import models
from django.contrib.postgres.fields.jsonb import JSONField
from django.contrib.contenttypes.fields import GenericRelation, GenericForeignKey
from model_utils.models import TimeStampedModel, SoftDeletableModel
from django.contrib.contenttypes.models import ContentType

from attendees.persons.models import Utility, Note


class Team(TimeStampedModel, SoftDeletableModel, Utility):
    notes = GenericRelation(Note)
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    meet = models.ForeignKey('Meet', null=False, blank=False, on_delete=models.SET(0))
    slug = models.SlugField(max_length=50, blank=False, null=False, unique=True)
    display_name = models.CharField(max_length=50, blank=True, null=True)
    display_order = models.SmallIntegerField(default=0, blank=False, null=False)
    infos = JSONField(null=True, blank=True, default=dict, help_text='Example: {"link": "https://..."}. Please keep {} here even no data')
    site_type = models.ForeignKey(ContentType, on_delete=models.SET(0), help_text='location: django_content_type id for table name')
    site_id = models.BigIntegerField()
    location = GenericForeignKey('site_type', 'site_id')

    class Meta:
        db_table = 'occasions_teams'

    def __str__(self):
        return '%s %s' % (self.meet, self.display_name or '')

