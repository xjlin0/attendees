from rest_framework import viewsets
from attendees.occasions.models import Character
from attendees.occasions.serializers import CharacterSerializer


class ApiCharacterViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Character to be viewed or edited.
    """
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer


api_character_viewset = ApiCharacterViewSet
