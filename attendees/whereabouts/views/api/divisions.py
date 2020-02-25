from rest_framework import viewsets
from attendees.whereabouts.models import Division
from attendees.whereabouts.serializers import DivisionSerializer


class ApiDivisionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Division to be viewed or edited.
    """
    queryset = Division.objects.all()
    serializer_class = DivisionSerializer


api_division_viewset = ApiDivisionViewSet
