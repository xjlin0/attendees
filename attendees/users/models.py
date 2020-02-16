from django.contrib.auth.models import AbstractUser
from django.db.models import CharField
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):

    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = CharField(_("Name of User"), blank=True, max_length=255)
    default_route = CharField(max_length=50, null=False, blank=False, default='occasions:occasions.urls.some_view', help_text='default route upon successful login') #needs to make it ENUM later

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})

    def belongs_to_groups_of(self, auth_group_names): #.in_bulk() might take more memory
        return self.groups.filter(name__in=auth_group_names).exists()

    def attend_divisions_of(self, division_slugs):
        return self.attendee.attending_set.filter(divisions__slug__in=division_slugs).exists()

    def attended_divisions_slugs(self):
        return self.attendee.attending_set.values_list('division__slug')
