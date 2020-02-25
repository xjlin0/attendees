from attendees.persons.models import Attending
from rest_framework import serializers


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = [f.name for f in model._meta.fields if f.name not in ['is_removed']]

