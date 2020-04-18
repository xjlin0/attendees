import time
from django.contrib.auth.mixins import UserPassesTestMixin
from attendees.users.models import Menu


class RouteGuard(UserPassesTestMixin):

    def test_func(self):
        whether_user_allowed_to_read_the_page = Menu.objects.filter(
            auth_groups__in=self.request.user.groups.all(),
            url_name=self.request.resolver_match.url_name,
            menuauthgroup__read=True,
        ).exists()
        if not whether_user_allowed_to_read_the_page:
            time.sleep(2)

        return whether_user_allowed_to_read_the_page
