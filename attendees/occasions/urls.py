from django.urls import path, include
from rest_framework import routers

from attendees.occasions.views import (
    children_ministry_participation_leader_list_view,
    children_ministry_participation_student_list_view,
    api_participation_viewset,
    api_character_viewset,
)


app_name = "occasions"

router = routers.DefaultRouter()
router.register('api/participations', api_participation_viewset)
router.register('api/characters', api_character_viewset)

urlpatterns = [
    path('', include(router.urls)),
    path("<slug:division_slug>/participations/leaders/", view=children_ministry_participation_leader_list_view, name="children_ministry_participations_leaders"),
    path("<slug:division_slug>/participations/students/", view=children_ministry_participation_student_list_view, name="children_ministry_participations_students"),

]
