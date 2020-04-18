import time

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from rest_framework import viewsets
from rest_framework.exceptions import AuthenticationFailed

from attendees.occasions.models import Team
from attendees.occasions.serializers import TeamSerializer


@method_decorator([login_required], name='dispatch')
class ApiOrganizationTeamViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Team to be viewed or edited.
    """
    serializer_class = TeamSerializer

    def get_queryset(self):
        if self.request.user.belongs_to_organization_of(self.kwargs['organization_slug']):
            meets = self.request.query_params.getlist('meets[]', [])
            return Team.objects.filter(
                meet__slug__in=meets,
                meet__assembly__division__organization__slug=self.kwargs['organization_slug']
            ).order_by(
                'display_order',
            )

        else:
            time.sleep(2)
            raise AuthenticationFailed(detail='Have you registered any events of the organization?')


api_organization_team_viewset = ApiOrganizationTeamViewSet