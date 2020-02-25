from rest_framework import viewsets
from attendees.occasions.models import Team
from attendees.occasions.serializers import TeamSerializer


class ApiTeamViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Team to be viewed or edited.
    """
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


api_team_viewset = ApiTeamViewSet
