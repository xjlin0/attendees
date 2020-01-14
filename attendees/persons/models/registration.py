from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.contenttypes.fields import GenericRelation
from model_utils.models import TimeStampedModel, SoftDeletableModel

from attendees.occasions.models import Event

from . import Utility, Note, Attendee


class Registration(TimeStampedModel, SoftDeletableModel, Utility):
    notes = GenericRelation(Note)
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    event = models.ForeignKey('occasions.Event', null=True, on_delete=models.SET_NULL)
    main_attendee = models.ForeignKey(Attendee, null=True, on_delete=models.SET_NULL)
    apply_type = models.CharField(max_length=20, null=True, help_text="online or paper")
    apply_key = models.CharField(max_length=50, null=True, help_text="E1T1F1 or #001")
    donation = models.DecimalField(max_digits=8, decimal_places=2, default=999999, validators=[MinValueValidator(0)])

    # @property
    # def price_sum(self):
    #     return sum([attending.price for attending in self.attending_set.all()]) + self.donation
    # # TODO: please check if attending_set works !!!!!!!!!
    #
    # def __str__(self):
    #     return '%s %s %s' % (self.apply_type, self.main_attendee, self.price_sum)

    def __str__(self):
        return '%s %s' % (self.apply_type, self.main_attendee)

    class Meta:
        db_table = 'persons_registrations'
        ordering = ('main_attendee__last_name', 'main_attendee__first_name')
