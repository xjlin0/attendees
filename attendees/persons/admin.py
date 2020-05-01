from django_summernote.admin import SummernoteModelAdmin
from django.contrib import admin
from attendees.occasions.models import *
from attendees.whereabouts.models import *
from .models import *

# Register your models here.


class AttendeeAddressInline(admin.StackedInline):
    model = AttendeeAddress
    extra = 0


class AttendingMeetInline(admin.StackedInline):
    model = AttendingMeet
    extra = 0


class RelationshipInline(admin.TabularInline):
    model = Relationship
    fk_name = 'from_attendee'
    extra = 0


class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ['id', 'created', 'modified']
    prepopulated_fields = {"slug": ("display_name",)}
    list_display = ('id', 'display_name', 'slug', 'display_order', 'description', 'modified')


class RelationAdmin(admin.ModelAdmin):
    readonly_fields = ['id', 'created', 'modified']
    list_display = ('id', 'title', 'reciprocal_ids', 'emergency_contact', 'scheduler', 'relative', 'display_order')


class AttendeeAdmin(admin.ModelAdmin):
    search_fields = ('first_name', 'last_name', 'last_name2', 'first_name2')
    readonly_fields = ['id', 'created', 'modified']
    inlines = (AttendeeAddressInline, RelationshipInline)
    list_display_links = ('last_name',)
    list_display = ('id', 'first_name', 'last_name', 'last_name2', 'first_name2', 'modified')


class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('id', 'main_attendee', 'apply_type', 'apply_key', 'assembly', 'modified')


class AttendanceInline(admin.StackedInline):
    model = Attendance
    extra = 0


class AttendingAdmin(admin.ModelAdmin):
    search_fields = ('attendee__first_name', 'attendee__last_name', 'attendee__first_name2', 'attendee__last_name2')
    list_display_links = ('attendee',)
    readonly_fields = ['id', 'created', 'modified']
    inlines = (AttendingMeetInline,) # add AttendanceInline when creating new Attending will fails on meet_names
    list_display = ('id', 'registration', 'attendee', 'meet_names', 'bed_needs', 'all_addresses')


class NoteAdmin(SummernoteModelAdmin):
    summernote_fields = ('body',)
    readonly_fields = ['id', 'created', 'modified']
    list_display = ('body', 'content_type', 'object_id', 'content_object', 'display_order', 'modified')


class RelationshipAdmin(admin.ModelAdmin):
    list_display_links = ('relation',)
    readonly_fields = ['id', 'created', 'modified']
    list_display = ('id', 'from_attendee', 'relation', 'to_attendee', 'emergency_contact', 'scheduler', 'relative','finish')


class AttendingMeetAdmin(admin.ModelAdmin):
    list_display_links = ('attending',)
    readonly_fields = ['id', 'created', 'modified']
    list_display = ('id', 'attending', 'meet', 'character', 'category', 'modified')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Note, NoteAdmin)
admin.site.register(Attendee, AttendeeAdmin)
admin.site.register(Registration, RegistrationAdmin)
admin.site.register(Attending, AttendingAdmin)
admin.site.register(Relation, RelationAdmin)
admin.site.register(Relationship, RelationshipAdmin)
admin.site.register(AttendingMeet, AttendingMeetAdmin)
