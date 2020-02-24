from rest_framework import viewsets
from rest_framework import permissions
from attendees.occasions.models import Character
from attendees.occasions.serializers import CharacterSerializer


class ApiCharacterViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Participations to be viewed or edited.
    """
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    permission_classes = [permissions.IsAuthenticated]


api_character_viewset = ApiCharacterViewSet
