from datetime import timedelta
from django.utils import timezone
import pytz

import time
from django.db.models import Q
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import Http404
from django.shortcuts import render
from attendees.occasions.models import Meet
from attendees.persons.models import Attendee

import logging


logger = logging.getLogger(__name__)


@method_decorator([login_required], name='dispatch')
class UserAttendanceListView(ListView):
    queryset = []
    template_name = 'occasions/user/attendances.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_organization_slug = self.kwargs.get('organization_slug', None)
        available_meets = Meet.objects.filter(
            Q(attendings__attendee=self.request.user.attendee)
            |
            Q(attendings__attendee__in=self.request.user.attendee.relations.filter(
                to_attendee__relation__in=Attendee.BE_LISTED_KEYWORDS,
            ))
        ).order_by(
            'display_name',
        )  # get all user's and user care receivers' joined meets, no time limit on the first load
        context.update({
            'current_organization_slug': current_organization_slug,
            'available_meets': available_meets,
        })
        return context

    def render_to_response(self, context, **kwargs):
        if self.request.user.belongs_to_organization_of(context['current_organization_slug']):
            if self.request.is_ajax():
                pass

            else:
                # chosen_character_slugs = self.request.GET.getlist('characters', [])
                # context.update({'chosen_character_slugs': chosen_character_slugs})
                context.update({'teams_endpoint': f"/{context['current_organization_slug']}/occasions/api/organization_teams/"})
                # context.update({'attendees_endpoint': f"/{context['current_organization_slug']}/persons/api/user_attendees/"})
                context.update({'gatherings_endpoint': f"/{context['current_organization_slug']}/occasions/api/user/gatherings/"})
                context.update({'characters_endpoint': f"/{context['current_organization_slug']}/occasions/api/user/characters/"})
                context.update({'attendings_endpoint': f"/{context['current_organization_slug']}/persons/api/user_attendings/"})
                context.update({'attendances_endpoint': f"/{context['current_organization_slug']}/occasions/api/user/attendances/"})
                return render(self.request, self.get_template_names()[0], context)
        else:
            time.sleep(2)
            raise Http404('Have you registered any events of the organization?')
#
#     # def get_attendances(self, args):
#     #     return []
#
#     # def get_partial_template(self):
#     #     return ''
#
#
user_attendance_list_view = UserAttendanceListView.as_view()
