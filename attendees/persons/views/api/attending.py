import time

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from rest_framework import viewsets
from rest_framework.exceptions import AuthenticationFailed

from attendees.persons.models import Attending
from attendees.persons.serializers import AttendingSerializer


@method_decorator([login_required], name='dispatch')
class ApiAttendingViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Attending to be viewed or edited.
    """
    serializer_class = AttendingSerializer

    def get_queryset(self):
        if self.request.user.belongs_to_organization_and_division(self.kwargs['organization_slug'], self.kwargs['division_slug']):
            meets = self.request.query_params.getlist('meets', [])
            return Attending.objects.filter(meets__slug__in=meets, meets__assembly__slug=self.kwargs['assembly_slug']).order_by('attendee')

        else:
            time.sleep(2)
            raise AuthenticationFailed(detail='Have you registered any events of the organization?')


api_attending_viewset = ApiAttendingViewSet
