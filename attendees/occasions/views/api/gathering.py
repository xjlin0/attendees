from rest_framework import viewsets
from attendees.occasions.models import Gathering
from attendees.occasions.serializers import GatheringSerializer


class ApiGatheringViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Team to be viewed or edited.
    """
    queryset = Gathering.objects.all()
    serializer_class = GatheringSerializer


api_gathering_viewset = ApiGatheringViewSet
