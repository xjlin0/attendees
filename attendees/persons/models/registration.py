from django.db import models
from django.contrib.postgres.fields.jsonb import JSONField
from django.contrib.postgres.indexes import GinIndex
from django.contrib.contenttypes.fields import GenericRelation
from model_utils.models import TimeStampedModel, SoftDeletableModel


from . import Utility, Note, Attendee


class Registration(TimeStampedModel, SoftDeletableModel, Utility):
    notes = GenericRelation(Note)
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    assembly = models.ForeignKey('occasions.Assembly', null=True, on_delete=models.SET_NULL)
    main_attendee = models.ForeignKey(Attendee, null=True, on_delete=models.SET_NULL)
    infos = JSONField(null=True, blank=True, default=dict, help_text='Example: {"price": "150.75", "donation": "85.00", "credit": "35.50", "apply_type": "online", "apply_key": "001"}. Please keep {} here even no data')

    # @property
    # def price_sum(self):
    #     return sum([attending.price for attending in self.attending_set.all()]) + self.donation
    # # TODO: please check if attending_set works !!!!!!!!!
    #
    # def __str__(self):
    #     return '%s %s %s' % (self.apply_type, self.main_attendee, self.price_sum)

    def __str__(self):
        return '%s' % (self.main_attendee,)

    @property
    def main_attendee_name(self):
        return self.main_attendee

    class Meta:
        db_table = 'persons_registrations'
        ordering = ('assembly', 'main_attendee__last_name', 'main_attendee__first_name')
        indexes = [
            GinIndex(fields=['infos'], name='registration_infos_gin', ),
        ]
