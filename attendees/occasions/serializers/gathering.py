from attendees.occasions.models import Gathering
from rest_framework import serializers


class GatheringSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gathering
        fields = [f.name for f in model._meta.fields if f.name not in ['is_removed']] + ['gathering_label']

