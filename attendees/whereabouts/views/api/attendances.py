# from rest_framework import viewsets
# from rest_framework import permissions
# from attendees.occasions.models import Attendance
# from attendees.occasions.serializers import AttendanceSerializer
#
#
# class ApiAttendanceViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows Attendances to be viewed or edited.
#     """
#     queryset = Attendance.objects.select_related('character', 'team', 'attending', 'gathering', 'attending__attendee').filter(attending__divisions__slug__in=['children_ministry']).order_by('gathering__meet', '-gathering__start', 'character__display_order')
#     serializer_class = AttendanceSerializer
#
#
# api_attendance_viewset = ApiAttendanceViewSet
