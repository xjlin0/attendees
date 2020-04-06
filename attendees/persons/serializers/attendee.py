from attendees.persons.models import Attendee
from rest_framework import serializers


class AttendeeSerializer(serializers.ModelSerializer):
    parents_notifiers_names = serializers.CharField()
    self_email_addresses = serializers.CharField()
    caregiver_email_addresses = serializers.CharField()
    self_phone_numbers = serializers.CharField()
    caregiver_phone_numbers = serializers.CharField()

    class Meta:
        model = Attendee
        fields = [f.name for f in model._meta.fields if f.name not in ['is_removed']] + [
            'display_label',
            'parents_notifiers_names',
            'self_email_addresses',
            'caregiver_email_addresses',
            'self_phone_numbers',
            'caregiver_phone_numbers',
        ]

