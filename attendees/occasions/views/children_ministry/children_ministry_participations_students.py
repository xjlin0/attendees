from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from attendees.occasions.models import Participation


@method_decorator([login_required], name='dispatch')
class ChildrenMinistryParticipationStudentListView(ListView): #.filter(attending__divisions__id__in=[3]) needs to be replaced with request.user.attended_divisions_slugs, and also need .filter(gathering__start__gte=timezone.now(),)
    queryset = Participation.objects.select_related('character', 'team', 'attending', 'gathering', 'attending__attendee').filter(attending__divisions__slug__in=['children_ministry'], character__slug='student').order_by('gathering__meet', '-gathering__start', 'character__display_order')
    template_name = 'occasions/children_ministry/participations/student_index.html'
    paginate_by = 500


children_ministry_participation_student_list_view = ChildrenMinistryParticipationStudentListView.as_view()

