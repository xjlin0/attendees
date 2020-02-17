from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from attendees.occasions.models import Participation


@method_decorator([login_required], name='dispatch')
class ParticipationListView(ListView):
    model = Participation
    template_name = 'occasions/participations/index.html'
    paginate_by = 500

participation_list_view = ParticipationListView.as_view()

