from rest_framework import viewsets
from rest_framework import permissions
from attendees.occasions.models import Participation
from attendees.occasions.serializers import ParticipationSerializer


class ApiParticipationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Participations to be viewed or edited.
    """
    queryset = Participation.objects.select_related('character', 'team', 'attending', 'gathering', 'attending__attendee').filter(attending__divisions__slug__in=['children_ministry']).order_by('gathering__meet', '-gathering__start', 'character__display_order')
    serializer_class = ParticipationSerializer
    permission_classes = [permissions.IsAuthenticated]


api_participation_viewset = ApiParticipationViewSet
