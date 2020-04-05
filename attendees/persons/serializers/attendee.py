from attendees.persons.models import Attendee
from rest_framework import serializers


class AttendeeSerializer(serializers.ModelSerializer):
    parents_kids_names = serializers.CharField()
    all_email_addresses = serializers.CharField()

    class Meta:
        model = Attendee
        fields = [f.name for f in model._meta.fields if f.name not in ['is_removed']] + [
            'display_label',
            'parents_kids_names',
            'all_email_addresses',
        ]

