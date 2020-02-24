from attendees.occasions.models import Participation
from rest_framework import serializers


class ParticipationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participation
        fields = '__all__'
        exclude = ['is_removed']
