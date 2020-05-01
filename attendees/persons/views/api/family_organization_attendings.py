import time

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from rest_framework import viewsets
from rest_framework.exceptions import AuthenticationFailed
from attendees.persons.services import AttendingService
from attendees.persons.serializers import AttendingSerializer


@method_decorator([login_required], name='dispatch')
class ApiFamilyOrganizationAttendingsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Attending to be viewed or edited.
    """
    serializer_class = AttendingSerializer

    def get_queryset(self):
        """
        :permission: this API is only for coworkers/organizers, ordinary participants should get nothing from this API
        :query: Find all gatherings of the current user and their kids/care-receivers, then list all attendings of the
                found gatherings. So if the current user didn't participate(attending), no info will be shown.
        :return: all Attendings with participating meets(group) and character(role)
        """
        current_user = self.request.user
        if current_user.organization:
            return AttendingService.by_family_organization_attendings(
                current_user=current_user,
                meet_slugs=self.request.query_params.getlist('meets[]', [])
            )  # Todo: probably need to check if the meets belongs to the organization?

        else:
            time.sleep(2)
            raise AuthenticationFailed(detail='Have you registered any events of the organization?')


api_family_organization_attendings_viewset = ApiFamilyOrganizationAttendingsViewSet
