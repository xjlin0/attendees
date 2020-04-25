from allauth.account.forms import SignupForm
from attendees.whereabouts.models import Organization
import logging


logger = logging.getLogger(__name__)


class MyCustomSignupForm(SignupForm):

    def save(self, request):
        user_hostname = request.META['HTTP_HOST']
        user = super(MyCustomSignupForm, self).save(request)
        user.organization = Organization.objects.get(hostname=user_hostname)
        user.save()
        return user
