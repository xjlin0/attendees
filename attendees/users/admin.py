from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model
from mptt.admin import MPTTModelAdmin
from .models import Menu, MenuAuthGroup

from attendees.users.forms import UserChangeForm, UserCreationForm

User = get_user_model()


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):

    form = UserChangeForm
    add_form = UserCreationForm
    fieldsets = (("User", {"fields": ("name", "organization",)}),) + auth_admin.UserAdmin.fieldsets
    list_display = ["username", "organization", "is_staff", "is_superuser"]
    search_fields = ["name"]


class MenuAdmin(admin.ModelAdmin):
    mptt_level_indent = 50
    list_display = ('organization', 'category',  'display_name', 'urn', 'display_order')



admin.site.register(Menu, MPTTModelAdmin)
