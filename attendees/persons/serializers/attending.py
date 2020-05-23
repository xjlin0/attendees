from attendees.persons.models import Attending
from .attendee import AttendeeSerializer
from rest_framework import serializers


class AttendingSerializer(serializers.ModelSerializer):
    meets_info = serializers.SerializerMethodField()
    attendee = AttendeeSerializer(many=False, read_only=True)

    def get_meets_info(self, obj):
        return {am.meet.slug: am.character.slug for am in obj.attendingmeet_set.all()}

    class Meta:
        model = Attending
        fields = '__all__'

