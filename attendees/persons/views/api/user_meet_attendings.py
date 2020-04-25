import time

from django.db.models.expressions import F
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from rest_framework import viewsets
from rest_framework.exceptions import AuthenticationFailed

from attendees.persons.models import Attending
from attendees.persons.serializers import AttendingSerializer


@method_decorator([login_required], name='dispatch')
class ApiUserMeetAttendingsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Attending to be viewed or edited.
    """
    serializer_class = AttendingSerializer

    def get_queryset(self):
        """
        :permission: this API is only for coworkers/organizers, ordinary participants should get nothing from this API
        :query: Find all gatherings of the current user, then list all attendings of the found gatherings.
                So if the current user didn't participate(attending), no info will be shown
        :return: all Attendings with participating meets(group) and character(role)
        """
        current_user = self.request.user
        if current_user.organization:
            meets = self.request.query_params.getlist('meets[]', [])
            user_attended_gathering_ids = current_user.attendee.attendings.values_list('gathering__id', flat=True).distinct()
            return Attending.objects.select_related().prefetch_related().filter(
                #registration_start/finish within the selected time period.
                meets__slug__in=meets,
                gathering__id__in=user_attended_gathering_ids,
                meets__assembly__division__organization__slug=current_user.organization.slug,
            ).annotate(
                meet=F('attendingmeet__meet__display_name'),
                character=F('attendingmeet__character__display_name'),
            ).order_by(
                'attendee',
            ).distinct()

        else:
            time.sleep(2)
            raise AuthenticationFailed(detail='Have you registered any events of the organization?')


api_user_meet_attendings_viewset = ApiUserMeetAttendingsViewSet
