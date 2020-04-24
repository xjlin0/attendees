import time

from django.db.models.expressions import F
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from rest_framework import viewsets
from rest_framework.exceptions import AuthenticationFailed
from django.db.models import Q
from attendees.persons.models import Attending, Attendee
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
        if current_user.belongs_to_organization_of(self.kwargs['organization_slug']):
            # Todo: probably need to check if the meets belongs to the organization?
            meets = self.request.query_params.getlist('meets[]', [])
            return Attending.objects.select_related().prefetch_related().filter(
                Q(attendee=current_user.attendee)
                |
                Q(attendee__in=current_user.attendee.relations.filter(
                    to_attendee__relation__in=Attendee.BE_LISTED_KEYWORDS,
                )),
                #registration_start/finish within the selected time period.
                meets__slug__in=meets,
                meets__assembly__division__organization__slug=self.kwargs['organization_slug'],
            ).annotate(
                meet=F('attendingmeet__meet__display_name'),
                character=F('attendingmeet__character__display_name'),
            ).order_by(
                'attendee',
            )

        else:
            time.sleep(2)
            raise AuthenticationFailed(detail='Have you registered any events of the organization?')


api_family_organization_attendings_viewset = ApiFamilyOrganizationAttendingsViewSet
