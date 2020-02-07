from django.contrib import admin
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
    inlines = (AssemblyAddressInline,)
    list_display = ('display_name', 'get_addresses', 'modified')


class PriceAdmin(admin.ModelAdmin):
    list_display = ('display_name', 'price_type', 'start', 'price_value', 'modified')


class ParticipationAdmin(admin.ModelAdmin):
    list_filter = ('gathering', 'attending', 'character', 'team')
    list_display = ('brief_program_session', 'attending', 'character', 'team', 'modified')


class ParticipationInline(admin.StackedInline):
    model = Participation
    extra = 0


class CharacterAdmin(admin.ModelAdmin):
    list_display = ('display_name', 'key', 'info', 'modified')


class TeamAdmin(admin.ModelAdmin):
    list_display = ('display_name', 'key', 'meet', 'display_order', 'modified')


class MeetAdmin(admin.ModelAdmin):
    search_fields = ('display_name',)
    list_display = ('display_name', 'key', 'info', 'url', 'modified')


class GatheringAdmin(admin.ModelAdmin):
    inlines = (ParticipationInline,)
    search_fields = ('meet__display_name', 'display_name')
    list_filter = ('meet',)
    list_display = ('meet', 'start', 'display_name', 'location', 'modified')


admin.site.register(AssemblyAddress, AssemblyAddressAdmin)
admin.site.register(Assembly, AssemblyAdmin)
admin.site.register(Price, PriceAdmin)
admin.site.register(Character, CharacterAdmin)
admin.site.register(Meet, MeetAdmin)
admin.site.register(Gathering, GatheringAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Participation, ParticipationAdmin)
