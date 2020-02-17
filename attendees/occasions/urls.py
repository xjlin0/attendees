from django.urls import path

from attendees.occasions.views import (
    participation_list_view,
)


app_name = "occasions"
urlpatterns = [
    path("participations/", view=participation_list_view, name="participations"),
]
