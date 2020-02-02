from django.contrib import admin
from attendees.occasions.models import *
from attendees.persons.models import *
from .models import *


class MeetAddressInline(admin.TabularInline):
    model = MeetAddress
    extra = 0


class AddressAdmin(admin.ModelAdmin):
    inlines = (MeetAddressInline,)
    list_display_links = ('street',)
    list_display = ('display_name', 'street', 'city', 'zip_code', 'phone1', 'email1')


class DivisionAdmin(admin.ModelAdmin):
    list_display_links = ('display_name',)
    list_display = ('organization', 'display_name', 'key', 'modified')


class PropertyAdmin(admin.ModelAdmin):
    list_display = ('display_name', 'key', 'campus', 'modified')


class CampusAdmin(admin.ModelAdmin):
    list_display = ('display_name', 'key', 'address', 'modified')


class SuiteAdmin(admin.ModelAdmin):
    list_display = ('display_name', 'key',  'site', 'modified')


class RoomAdmin(admin.ModelAdmin):
    list_display = ('display_name', 'label', 'suite', 'modified')


class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('display_name', 'key', 'modified')


admin.site.register(Address, AddressAdmin)
admin.site.register(Campus, CampusAdmin)
admin.site.register(Property, PropertyAdmin)
admin.site.register(Suite, SuiteAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(Division, DivisionAdmin)
admin.site.register(Organization, OrganizationAdmin)
