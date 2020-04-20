from django.urls import path, include
from rest_framework import routers

from attendees.occasions.views import (
    assembly_attendance_list_view,
    user_attendance_list_view,
    coworkers_organization_attendance_list_view,
    api_user_attendance_viewset,
    api_user_character_viewset,
    api_user_gathering_viewset,
    api_attendance_viewset,
    api_character_viewset,
    api_team_viewset,
    api_gathering_viewset,
    api_organization_team_viewset,
    api_organization_gathering_viewset,
    api_organization_character_viewset,
    api_organization_attendance_viewset,
)


app_name = "occasions"

router = routers.DefaultRouter()
router.register('api/(?P<division_slug>.+)/(?P<assembly_slug>.+)/attendances', api_attendance_viewset, basename='attendance')
router.register('api/(?P<division_slug>.+)/(?P<assembly_slug>.+)/characters', api_character_viewset, basename='character')
router.register('api/(?P<division_slug>.+)/(?P<assembly_slug>.+)/teams', api_team_viewset, basename='team')
router.register('api/(?P<division_slug>.+)/(?P<assembly_slug>.+)/gatherings', api_gathering_viewset, basename='gathering')
router.register('api/(?P<division_slug>.+)/(?P<assembly_slug>.+)/gatherings', api_gathering_viewset, basename='gathering')
router.register('api/organization_teams', api_organization_team_viewset, basename='team')
router.register('api/organization_gatherings', api_organization_gathering_viewset, basename='gathering')
router.register('api/organization_characters', api_organization_character_viewset, basename='character')
router.register('api/organization_attendances', api_organization_attendance_viewset, basename='attendance')
router.register('api/user/attendances', api_user_attendance_viewset, basename='attendance')
router.register('api/user/characters', api_user_character_viewset, basename='character')
router.register('api/user/gatherings', api_user_gathering_viewset, basename='gathering')

urlpatterns = [
    path('', include(router.urls)),
    path("<slug:division_slug>/<slug:assembly_slug>/attendances/", view=assembly_attendance_list_view, name="assembly_attendances"),
    # path("<slug:division_slug>/<slug:assembly_slug>/attendings/", view=assembly_attendance_others_list_view, name="assembly_attendance_others"),
    path('coworkers/organization_attendances/', view=coworkers_organization_attendance_list_view, name='coworkers_organization_attendance'),
    path('user/attendances/', view=user_attendance_list_view, name='user-attendances'),

]
