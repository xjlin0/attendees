from attendees.occasions.models import Participation
from rest_framework import serializers


class ParticipationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participation
        fields = [f.name for f in model._meta.fields if f.name not in ['is_removed']] + ['gathering_label', 'attending_label', 'team_label', 'character_label']

