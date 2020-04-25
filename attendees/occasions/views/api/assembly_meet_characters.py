import time

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from rest_framework import viewsets
from rest_framework.exceptions import AuthenticationFailed

from attendees.occasions.models import Character
from attendees.occasions.serializers import CharacterSerializer


@method_decorator([login_required], name='dispatch')
class ApiAssemblyMeetCharactersViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Character to be viewed or edited.
    """
    serializer_class = CharacterSerializer

    def get_queryset(self):
        if self.request.user.belongs_to_organization_and_division(self.kwargs['organization_slug'], self.kwargs['division_slug']):
            # Todo: probably need to check if the assembly belongs to the division?
            meets = self.request.query_params.getlist('meets[]', [])
            return Character.objects.filter(
                assembly__slug=self.kwargs['assembly_slug'],
                assembly__meet__slug__in=meets,
            ).order_by(
                'display_order',
            ).distinct()

        else:
            time.sleep(2)
            raise AuthenticationFailed(detail='Have you registered any events of the organization?')


api_assembly_meet_characters_viewset = ApiAssemblyMeetCharactersViewSet
