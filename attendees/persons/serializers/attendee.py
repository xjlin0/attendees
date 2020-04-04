from attendees.persons.models import Attendee
from rest_framework import serializers


class AttendeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendee
        fields = [f.name for f in model._meta.fields if f.name not in ['is_removed']] + ['display_label']

