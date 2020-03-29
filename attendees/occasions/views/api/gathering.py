from rest_framework import viewsets
from attendees.occasions.models import Gathering
from attendees.occasions.serializers import GatheringSerializer
import logging


logger = logging.getLogger(__name__)

class ApiGatheringViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Team to be viewed or edited.
    """

    serializer_class = GatheringSerializer


    def get_queryset(self):
        if self.request.user.belongs_to_organization_and_division(self.kwargs['organization_slug'], self.kwargs['division_slug']):
            meets = self.request.query_params.getlist('meets[]', [])
            return Gathering.objects.filter(meet__slug__in=meets).order_by('meet', '-start')

api_gathering_viewset = ApiGatheringViewSet
