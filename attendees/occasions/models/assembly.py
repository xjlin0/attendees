from django.db import models
from django.urls import reverse
from django.contrib.contenttypes.fields import GenericRelation

from model_utils.models import TimeStampedModel, SoftDeletableModel

from attendees.persons.models import Utility, Note


class Assembly(TimeStampedModel, SoftDeletableModel, Utility):
    notes = GenericRelation(Note)
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    start = models.DateTimeField(null=True, blank=True, help_text='optional')
    finish = models.DateTimeField(null=True, blank=True, help_text='optional')
    addresses = models.ManyToManyField('whereabouts.Address', through='AssemblyAddress')
    # characters = models.ManyToManyField('Character', through='AssemblyCharacter')
    display_name = models.CharField(max_length=50, blank=False, null=False)
    slug = models.SlugField(max_length=50, blank=False, null=False, unique=True, help_text='format: Organization_name-Assembly_name')
    division = models.ForeignKey('whereabouts.Division', null=False, blank=False, on_delete=models.SET(0))

    def get_absolute_url(self):
        return reverse('assembly_detail', args=[str(self.id)])

    class Meta:
        db_table = 'occasions_assemblies'
        ordering = ('display_name',)

    def __str__(self):
        return '%s' % self.display_name

    def get_addresses(self):
        return "\n".join([a.street1 or '' + a.city or '' for a in self.addresses.all()])


# from rest_framework import serializers
#
#
# class AssemblySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Assembly
#         fields = ['id', 'name', 'division', 'ttttt']

# from mainsite.models.assembly import AssemblySerializer
# k2=Assembly.objects.get(pk=2)
# serializer=AssemblySerializer(k2)
# serializer.data
# #=> {'id': 2, 'name': '2019 Fall kid programs', 'division': 'none', 'ttttt': 'ttttt'}
