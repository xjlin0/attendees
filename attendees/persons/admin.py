from django_summernote.admin import SummernoteModelAdmin
from django.contrib import admin
from attendees.occasions.models import *
from attendees.whereabouts.models import *
from .models import *

# Register your models here.

# class MeetAddressAdmin(admin.ModelAdmin):
#     list_display = ('meet', 'address', 'modified')



# class MeetAddressAdmin(admin.ModelAdmin):
#     list_display = ('Meet', 'address', 'modified')
#
#
# class MeetAddressInline(admin.TabularInline):
#     model = MeetAddress
#     extra = 0
#
#
# class AddressAdmin(admin.ModelAdmin):
#     inlines = (MeetAddressInline,)
#     list_display = ('address_type', 'street', 'city', 'zip_code', 'phone1', 'email1')


class AttendeeAddressInline(admin.StackedInline):
    model = AttendeeAddress
    extra = 0


# class DivisionAdmin(admin.ModelAdmin):
#     list_display = ('organization', 'name', 'key', 'modified')
#
#
class AttendingDivisionInline(admin.StackedInline):
    model = AttendingDivision
    extra = 0
#
#
# class MeetAdmin(admin.ModelAdmin):
#     inlines = (MeetAddressInline,)
#     list_display = ('name', 'get_addresses', 'modified')


class AttendeeAdmin(admin.ModelAdmin):
    search_fields = ('first_name', 'last_name', 'last_name2', 'first_name2')
    inlines = (AttendeeAddressInline,)
    list_display = ('first_name', 'last_name', 'last_name2', 'first_name2', 'modified')


# class PriceAdmin(admin.ModelAdmin):
#     list_display = ('price_label', 'price_type', 'start_date', 'price_value', 'modified')


class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('main_attendee', 'apply_type', 'apply_key', 'meet', 'modified')


# class ParticipationAdmin(admin.ModelAdmin):
#     # list_filter = ('session', 'attending', 'character', 'team')
#     list_display = ('brief_program_session', 'attending', 'character', 'team', 'modified')


class ParticipationInline(admin.StackedInline):
    model = Participation
    extra = 0


class AttendingAdmin(admin.ModelAdmin):
    search_fields = ('attendee__first_name', 'attendee__last_name', 'attendee__first_name2', 'attendee__first_name2')
    inlines = (AttendingDivisionInline, ParticipationInline,)
    list_display = ('registration', 'attendee', 'division_names', 'bed_needs', 'all_addresses')


# class CharacterAdmin(admin.ModelAdmin):
#     list_display = ('name', 'info', 'modified')
#
#
# class TeamAdmin(admin.ModelAdmin):
#     list_display = ('name', 'group', 'display_order', 'modified')


class NoteAdmin(SummernoteModelAdmin):
    summernote_fields = ('note_text',)
    list_display = ('note_text', 'content_type', 'object_id', 'content_object', 'modified')


# class PropertyAdmin(admin.ModelAdmin):
#     list_display = ('name', 'campus', 'modified')
#
#
# class CampusAdmin(admin.ModelAdmin):
#     list_display = ('name', 'address','modified')
#
#
# class SuiteAdmin(admin.ModelAdmin):
#     list_display = ('name', 'site', 'modified')
#
#
# class RoomAdmin(admin.ModelAdmin):
#     list_display = ('name', 'label', 'suite', 'modified')
#
#
# class OrganizationAdmin(admin.ModelAdmin):
#     list_display = ('name', 'modified')


class RelationshipAdmin(admin.ModelAdmin):
    list_display = ('from_attendee', 'to_attendee', 'relation', 'modified')


# class GroupAdmin(admin.ModelAdmin):
#     search_fields = ('name',)
#     list_display = ('name', 'info', 'url', 'modified')
#
#
## class ProgramProgressionAdmin(admin.ModelAdmin):
##     search_fields = ('name',)
##     list_display = ('name', 'display_order', 'modified')
#
#
# class SessionAdmin(admin.ModelAdmin):
#     inlines = (ParticipationInline,)
#     search_fields = ('group__name', 'name')
#     # list_filter = ('group')
#     list_display = ('group', 'start', 'name', 'location', 'modified')
#
#
##class ProgramGroupSettingAdmin(admin.ModelAdmin):
##     list_display = ('program_group', 'schedules', 'start_time', 'duration', 'location', 'modified')


admin.site.register(Note, NoteAdmin)
admin.site.register(Attendee, AttendeeAdmin)
# admin.site.register(MeetAddress, MeetAddressAdmin)
# admin.site.register(Address, AddressAdmin)
# admin.site.register(Meet, MeetAdmin)
# admin.site.register(Price, PriceAdmin)
admin.site.register(Registration, RegistrationAdmin)
admin.site.register(Attending, AttendingAdmin)
# admin.site.register(Character, CharacterAdmin)
# admin.site.register(Campus, CampusAdmin)
# admin.site.register(Property, PropertyAdmin)
# admin.site.register(Suite, SuiteAdmin)
# admin.site.register(Room, RoomAdmin)
# admin.site.register(Division, DivisionAdmin)
# admin.site.register(Organization, OrganizationAdmin)
admin.site.register(Relationship, RelationshipAdmin)
# admin.site.register(Group, GroupAdmin)
## admin.site.register(Progression, ProgressionAdmin)
# admin.site.register(Session, SessionAdmin)
# admin.site.register(Team, TeamAdmin)
# admin.site.register(Participation, ParticipationAdmin)
## admin.site.register(ProgramGroupSetting, ProgramGroupSettingAdmin)
