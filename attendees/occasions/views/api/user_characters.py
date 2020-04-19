import time

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from rest_framework import viewsets
from django.db.models import Q
from rest_framework.exceptions import AuthenticationFailed
from attendees.persons.models import Attendee
from attendees.occasions.models import Character
from attendees.occasions.serializers import CharacterSerializer


@method_decorator([login_required], name='dispatch')
class ApiUserCharacterViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Character to be viewed or edited.
    """
    serializer_class = CharacterSerializer

    def get_queryset(self):
        current_user = self.request.user
        if current_user.belongs_to_organization_of(self.kwargs['organization_slug']):
            # user_assembly_slugs = current_user.attendee.attendings.values_list('gathering__meet__assembly__slug', flat=True)
            # care_receiver_assembly_slugs = current_user.attendee.relations.filter(to_attendee__relation__in=Attendee.BE_LISTED_KEYWORDS).values_list('attendings__gathering__meet__assembly__slug', flat=True)
            return Character.objects.filter(
                Q(assembly__slug__in=current_user.attendee.attendings.values_list('gathering__meet__assembly__slug', flat=True))
                |
                Q(assembly__slug__in=current_user.attendee.relations.filter(to_attendee__relation__in=Attendee.BE_LISTED_KEYWORDS).values_list('attendings__gathering__meet__assembly__slug', flat=True)),
                assembly__division__organization__slug=self.kwargs['organization_slug'],
                ).order_by(
                    'display_order',
            )

        else:
            time.sleep(2)
            raise AuthenticationFailed(detail='Have you registered any events of the organization?')


api_user_character_viewset = ApiUserCharacterViewSet
