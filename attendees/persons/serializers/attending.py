from attendees.persons.models import Attending
from rest_framework import serializers


class AttendingSerializer(serializers.ModelSerializer):
    meet = serializers.CharField()
    character = serializers.CharField()

    class Meta:
        model = Attending
        fields = [f.name for f in model._meta.fields if f.name not in ['is_removed']] + ['attending_label', 'meet', 'character']

