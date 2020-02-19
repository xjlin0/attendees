from django.urls import path

from attendees.occasions.views import (
    children_ministry_participation_leader_list_view,
    children_ministry_participation_student_list_view,
)


app_name = "occasions"
urlpatterns = [
    path("<slug:division_slug>/participations/leaders/", view=children_ministry_participation_leader_list_view, name="children_ministry_participations_leaders"),
    path("<slug:division_slug>/participations/students/", view=children_ministry_participation_student_list_view, name="children_ministry_participations_students"),

]
