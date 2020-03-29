from django.urls import path, include
from rest_framework import routers

from attendees.occasions.views import (
    assembly_participation_attendance_list_view,
    assembly_participation_student_list_view,
    api_participation_viewset,
    api_character_viewset,
    api_team_viewset,
    api_gathering_viewset,
)


app_name = "occasions"

router = routers.DefaultRouter()
router.register('api/(?P<division_slug>.+)/(?P<assembly_slug>.+)/participations', api_participation_viewset, basename='participation')
router.register('api/characters', api_character_viewset, basename='character')
router.register('api/teams', api_team_viewset, basename='team')
router.register('api/(?P<division_slug>.+)/(?P<assembly_slug>.+)/gatherings', api_gathering_viewset, basename='gathering')

urlpatterns = [
    path('', include(router.urls)),
    path("<slug:division_slug>/<slug:assembly_slug>/participations/", view=assembly_participation_attendance_list_view, name="children_ministry_participations_leaders"),
    # path("<slug:division_slug>/<slug:assembly_slug>/attendings/", view=assembly_participation_student_list_view, name="children_ministry_participations_students"),

]
