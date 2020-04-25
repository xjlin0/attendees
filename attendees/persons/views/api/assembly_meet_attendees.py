import time

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from rest_framework import viewsets
from rest_framework.exceptions import AuthenticationFailed

from attendees.persons.models import Attendee
from attendees.persons.serializers import AttendeeSerializer


@method_decorator([login_required], name='dispatch')
class ApiAssemblyMeetAttendeesSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Team to be viewed or edited.
    """
    serializer_class = AttendeeSerializer


    def get_queryset(self):
        if self.request.user.belongs_to_organization_and_division(self.kwargs['organization_slug'], self.kwargs['division_slug']):
            meets = self.request.query_params.getlist('meets[]', [])
            return Attendee.objects.filter(
                attendings__meets__slug__in=meets,
                attendings__meets__assembly__slug=self.kwargs['assembly_slug']
            ).order_by(
                'last_name',
                'last_name2',
                'first_name',
                'first_name2'
            )

        else:
            time.sleep(2)
            raise AuthenticationFailed(detail='Have you registered any events of the organization?')


api_assembly_meet_attendees_viewset = ApiAssemblyMeetAttendeesSet
