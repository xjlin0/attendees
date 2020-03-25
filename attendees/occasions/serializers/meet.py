from attendees.occasions.models import Meet
from rest_framework import serializers


class MeetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meet
        fields = [f.name for f in model._meta.fields if f.name not in ['is_removed']]

