from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.utils import timezone
from django.http import Http404
from django.shortcuts import render
from attendees.occasions.models import Meet, Participation


import logging


logger = logging.getLogger(__name__)


@method_decorator([login_required], name='dispatch')
class AssemblyParticipationListView(ListView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Todo include user divisions and meets slugs in context
        current_division_slug = self.kwargs.get('division_slug', None)
        current_organization_slug = self.kwargs.get('organization_slug', None)
        available_meets = Meet.objects.filter(assembly__division__slug=current_division_slug).in_bulk(field_name='slug')
        # available_characters = Participation.objects.filter(attending__divisions__slug=current_division_slug).order_by('character__display_order').values_list('character__slug', flat=True).distinct()
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
                partial_template = self.get_partial_template()
                filtered_participations = self.get_participations({'current_division_slug': context['current_division_slug'], 'chosen_start': chosen_start, 'chosen_finish': chosen_finish, 'chosen_meet_slugs': chosen_meet_slugs})
                return render(self.request, partial_template, {'filtered_participations': filtered_participations})
            else:
                context.update({'filtered_participations': []})
                context.update({'teams_endpoint': f"/{context['current_organization_slug']}/occasions/api/teams/"})
                context.update({'gatherings_endpoint': f"/{context['current_organization_slug']}/occasions/api/gatherings/"})
                context.update({'characters_endpoint': f"/{context['current_organization_slug']}/occasions/api/characters/"})
                context.update({'participations_endpoint': f"/{context['current_organization_slug']}/occasions/api/{context['current_division_slug']}/participations/"})
                return render(self.request, self.get_template_names()[0], context)
        else:
            raise Http404('Have you registered any events of the organization?')

    def get_participations(self, args):
        return []

    def get_partial_template(self):
        return ''
