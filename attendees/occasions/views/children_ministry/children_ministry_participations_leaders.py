from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponse
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
        """
        participations = Participation.objects.select_related('character', 'team', 'attending', 'gathering', 'attending__attendee').filter(attending__divisions__slug__in=['children_ministry']).exclude(character__slug='student').order_by('gathering__meet', '-gathering__start', 'character__display_order')

        return JsonResponse(
            serializers.serialize('json', participations), safe=False,
            **response_kwargs
        )


@method_decorator([login_required], name='dispatch')
class ChildrenMinistryParticipationLeaderListView(ListView, JSONResponseMixin): #.filter(attending__divisions__id__in=[3]) needs to be replaced with request.user.attended_divisions_slugs, and also need .filter(gathering__start__gte=timezone.now(),)
    # queryset = Participation.objects.select_related('character', 'team', 'attending', 'gathering', 'attending__attendee').filter(attending__divisions__slug__in=['children_ministry']).exclude(character__slug='student').order_by('gathering__meet', '-gathering__start', 'character__display_order') #use .prefetch_related()for M2M
    # model = Participation
    template_name = 'occasions/children_ministry/participations/leader_index.html'
    paginate_by = 500

    def get_queryset(self):
        # sss= self.ajax_list_partial #https://dkoug.com/post/django-ajax-class-based-views/
        meet_slug = self.kwargs.get('meet_slug', None)
        assembly_slug = self.kwargs.get('assembly_slug', None)
        user_organization = self.request.user.organization or None
        url_division_slug = self.kwargs.get('division_slug', None)
        if user_organization and url_division_slug and meet_slug and assembly_slug:
            user_division_slugs = user_organization.division_set.values_list('slug', flat=True)
            # check if passed in url_division_slug belongs user's organization's divisions
            # then filter Participations baed on division/meet/assembly slugs
            # how to return json?
            return Participation.objects.select_related('character', 'team', 'attending', 'gathering', 'attending__attendee').filter(attending__divisions__slug__in=['children_ministry']).exclude(character__slug='student').order_by('gathering__meet', '-gathering__start', 'character__display_order')
        else: # no url params, prepared empty table for ajax, probably TemplateResponseMixin or JSONResponseMixin?
            return []

    def render_to_response(self, context):
        # Look for a 'format=json' GET argument
        if self.request.is_ajax():
            return self.render_to_json_response(context)
        else:
            return super().render_to_response(context)


children_ministry_participation_leader_list_view = ChildrenMinistryParticipationLeaderListView.as_view()

