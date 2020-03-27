from django.db import models
from django.contrib.contenttypes.fields import GenericRelation

from model_utils.models import TimeStampedModel, SoftDeletableModel

from attendees.persons.models import Utility, Note

from . import Assembly, Character


class AssemblyCharacter(TimeStampedModel, SoftDeletableModel, Utility):
    notes = GenericRelation(Note)
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    assembly = models.ForeignKey(Assembly, on_delete=models.SET(0), null=False, blank=False)
    character = models.ForeignKey(Character, on_delete=models.SET(0), null=False, blank=False)

    class Meta:
        db_table = 'occasions_assembly_characters'
        verbose_name_plural = 'Assembly Characters'
        constraints = [
            models.UniqueConstraint(fields=['assembly', 'character'], name="assembly_character")
        ]

    def __str__(self):
        return '%s %s' % (self.assembly or '', self.character or '')
