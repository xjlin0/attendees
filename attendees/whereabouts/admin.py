from django.contrib import admin
from attendees.occasions.models import *
from attendees.persons.models import *
from .models import *


class AssemblyAddressInline(admin.TabularInline):
    model = AssemblyAddress
    extra = 0


class AddressAdmin(admin.ModelAdmin):
    inlines = (AssemblyAddressInline,)
    list_display_links = ('street',)
    list_display = ('display_name', 'street', 'city', 'zip_code', 'phone1', 'email1')


class DivisionAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("display_name",)}
    list_display_links = ('display_name',)
    list_display = ('organization', 'display_name', 'slug', 'modified')


class PropertyAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("display_name",)}
    list_display = ('display_name', 'slug', 'campus', 'modified')


class CampusAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("display_name",)}
    list_display = ('display_name', 'slug', 'address', 'modified')


class SuiteAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("display_name",)}
    list_display = ('display_name', 'slug',  'site', 'modified')


class RoomAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("display_name",)}
    list_display = ('display_name', 'label', 'suite', 'modified')


class OrganizationAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("display_name",)}
    list_display = ('display_name', 'slug', 'modified')


admin.site.register(Address, AddressAdmin)
admin.site.register(Campus, CampusAdmin)
admin.site.register(Property, PropertyAdmin)
admin.site.register(Suite, SuiteAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(Division, DivisionAdmin)
admin.site.register(Organization, OrganizationAdmin)
