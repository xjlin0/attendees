from django.urls import path, include
from rest_framework import routers

from attendees.persons.views import (
    api_attending_viewset,
)

app_name = "persons"

router = routers.DefaultRouter()
router.register('api/(?P<division_slug>.+)/(?P<assembly_slug>.+)/attendings', api_attending_viewset, basename='participation')

urlpatterns = [
    path('', include(router.urls)),
]
