from rest_framework import viewsets
from rest_framework import permissions
from attendees.whereabouts.models import Division
from attendees.whereabouts.serializers import DivisionSerializer


class ApiDivisionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Participations to be viewed or edited.
    """
    queryset = Division.objects.all()
    serializer_class = DivisionSerializer
    permission_classes = [permissions.IsAuthenticated]


api_division_viewset = ApiDivisionViewSet
