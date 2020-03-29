from rest_framework import viewsets
from attendees.occasions.models import Gathering
from attendees.occasions.serializers import GatheringSerializer
import logging


logger = logging.getLogger(__name__)

class ApiGatheringViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Team to be viewed or edited.
    """
    # queryset = Gathering.objects.all()
    serializer_class = GatheringSerializer


    def get_queryset(self):
        if self.request.user.belongs_to_organization_and_division(self.kwargs['organization_slug'], self.kwargs['division_slug']):
            meets = self.request.query_params.getlist('meets[]', [])
            logger.info("hi jack 20 here is self.request.query_params: ")
            logger.info(self.request.query_params)
            logger.info("hi jack 22 here is meets: ")
            logger.info(meets)
            return Gathering.objects.filter(meet__slug__in=meets).order_by('meet', '-start')

    # def get_queryset(self):
    #     logger.info("hi jack 18 here is self.kwargs: ")
    #     logger.info(self.kwargs)
    #     logger.info("hi jack 20 here is self.request.query_params: ")
    #     logger.info(self.request.query_params)
    #
    #     return Gathering.objects.all()

api_gathering_viewset = ApiGatheringViewSet
