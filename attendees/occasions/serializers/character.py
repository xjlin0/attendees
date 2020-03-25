from attendees.occasions.models import Character
from rest_framework import serializers


class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = [f.name for f in model._meta.fields if f.name not in ['is_removed']]

