from django.contrib import admin
from django.contrib.postgres import fields
from django_json_widget.widgets import JSONEditorWidget
from attendees.persons.models import *
from attendees.whereabouts.models import *
from .models import *

# Register your models here.


class AssemblyAddressAdmin(admin.ModelAdmin):
    list_display = ('assembly', 'address', 'modified')


class AssemblyAddressInline(admin.TabularInline):
    model = AssemblyAddress
    extra = 0


class AssemblyAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("display_name",)}
    inlines = (AssemblyAddressInline,)
    list_display_links = ('display_name',)
    list_display = ('id', 'division', 'display_name', 'slug', 'get_addresses')
    readonly_fields = ['id', 'created', 'modified']


class PriceAdmin(admin.ModelAdmin):
    list_display = ('display_name', 'price_type', 'start', 'price_value', 'modified')


class AttendanceAdmin(admin.ModelAdmin):
    list_display_links = ('attending',)
    list_filter = ('gathering', 'attending', 'character', 'team')
    list_display = ('id', 'attendance_info', 'attending', 'character', 'team', 'modified')
    readonly_fields = ['id','created', 'modified']
    fieldsets = (
        (None, {"fields": (tuple(['start', 'finish']),
                           tuple(['gathering', 'team']),
                           tuple(['attending', 'character']),
                           tuple(['free', 'display_order', 'category']),
                           tuple(['id', 'created', 'modified']),
                           tuple(['infos']),
                           ), }),
    )


class AttendanceInline(admin.StackedInline):
    model = Attendance
    extra = 0
    fieldsets = (
        (None, {"fields": (tuple(['start', 'finish', 'free', 'category']),
                           tuple(['gathering', 'team', 'attending', 'character']),
                           tuple(['infos']),
                           ), }),
    )


class CharacterAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("display_name",)}
    list_filter = ('assembly',)
    list_display_links = ('display_name',)
    list_display = ('id', 'assembly', 'display_name', 'slug', 'display_order', 'type')


class TeamAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("display_name",)}
    readonly_fields = ['id', 'created', 'modified']
    list_display = ('id', 'display_name', 'slug', 'meet', 'display_order', 'modified')


class MeetAdmin(admin.ModelAdmin):
    formfield_overrides = {
        fields.JSONField: {'widget': JSONEditorWidget},
    }
    prepopulated_fields = {"slug": ("display_name",)}
    search_fields = ('display_name',)
    list_filter = ('assembly',)
    list_display_links = ('display_name',)
    list_display = ('id', 'display_name', 'slug', 'assembly')
    readonly_fields = ['id', 'created', 'modified']
    fieldsets = (
        (None, {"fields": (tuple(['start', 'finish', 'slug']),
                           tuple(['display_name', 'infos']),
                           tuple(['site_type', 'assembly', 'site_id']),
                           tuple(['id', 'created', 'modified']),
                           ), }),
    )


class GatheringAdmin(admin.ModelAdmin):
    formfield_overrides = {
        fields.JSONField: {'widget': JSONEditorWidget},
    }
    inlines = (AttendanceInline,)
    list_display_links = ('display_name',)
    search_fields = ('meet__display_name', 'display_name')
    list_filter = ('meet',)
    list_display = ('id', 'meet', 'start', 'display_name', 'location', 'modified')
    readonly_fields = ['id', 'created', 'modified']
    fieldsets = (
        (None, {"fields": (tuple(['start', 'finish']),
                           tuple(['display_name', 'infos']),
                           tuple(['site_type', 'meet', 'site_id', 'occurrence']),
                           tuple(['id', 'created', 'modified']),
                           ), }),
    )


admin.site.register(AssemblyAddress, AssemblyAddressAdmin)
admin.site.register(Assembly, AssemblyAdmin)
admin.site.register(Price, PriceAdmin)
admin.site.register(Character, CharacterAdmin)
admin.site.register(Meet, MeetAdmin)
admin.site.register(Gathering, GatheringAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Attendance, AttendanceAdmin)
