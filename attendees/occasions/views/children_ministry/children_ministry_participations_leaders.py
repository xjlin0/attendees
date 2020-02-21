from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import JsonResponse
from django.core import serializers
from django.utils import timezone
from django.shortcuts import get_object_or_404
from datetime import timedelta
import logging


from attendees.occasions.models import Participation

logger = logging.getLogger(__name__)
class ParticipationJSONResponseMixin:

    """
    A mixin that can be used to render a JSON response.
    https://docs.djangoproject.com/en/3.0/topics/class-based-views/mixins/#more-than-just-html
    """
    def render_to_json_response(self, context, params, **response_kwargs):
        """
        Returns a JSON response, transforming 'context' to make the payload.
        filter(attending__divisions__id__in=[3]) needs to be replaced with request.user.attended_divisions_slugs, and also need .filter(gathering__start__gte=timezone.now(),)
        """
        participations = Participation.objects.select_related('character', 'team', 'attending', 'gathering', 'attending__attendee').filter(attending__divisions__slug__in=['children_ministry']).exclude(character__slug='student').order_by('gathering__meet', '-gathering__start', 'character__display_order')
        logger.info("27 The value of context is %s", context)
        logger.info("28 The value of response_kwargs is %s", response_kwargs)
        logger.info("29 The value of params is %s", params)
        # logger.info("29 The value of request.GET('hi') is %s", 5)
        return JsonResponse(
            serializers.serialize('json', participations),
            safe=False,
            **response_kwargs
        )


@method_decorator([login_required], name='dispatch')
class ChildrenMinistryParticipationLeaderListView(ListView, ParticipationJSONResponseMixin):
    queryset = []
    template_name = 'occasions/children_ministry/participations/leader_index.html'

    def render_to_response(self, context, **kwargs):
        logger.info("44 The value of kwargs is %s", kwargs)
        logger.info("45 The value of self.request is %s", self.request)
        logger.info("46 The value of self.kwargs is %s", self.kwargs)
        if self.request.is_ajax():
            return self.render_to_json_response(context, params=self.kwargs, **kwargs)
        else:
            return super().render_to_response(context, **kwargs)


children_ministry_participation_leader_list_view = ChildrenMinistryParticipationLeaderListView.as_view()

