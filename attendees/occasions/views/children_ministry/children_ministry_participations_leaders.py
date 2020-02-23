from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import Http404
from django.shortcuts import render
from attendees.occasions.models import Meet
from django.utils import timezone

import logging


from attendees.occasions.models import Participation

logger = logging.getLogger(__name__)


@method_decorator([login_required], name='dispatch')
class ChildrenMinistryParticipationLeaderListView(ListView):
    queryset = []
    template_name = 'occasions/children_ministry/participations/leader_index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Todo include user divisions and meets slugs in context
        current_division_slug = self.kwargs.get('division_slug', None)
        current_organization_slug = self.kwargs.get('organization_slug', None)
        available_meets = Meet.objects.filter(division__slug=current_division_slug).in_bulk(field_name='slug')
        context.update({
            'current_organization_slug': current_organization_slug,
            'current_division_slug': current_division_slug,
            'available_meets': available_meets,
        })
        return context

    def render_to_response(self, context, **kwargs):
        if self.request.user.belongs_to_organization_and_division(context['current_organization_slug'], context['current_division_slug']):
            if self.request.is_ajax():
                chosen_meet_slugs = self.request.GET.getlist('meets[]', [])
                chosen_start = self.request.GET.get('start', timezone.now())
                chosen_finish = self.request.GET.get('finish', timezone.now())
                partial_template = 'occasions/children_ministry/participations/_grouped_list.html'
                filtered_participations = Participation.objects.select_related('character', 'team', 'attending', 'gathering','attending__attendee').filter(attending__divisions__slug=context['current_division_slug'], gathering__meet__slug__in=chosen_meet_slugs, gathering__start__gte=chosen_start, gathering__finish__lte=chosen_finish).exclude(character__slug='student').order_by('gathering__meet', '-gathering__start', 'character__display_order')
                return render(self.request, partial_template, {'filtered_participations': filtered_participations})
            else:
                context.update({'filtered_participations': []})
                return render(self.request, self.get_template_names()[0], context)
        else:
            raise Http404('Have you registered any events of the organization?')


children_ministry_participation_leader_list_view = ChildrenMinistryParticipationLeaderListView.as_view()

