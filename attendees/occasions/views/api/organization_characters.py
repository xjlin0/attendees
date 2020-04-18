import time

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from rest_framework import viewsets
from rest_framework.exceptions import AuthenticationFailed

from attendees.occasions.models import Character
from attendees.occasions.serializers import CharacterSerializer


@method_decorator([login_required], name='dispatch')
class ApiOrganizationCharacterViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Character to be viewed or edited.
    """
    serializer_class = CharacterSerializer

    def get_queryset(self):
        current_user = self.request.user
        if current_user.belongs_to_organization_of(self.kwargs['organization_slug']):
            assembly__slugs = current_user.attendee.attendings.values_list('gathering__meet__assembly__slug', flat=True)
            return Character.objects.filter(
                assembly__division__organization__slug=self.kwargs['organization_slug'],
                assembly__slug__in=assembly__slugs,
            ).order_by(
                'display_order',
            )

        else:
            time.sleep(2)
            raise AuthenticationFailed(detail='Have you registered any events of the organization?')


api_organization_character_viewset = ApiOrganizationCharacterViewSet