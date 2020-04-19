import time

from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# from django.utils import timezone
from django.http import Http404
from django.shortcuts import render
from attendees.occasions.models import Meet, Character
from attendees.users.authorization import RouteGuard
import logging


logger = logging.getLogger(__name__)


@method_decorator([login_required], name='dispatch')
class PageAttendingListView(RouteGuard, ListView):
    queryset = []
    template_name = 'persons/division/assembly/attendings.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Todo include user divisions and meets slugs in context
        current_division_slug = self.kwargs.get('division_slug', None)
        current_organization_slug = self.kwargs.get('organization_slug', None)
        current_assembly_slug = self.kwargs.get('assembly_slug', None)
        available_meets = Meet.objects.filter(assembly__slug=current_assembly_slug).order_by('display_name')
        available_characters = Character.objects.filter(assembly__slug=current_assembly_slug).order_by('display_order')
        context.update({
            'current_organization_slug': current_organization_slug,
            'current_division_slug': current_division_slug,
            'current_assembly_slug': current_assembly_slug,
            'available_meets': available_meets,
            'available_characters': available_characters,
        })
        return context

    def render_to_response(self, context, **kwargs):
        if self.request.user.belongs_to_organization_and_division(context['current_organization_slug'], context['current_division_slug']):
            if self.request.is_ajax():
                pass

            else:
                # chosen_character_slugs = self.request.GET.getlist('characters', [])
                # context.update({'chosen_character_slugs': chosen_character_slugs})
                context.update({'teams_endpoint': f"/{context['current_organization_slug']}/occasions/api/{context['current_division_slug']}/{context['current_assembly_slug']}/teams/"})
                context.update({'attendees_endpoint': f"/{context['current_organization_slug']}/persons/api/{context['current_division_slug']}/{context['current_assembly_slug']}/attendees/"})
                context.update({'gatherings_endpoint': f"/{context['current_organization_slug']}/occasions/api/{context['current_division_slug']}/{context['current_assembly_slug']}/gatherings/"})
                context.update({'characters_endpoint': f"/{context['current_organization_slug']}/occasions/api/{context['current_division_slug']}/{context['current_assembly_slug']}/characters/"})
                context.update({'attendings_endpoint': f"/{context['current_organization_slug']}/persons/api/{context['current_division_slug']}/{context['current_assembly_slug']}/attendings/"})
                context.update({'attendances_endpoint': f"/{context['current_organization_slug']}/occasions/api/{context['current_division_slug']}/{context['current_assembly_slug']}/attendances/"})
                return render(self.request, self.get_template_names()[0], context)
        else:
            time.sleep(2)
            raise Http404('Have you registered any events of the organization?')

    # def get_attendances(self, args):
    #     return []

    # def get_partial_template(self):
    #     return ''


assembly_attending_list_view = PageAttendingListView.as_view()
