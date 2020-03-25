from rest_framework import viewsets
from attendees.persons.models import Attending
from attendees.persons.serializers import AttendingSerializer


class ApiAttendingViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Attending to be viewed or edited.
    """
    queryset = Attending.objects.all()
    serializer_class = AttendingSerializer


api_attending_viewset = ApiAttendingViewSet
