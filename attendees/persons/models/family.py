from django.db import models
from model_utils.models import TimeStampedModel, SoftDeletableModel


class Family(TimeStampedModel, SoftDeletableModel):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    slug = models.SlugField(max_length=50, help_text='uniq key', blank=False, null=False, unique=True)
    attendees = models.ManyToManyField('persons.Attendee', through='FamilyAttendee', related_name='attendees')
    display_name = models.CharField(max_length=50, blank=True, null=True)
    display_order = models.SmallIntegerField(default=0, blank=False, null=False, db_index=True)

    def __str__(self):
        return '%s family' % (self.display_name,)

    class Meta:
        db_table = 'persons_families'
        verbose_name_plural = 'Families'
        ordering = ('display_order', '-modified',)

