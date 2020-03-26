from django.db import models
from django.urls import reverse
from django.contrib.contenttypes.fields import GenericRelation, GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from model_utils.models import TimeStampedModel, SoftDeletableModel

from attendees.persons.models import Utility, Note


class Meet(TimeStampedModel, SoftDeletableModel, Utility):
    notes = GenericRelation(Note)
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    assembly = models.ForeignKey('occasions.Assembly', null=True, blank=True, on_delete=models.SET_NULL)
    attendings = models.ManyToManyField('persons.Attending', through='persons.AttendingMeet', related_name="attendings")
    start = models.DateTimeField(null=True, blank=True, help_text='optional')
    finish = models.DateTimeField(null=True, blank=True, help_text='optional')
    display_name = models.CharField(max_length=50, blank=True, null=True, db_index=True, help_text="The Rock, Little Foot, singspiration, A/V control, etc.")
    slug = models.SlugField(max_length=50, blank=False, null=False, unique=True)
    info = models.CharField(max_length=255, blank=True, null=True)
    url = models.URLField(max_length=255, blank=True, null=True)
    site_type = models.ForeignKey(ContentType, on_delete=models.SET(0), help_text='location: django_content_type id for table name')
    site_id = models.BigIntegerField()
    location = GenericForeignKey('site_type', 'site_id')

    # def save(self):
    #     pass # https://stackoverflow.com/a/27241824

    def get_absolute_url(self):
        return reverse('character_detail', args=[str(self.id)])

    class Meta:
        db_table = 'occasions_meets'

    def __str__(self):
        return '%s %s %s' % (self.display_name or '', self.info or '', self.url or '')
