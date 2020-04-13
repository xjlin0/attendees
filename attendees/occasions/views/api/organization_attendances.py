import time

from rest_framework import viewsets
from rest_framework.exceptions import AuthenticationFailed

from attendees.occasions.models import Attendance
from attendees.occasions.serializers import AttendanceSerializer
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@method_decorator([login_required], name='dispatch')
class ApiOrganizationAttendanceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Attendances to be viewed or edited.
    """
    serializer_class = AttendanceSerializer

    def get_queryset(self):
        if self.request.user.belongs_to_organization_of(self.kwargs['organization_slug']):
            meets = self.request.query_params.getlist('meets[]', [])
            start = self.request.query_params.get('start', None)
            finish = self.request.query_params.get('finish', None)
            return Attendance.objects.select_related(
                'character', 'team', 'attending', 'gathering', 'attending__attendee').filter(
                    gathering__meet__assembly__division__organization__slug=self.kwargs['organization_slug'],
                    gathering__meet__slug__in=meets,
                    gathering__start__gte=start,
                    gathering__finish__lte=finish,
                ).order_by('gathering__meet', '-gathering__start', 'character__display_order')

        else:
            time.sleep(2)
            raise AuthenticationFailed(detail='Have you registered any events of the organization?')


api_organization_attendance_viewset = ApiOrganizationAttendanceViewSet
