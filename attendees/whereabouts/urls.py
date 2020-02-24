from django.urls import path, include
from rest_framework import routers

from attendees.whereabouts.views import (
    api_division_viewset,
)

app_name = "whereabouts"

router = routers.DefaultRouter()
router.register('api/divisions', api_division_viewset)

urlpatterns = [
    path('', include(router.urls)),
]
