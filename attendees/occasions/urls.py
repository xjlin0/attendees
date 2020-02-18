from django.urls import path

from attendees.occasions.views import (
    participation_leader_list_view,
    participation_student_list_view,
)


app_name = "occasions"
urlpatterns = [
    path("participations/leaders/", view=participation_leader_list_view, name="participations_leaders"),
    path("participations/students/", view=participation_student_list_view, name="participations_students"),

]
