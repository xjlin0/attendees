import time

from rest_framework import viewsets
from rest_framework.exceptions import AuthenticationFailed
from django.db.models import Q
from attendees.occasions.models import Attendance
from attendees.persons.models import Attendee
from attendees.occasions.serializers import AttendanceSerializer
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@method_decorator([login_required], name='dispatch')
class ApiFamilyOrganizationAttendancesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Attendances to be viewed.   All authenticated user (and
    the users kids/care receiver)'s Attendance will be shown.
    """
    serializer_class = AttendanceSerializer

    def get_queryset(self):
        """
        :permission: this API is only for authenticated users (participants, coworker or organization).
                     Anonymous users should not get any info from this API.
        :query: Find all gatherings of all Attendances of the current user and their kid/care receiver,
                , so all their "family" Attendances will show up.
        :return:  Attendances of the logged in user and their kids/care receivers
        """
        # Todo 1. reorganize the view/api/js files to match urls that make sense
        #      2. extract current_user.belongs_to_organization_of ... to route guard
        #      3. check if the meets belongs to the organization
        current_user = self.request.user
        if current_user.organization:
            meets = self.request.query_params.getlist('meets[]', [])
            start = self.request.query_params.get('start', None)
            finish = self.request.query_params.get('finish', None)
            return Attendance.objects.select_related(
                'character', 'team', 'attending', 'gathering', 'attending__attendee').filter(
                    Q(attending__attendee=current_user.attendee)
                    |
                    Q(attending__attendee__in=current_user.attendee.relations.filter(
                        to_attendee__relation__in=Attendee.BE_LISTED_KEYWORDS,
                    )),
                    gathering__meet__assembly__division__organization__slug=current_user.organization.slug,
                    gathering__meet__slug__in=meets,
                    gathering__start__gte=start,
                    gathering__finish__lte=finish,
                ).order_by('gathering__meet', '-gathering__start', 'character__display_order')

        else:
            time.sleep(2)
            raise AuthenticationFailed(detail='Have you registered any events of the organization?')


api_family_organization_attendances_viewset = ApiFamilyOrganizationAttendancesViewSet
