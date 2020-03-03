from rest_framework import viewsets
from attendees.occasions.models import Participation
from attendees.occasions.serializers import ParticipationSerializer


class ApiParticipationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Participations to be viewed or edited.
    """
    queryset = Participation.objects.select_related('character', 'team', 'attending', 'gathering', 'attending__attendee').filter(attending__divisions__slug__in=['children_ministry']).order_by('gathering__meet', '-gathering__start', 'character__display_order')
    serializer_class = ParticipationSerializer

    # def get_queryset(self):
    #     """
    #     Optionally restricts the returned purchases to chosen meets,
    #     by filtering against a `username` query parameter in the URL.
    #     """
    #     queryset = Purchase.objects.all()
    #     username = self.request.query_params.get('username', None)
    #     if username is not None:
    #         queryset = queryset.filter(purchaser__username=username)
    #     return queryset

api_participation_viewset = ApiParticipationViewSet
