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


class MenuAuthGroupInline(admin.TabularInline):
    model = MenuAuthGroup
    extra = 0


@admin.register(Menu)
class MenuAdmin(MPTTModelAdmin):

    mptt_level_indent = 20
    list_display = ('display_name', 'organization_slug', 'category', 'urn', 'display_order')
    inlines = (MenuAuthGroupInline,)
    list_display_links=('display_name',)


@admin.register(MenuAuthGroup)
class MenuAuthGroupAdmin(admin.ModelAdmin):

    list_display = ('auth_group', 'read', 'write', 'menu',)
