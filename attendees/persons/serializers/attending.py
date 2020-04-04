from attendees.persons.models import Attending
from .attendee import AttendeeSerializer
from rest_framework import serializers


class AttendingSerializer(serializers.ModelSerializer):
    meet = serializers.CharField()
    character = serializers.CharField()
    attendee = AttendeeSerializer(many=False, read_only=True)

    class Meta:
        model = Attending
        fields = [f.name for f in model._meta.fields if f.name not in ['is_removed']] + [
            'attending_label',
            'meet',
            'character',
            'attendee',
        ]

