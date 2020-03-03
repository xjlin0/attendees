from django.urls import path, include
from rest_framework import routers

from attendees.occasions.views import (
    assembly_participation_leader_list_view,
    assembly_participation_student_list_view,
    api_participation_viewset,
    api_character_viewset,
    api_team_viewset,
    api_gathering_viewset,
)


app_name = "occasions"
#'api/<slug:division_slug>/<slug:assembly_slug>/participations'
router = routers.DefaultRouter()
router.register('api/participations', api_participation_viewset)
router.register('api/characters', api_character_viewset)
router.register('api/teams', api_team_viewset)
router.register('api/gatherings', api_gathering_viewset)

urlpatterns = [
    path('', include(router.urls)),
    path("<slug:division_slug>/<slug:assembly_slug>/participations/leaders/", view=assembly_participation_leader_list_view, name="children_ministry_participations_leaders"),
    path("<slug:division_slug>/<slug:assembly_slug>/participations/students/", view=assembly_participation_student_list_view, name="children_ministry_participations_students"),

]
