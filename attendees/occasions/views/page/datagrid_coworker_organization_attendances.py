from datetime import timedelta
from django.utils import timezone
import pytz

import time
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import Http404
from django.shortcuts import render
from attendees.occasions.models import Meet
from attendees.users.authorization import RouteGuard
import logging


logger = logging.getLogger(__name__)


@method_decorator([login_required], name='dispatch')
class DatagridCoworkerOrganizationAttendancesListView(RouteGuard, ListView):
    queryset = []
    template_name = 'occasions/datagrid_coworker_organization_attendances.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # current_organization_slug = self.kwargs.get('organization_slug', None)
        available_meets = Meet.objects.filter(assembly__division__organization__slug=self.request.user.organization.slug).order_by('display_name')
        context.update({
            'current_organization_slug': self.request.user.organization.slug,
            'available_meets': available_meets,
        })
        return context

    def render_to_response(self, context, **kwargs):
        if self.request.user.organization:
            if self.request.is_ajax():
                pass

            else:
                # chosen_character_slugs = self.request.GET.getlist('characters', [])
                # context.update({'chosen_character_slugs': chosen_character_slugs})
                context.update({'teams_endpoint': f"/occasions/api/organization_meet_teams/"})
                # context.update({'attendees_endpoint': f"/persons/api/organization_attendees/"})
                context.update({'gatherings_endpoint': f"/occasions/api/organization_team_gatherings/"})
                context.update({'characters_endpoint': f"/occasions/api/user_assembly_characters/"})
                context.update({'attendings_endpoint': f"/persons/api/user_meet_attendings/"})
                context.update({'attendances_endpoint': f"/occasions/api/coworker_organization_attendances/"})
                return render(self.request, self.get_template_names()[0], context)
        else:
            time.sleep(2)
            raise Http404('Have you registered any events of the organization?')


datagrid_coworker_organization_attendances_list_view = DatagridCoworkerOrganizationAttendancesListView.as_view()
