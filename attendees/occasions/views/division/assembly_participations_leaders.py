from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .assembly_participations import AssemblyParticipationListView

import logging


from attendees.occasions.models import Participation

logger = logging.getLogger(__name__)


@method_decorator([login_required], name='dispatch')
class AssemblyParticipationLeaderListView(AssemblyParticipationListView):
    queryset = []
    template_name = 'occasions/division/assembly/participations_leader_index.html'

    def get_participations(self, args):
        current_division_slug = args.get('current_division_slug')
        chosen_start = args.get('chosen_start')
        chosen_finish = args.get('chosen_finish')
        chosen_meet_slugs = args.get('chosen_meet_slugs')
        return [] #Participation.objects.select_related('character', 'team', 'attending', 'gathering', 'attending__attendee')#.filter(attending__divisions__slug=current_division_slug, gathering__meet__slug__in=chosen_meet_slugs, gathering__start__gte=chosen_start, gathering__finish__lte=chosen_finish).exclude(character__slug='student').order_by('gathering__meet', '-gathering__start', 'character__display_order')

    def get_partial_template(self):
        return 'occasions/division/assembly/_participations_grouped_list.html'


assembly_participation_leader_list_view = AssemblyParticipationLeaderListView.as_view()

