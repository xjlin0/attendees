from django.urls import path, include
from rest_framework import routers

from attendees.occasions.views import (
    assembly_attendance_list_view,
    # assembly_attendance_others_list_view,
    user_organization_attendance_list_view,
    api_attendance_viewset,
    api_character_viewset,
    api_team_viewset,
    api_gathering_viewset,
)


app_name = "occasions"

router = routers.DefaultRouter()
router.register('api/(?P<division_slug>.+)/(?P<assembly_slug>.+)/attendances', api_attendance_viewset, basename='attendance')
router.register('api/(?P<division_slug>.+)/(?P<assembly_slug>.+)/characters', api_character_viewset, basename='character')
router.register('api/(?P<division_slug>.+)/(?P<assembly_slug>.+)/teams', api_team_viewset, basename='team')
router.register('api/(?P<division_slug>.+)/(?P<assembly_slug>.+)/gatherings', api_gathering_viewset, basename='gathering')

urlpatterns = [
    path('', include(router.urls)),
    path("<slug:division_slug>/<slug:assembly_slug>/attendances/", view=assembly_attendance_list_view, name="assembly_attendances"),
    # path("<slug:division_slug>/<slug:assembly_slug>/attendings/", view=assembly_attendance_others_list_view, name="assembly_attendance_others"),
    path('user/organization_attendances/', view=user_organization_attendance_list_view, name='user_organization_attendance'),
]
