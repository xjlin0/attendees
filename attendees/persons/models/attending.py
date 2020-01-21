from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.urls import reverse
from django.contrib.contenttypes.fields import GenericRelation
from django.utils.functional import cached_property

from model_utils.models import TimeStampedModel, SoftDeletableModel

from . import Note, Utility, Attendee, Registration


class Attending(TimeStampedModel, SoftDeletableModel, Utility):
    link_notes = GenericRelation(Note)
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    registration = models.ForeignKey(Registration, null=True, on_delete=models.SET_NULL)
    attendee = models.ForeignKey(Attendee, null=True, on_delete=models.SET_NULL)
    # addresses = models.ManyToManyField('Address', through='AttendingAddress')
    # program_sessions = models.ManyToManyField('ProgramSession', through='ProgramParticipation')
    price = models.DecimalField(max_digits=8, decimal_places=2, default=999999, validators=[MinValueValidator(0)])
    age = models.IntegerField(null=True, blank=True)
    attending_type = models.CharField(max_length=20, null=True)
    divisions = models.ManyToManyField('whereabouts.Division', through='AttendingDivision')
    belief = models.CharField(max_length=20, null=True)
    bed_needs = models.IntegerField(default=1)
    mobility = models.IntegerField(default=0)

    def clean(self):
        if self.bed_needs < 1 and self.age is None:
            raise ValidationError("You must specify age for kid")

    def get_absolute_url(self):
        return reverse('attending_detail', args=[str(self.id)])


    class Meta:
        db_table = 'persons_attendings'
        ordering = ['registration']

    @property
    def main_contact(self):
        return self.registration.main_attendee

    # @cached_property
    # def division_names(self):
    #     return ",".join([d.name for d in self.divisions.all()])

    # @cached_property
    # def all_addresses(self):
    #     return ",".join([str(a) for a in self.addresses.all()])

    # def __str__(self):
    #     return '%s %s %s' % (self.attendee, self.division_names, self.bed_needs)
