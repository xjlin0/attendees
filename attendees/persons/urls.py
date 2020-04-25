from django.urls import path, include
from rest_framework import routers

from attendees.persons.views import (
    api_assembly_meet_attendings_viewset,
    api_assembly_meet_attendees_viewset,
    datagrid_assembly_all_attendings_list_view,
    api_user_meet_attendings_viewset,
    api_family_organization_attendings_viewset,
)

app_name = "persons"

router = routers.DefaultRouter()
router.register(
    'api/(?P<division_slug>.+)/(?P<assembly_slug>.+)/assembly_meet_attendings',
    api_assembly_meet_attendings_viewset,
    basename='attending',
)
router.register(
    'api/(?P<division_slug>.+)/(?P<assembly_slug>.+)/assembly_meet_attendees',
    api_assembly_meet_attendees_viewset,
    basename='attendee',
)
router.register(
    'api/user_meet_attendings',
    api_user_meet_attendings_viewset,
    basename='attending',
)
router.register(
    'api/family_organization_attendings',
    api_family_organization_attendings_viewset,
    basename='attending',
)

urlpatterns = [
    path('',
        include(router.urls)
    ),

    path(
        "<slug:division_slug>/<slug:assembly_slug>/datagrid_assembly_all_attendings/",
        view=datagrid_assembly_all_attendings_list_view,
        name="datagrid_assembly_all_attendings",
    ),
]
