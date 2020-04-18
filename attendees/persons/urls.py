from django.urls import path, include
from rest_framework import routers

from attendees.persons.views import (
    api_attending_viewset,
    api_attendee_viewset,
    assembly_attending_list_view,
    api_organization_attending_viewset,
)

app_name = "persons"

router = routers.DefaultRouter()
router.register(
    'api/(?P<division_slug>.+)/(?P<assembly_slug>.+)/attendings',
    api_attending_viewset,
    basename='attending',
)
router.register(
    'api/(?P<division_slug>.+)/(?P<assembly_slug>.+)/attendees',
    api_attendee_viewset,
    basename='attendee',
)
router.register(
    'api/organization_attendings',
    api_organization_attending_viewset,
    basename='attending',
)

urlpatterns = [
    path('',
        include(router.urls)
    ),

    path(
        "<slug:division_slug>/<slug:assembly_slug>/attendings/",
        view=assembly_attending_list_view,
        name="assembly-attendings",
    ),
]
