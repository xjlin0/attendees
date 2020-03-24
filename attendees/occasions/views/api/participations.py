from rest_framework import viewsets
from attendees.occasions.models import Participation
from attendees.occasions.serializers import ParticipationSerializer
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponseNotAllowed
from urllib import parse
import logging


logger = logging.getLogger(__name__)


@method_decorator([login_required], name='dispatch')
class ApiParticipationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Participations to be viewed or edited.
    """
    serializer_class = ParticipationSerializer

    def get_queryset(self):
        if self.request.user.belongs_to_organization_and_division(self.kwargs['organization_slug'], self.kwargs['division_slug']):

            meets = self.request.query_params.getlist('meets', [])
            start = self.request.query_params.get('start', None)
            finish = self.request.query_params.get('finish', None)
            return Participation.objects.select_related(
                'character', 'team', 'attending', 'gathering',
                                                        'attending__attendee').filter(
                attending__divisions__slug=self.kwargs['division_slug'], gathering__meet__slug__in=meets,
                gathering__start__gte=start, gathering__finish__lte=finish).exclude(
                character__slug='student').order_by('gathering__meet', '-gathering__start', 'character__display_order')

        else:
            raise HttpResponseNotAllowed('Have you registered any events of the organization?')


    # def get_queryset(self):
    #     """
    #     Optionally restricts the returned participations to chosen meets,
    #     by filtering against a start/finish/meet query parameter in the URL.
    #     """
    #     queryset = Purchase.objects.all()
    #     username = self.request.query_params.get('username', None)
    #     if username is not None:
    #         queryset = queryset.filter(purchaser__username=username)
    #     return queryset

api_participation_viewset = ApiParticipationViewSet
