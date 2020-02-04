from django.db import models
from django.urls import reverse
from django.core.exceptions import ValidationError
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.postgres.fields import JSONField

from model_utils.models import TimeStampedModel, SoftDeletableModel

from attendees.persons.models import Utility, Note
from attendees.occasions.models import Meet, MeetAddress


class Address(TimeStampedModel, SoftDeletableModel, Utility):
    notes = GenericRelation(Note)
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    display_name = models.CharField(max_length=50, blank=True, null=True, db_index=True, help_text='optional label')
    meets = models.ManyToManyField(Meet, through=MeetAddress)
    attendees = models.ManyToManyField('persons.Attendee', through='persons.AttendeeAddress')
    email1 = models.EmailField(blank=True, null=True, max_length=254, db_index=True)
    email2 = models.EmailField(blank=True, null=True, max_length=254)
    phone1 = models.CharField(max_length=15, blank=True, null=True, db_index=True)
    phone2 = models.CharField(max_length=15, blank=True, null=True)
    address_type = models.CharField(max_length=20, default='street', blank=True, null=True, help_text='mailing, remote or street address')
    street1 = models.CharField(max_length=50, blank=True, null=True)
    street2 = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=10, default='CA', blank=True, null=True)
    zip_code = models.CharField(max_length=10, null=True, blank=True)
    url = models.URLField(max_length=255, blank=True, null=True)
    fields = JSONField(default=dict, null=True, blank=True, help_text="please keep {} here even there's no data")

    def get_absolute_url(self):
        return reverse('address_detail', args=[str(self.id)])

    def clean(self):  #needs to check if fields are valid json (even empty json)
        if not (self.street1 or self.phone1 or self.url or self.fields):
            raise ValidationError("You must specify at least a street or telephone or url or field")

    class Meta:
        db_table = 'whereabouts_addresses'
        verbose_name_plural = 'Addresses'

    @property
    def street(self):
        return ('{street1} {street2}').format(street1=self.street1, street2=self.street2 or '').strip()

    def __str__(self):
        return '%s, %s, %s. %s %s' % (self.display_name or self.attendees.first() or '', self.street, self.city, self.zip_code, self.phone1)
