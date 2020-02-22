from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import JsonResponse, Http404
from django.core import serializers
from django.shortcuts import render
from django.utils import timezone
from datetime import timedelta
import logging


from attendees.occasions.models import Participation

logger = logging.getLogger(__name__)


class ParticipationJSONResponseMixin:

    """
    A mixin that can be used to render a JSON response.
    https://docs.djangoproject.com/en/3.0/topics/class-based-views/mixins/#more-than-just-html
    """
    def render_to_json_response(self, context, **response_kwargs):
        """
        Returns a JSON response, transforming 'context' to make the payload.
        filter(attending__divisions__id__in=[3]) needs to be replaced with request.user.attended_divisions_slugs, and also need .filter(gathering__start__gte=timezone.now(),)
        """
        participations = Participation.objects.select_related('character', 'team', 'attending', 'gathering', 'attending__attendee').filter(attending__divisions__slug__in=['children_ministry']).exclude(character__slug='student').order_by('gathering__meet', '-gathering__start', 'character__display_order')
        # logger.info("29 The value of context is %s", context)
        # logger.info("30 The value of self.request.user is %s", self.request.user)
        # logger.info("31 The value of params is %s", path_params)
        # logger.info("32 The value of self.request.GET.get('hi') (search params) is %s", self.request.GET.get('hi'))
        # logger.info("33 The value of self.kwargs (url params) is %s", self.kwargs)
        return JsonResponse(
            serializers.serialize('json', participations),
            safe=False,
            **response_kwargs
        )


@method_decorator([login_required], name='dispatch')
class ChildrenMinistryParticipationLeaderListView(ListView, ParticipationJSONResponseMixin):
    queryset = []
    template_name = 'occasions/children_ministry/participations/leader_index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Todo include user divisions and meets slugs in context
        context.update({'var1': 'hello'})
        return context

    def render_to_response(self, context, **kwargs):
        # logger.info("53 The value of self.get_template_names()[0] is %s", self.get_template_names()[0])
        # logger.info("54 The value of self.kwargs is %s", self.kwargs)
        # logger.info("55 The value of kwargs is %s", kwargs)
        if True:
            if self.request.is_ajax():
                partial_template = 'occasions/children_ministry/participations/_grouped_list.html'
                filtered_participations = Participation.objects.select_related('character', 'team', 'attending', 'gathering','attending__attendee').filter(attending__divisions__slug__in=['children_ministry']).exclude(character__slug='student').order_by('gathering__meet', '-gathering__start', 'character__display_order')
                return render(self.request, partial_template, {'filtered_participations': filtered_participations})
            else:
                template_name = self.get_template_names()[0]
                return render(self.request, template_name, {'filtered_participations': []})
        else:
            raise Http404("Have you registered any events of the organization?")


children_ministry_participation_leader_list_view = ChildrenMinistryParticipationLeaderListView.as_view()

