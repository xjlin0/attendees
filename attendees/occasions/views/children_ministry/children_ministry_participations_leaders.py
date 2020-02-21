from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import JsonResponse
from django.core import serializers
from django.utils import timezone
from django.shortcuts import get_object_or_404
from datetime import timedelta

from attendees.occasions.models import Participation


class JSONResponseMixin:
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

        return JsonResponse(
            serializers.serialize('json', participations),
            safe=False,
            **response_kwargs
        )


@method_decorator([login_required], name='dispatch')
class ChildrenMinistryParticipationLeaderListView(ListView, JSONResponseMixin):
    queryset = []
    template_name = 'occasions/children_ministry/participations/leader_index.html'

    def render_to_response(self, context, **kwargs):
        # Look for a 'format=json' GET argument
        if self.request.is_ajax():
            return self.render_to_json_response(context, **kwargs)
        else:
            return super().render_to_response(context, **kwargs)


children_ministry_participation_leader_list_view = ChildrenMinistryParticipationLeaderListView.as_view()

