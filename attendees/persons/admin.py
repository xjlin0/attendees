from django_summernote.admin import SummernoteModelAdmin
from django.contrib import admin
from attendees.occasions.models import *
from attendees.whereabouts.models import *
from .models import *

# Register your models here.

class AttendeeAddressInline(admin.StackedInline):
    model = AttendeeAddress
    extra = 0


class AttendingDivisionInline(admin.StackedInline):
    model = AttendingDivision
    extra = 0


class RelationshipInline(admin.TabularInline):
    model = Relationship
    fk_name = 'from_attendee'
    extra = 0


class AttendeeAdmin(admin.ModelAdmin):
    search_fields = ('first_name', 'last_name', 'last_name2', 'first_name2')
    inlines = (AttendeeAddressInline, RelationshipInline)
    list_display_links = ('last_name',)
    list_display = ('first_name', 'last_name', 'last_name2', 'first_name2', 'modified')


class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('main_attendee', 'apply_type', 'apply_key', 'assembly', 'modified')


class ParticipationInline(admin.StackedInline):
    model = Participation
    extra = 0


class AttendingAdmin(admin.ModelAdmin):
    search_fields = ('attendee__first_name', 'attendee__last_name', 'attendee__first_name2', 'attendee__last_name2')
    inlines = (AttendingDivisionInline, ParticipationInline,)
    list_display = ('registration', 'attendee', 'division_names', 'bed_needs', 'all_addresses')


class NoteAdmin(SummernoteModelAdmin):
    summernote_fields = ('note_text',)
    list_display = ('note_text', 'content_type', 'object_id', 'content_object', 'modified')


class RelationshipAdmin(admin.ModelAdmin):
    list_display_links = ('relation',)
    list_display = ('from_attendee', 'to_attendee', 'relation', 'category', 'modified')


admin.site.register(Note, NoteAdmin)
admin.site.register(Attendee, AttendeeAdmin)
admin.site.register(Registration, RegistrationAdmin)
admin.site.register(Attending, AttendingAdmin)
admin.site.register(Relationship, RelationshipAdmin)
