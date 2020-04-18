import time

from django.db.models.expressions import F
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from rest_framework import viewsets
from rest_framework.exceptions import AuthenticationFailed

from attendees.persons.models import Attending
from attendees.persons.serializers import AttendingSerializer


@method_decorator([login_required], name='dispatch')
class ApiOrganizationAttendingViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Attending to be viewed or edited.
    """
    serializer_class = AttendingSerializer

    def get_queryset(self):
        current_user = self.request.user
        if current_user.belongs_to_organization_of(self.kwargs['organization_slug']):
            meets = self.request.query_params.getlist('meets[]', [])
            user_attended_gathering_ids = current_user.attendee.attendings.values_list('gathering__id', flat=True).distinct()
            return Attending.objects.select_related().prefetch_related().filter(
                meets__slug__in=meets,
                gathering__id__in=user_attended_gathering_ids,
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


api_organization_attending_viewset = ApiOrganizationAttendingViewSet