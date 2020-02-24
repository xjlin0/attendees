from django.urls import path, include
from rest_framework import routers

from attendees.occasions.views import (
    children_ministry_participation_leader_list_view,
    children_ministry_participation_student_list_view,
    participation_viewset,
)


app_name = "occasions"

router = routers.DefaultRouter()
router.register('api/v1/participations', participation_viewset)

urlpatterns = [
    path('', include(router.urls)),
    path("<slug:division_slug>/participations/leaders/", view=children_ministry_participation_leader_list_view, name="children_ministry_participations_leaders"),
    path("<slug:division_slug>/participations/students/", view=children_ministry_participation_student_list_view, name="children_ministry_participations_students"),

]



#router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
# router.register(r'groups', views.GroupViewSet)
#
# # Wire up our API using automatic URL routing.
# # Additionally, we include login URLs for the browsable API.
# urlpatterns = [
#     path('', include(router.urls)),
#     path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
# ]
