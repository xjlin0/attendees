import time
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.utils import timezone
from django.http import Http404
from django.shortcuts import render
from attendees.occasions.models import Meet, Character
from attendees.users.models import Menu

import logging


logger = logging.getLogger(__name__)


@method_decorator([login_required], name='dispatch')
class AssemblyAttendanceListView(UserPassesTestMixin, ListView):
    queryset = []
    template_name = 'occasions/division/assembly/attendances.html'

    def test_func(self):
        logger.info("hi jack 24 here is test_func")

        return Menu.objects.filter(
            auth_groups__in=self.request.user.groups.all(),
            url_name=self.request.resolver_match.url_name,
            menuauthgroup__read=True,
        ).exists()

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
        logger.info("hi jack 50 here is view name")
        logger.info(self.request.resolver_match.url_name)
        if self.request.user.belongs_to_organization_and_division(context['current_organization_slug'], context['current_division_slug']):
            if self.request.is_ajax():
                chosen_meet_slugs = self.request.GET.getlist('meets[]', [])
                chosen_character_slugs = self.request.GET.getlist('characters[]', [])
                chosen_start = self.request.GET.get('start', timezone.now())
                chosen_finish = self.request.GET.get('finish', timezone.now())
                partial_template = self.get_partial_template()
                filtered_attendances = self.get_attendances({'current_division_slug': context['current_division_slug'], 'chosen_start': chosen_start, 'chosen_finish': chosen_finish, 'chosen_meet_slugs': chosen_meet_slugs, 'chosen_character_slugs': chosen_character_slugs})
                return render(self.request, partial_template, {'filtered_attendances': filtered_attendances})
            else:
                context.update({'filtered_attendances': []})
                context.update({'teams_endpoint': f"/{context['current_organization_slug']}/occasions/api/{context['current_division_slug']}/{context['current_assembly_slug']}/teams/"})
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
    #
    # def get_partial_template(self):
    #     return ''


assembly_attendance_list_view = AssemblyAttendanceListView.as_view()
