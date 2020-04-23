from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from rest_framework import viewsets
from rest_framework.exceptions import AuthenticationFailed
import time
from attendees.occasions.models import Gathering
from attendees.occasions.serializers import GatheringSerializer


@method_decorator([login_required], name='dispatch')
class ApiAssemblyMeetGatheringsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Team to be viewed or edited.
    """

    serializer_class = GatheringSerializer

    def get_queryset(self):
        if self.request.user.belongs_to_organization_and_division(self.kwargs['organization_slug'], self.kwargs['division_slug']):
            # Todo: probably need to check if the assembly belongs to the division
            meets = self.request.query_params.getlist('meets[]', [])
            return Gathering.objects.filter(
                meet__slug__in=meets,
                meet__assembly__slug=self.kwargs['assembly_slug'],
            ).order_by(
                'meet',
                '-start',
            )

        else:
            time.sleep(2)
            raise AuthenticationFailed(detail='Have you registered any events of the organization?')


api_assembly_meet_gatherings_viewset = ApiAssemblyMeetGatheringsViewSet
