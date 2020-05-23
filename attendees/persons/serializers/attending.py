from attendees.persons.models import Attending
from .attendee import AttendeeSerializer
from rest_framework import serializers


class AttendingSerializer(serializers.ModelSerializer):
    meets_object = serializers.SerializerMethodField()
    # character = serializers.CharField()
    attendee = AttendeeSerializer(many=False, read_only=True)

    def get_meets_object(self, obj):
        return {m.slug: m.display_name for m in obj.meets.all()}

    class Meta:
        model = Attending
        fields = '__all__'

