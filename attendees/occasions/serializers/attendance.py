from attendees.occasions.models import Attendance
from rest_framework import serializers


class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = [f.name for f in model._meta.fields if f.name not in ['is_removed']] + ['attendance_label']

