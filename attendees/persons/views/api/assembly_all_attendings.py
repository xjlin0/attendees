import time

from django.db.models.expressions import F
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from rest_framework import viewsets
from rest_framework.exceptions import AuthenticationFailed

from attendees.persons.models import Attending
from attendees.persons.serializers import AttendingSerializer


@method_decorator([login_required], name='dispatch')
class ApiAssemblyMeetAttendingsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Attending to be viewed or edited.
    """
    serializer_class = AttendingSerializer

    def get_queryset(self):
        if self.request.user.belongs_to_organization_and_division(self.kwargs['organization_slug'], self.kwargs['division_slug']):
            # Todo: probably also need to check if the assembly belongs to the division
            meets = self.request.query_params.getlist('meets[]', [])
            characters = self.request.query_params.getlist('characters[]', [])
            return Attending.objects.select_related().prefetch_related().filter(
                meets__slug__in=meets,
                attendingmeet__character__slug__in=characters,
                meets__assembly__slug=self.kwargs['assembly_slug'],
            ).annotate(
                meet=F('attendingmeet__meet__display_name'),
                character=F('attendingmeet__character__display_name'),
            ).order_by(
                'attendee',
            )

        else:
            time.sleep(2)
            raise AuthenticationFailed(detail='Have you registered any events of the organization?')


api_assembly_meet_attendings_viewset = ApiAssemblyMeetAttendingsViewSet
