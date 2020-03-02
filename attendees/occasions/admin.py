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
    prepopulated_fields = {"slug": ("display_name",)}
    inlines = (AssemblyAddressInline,)
    list_display = ('display_name', 'get_addresses', 'modified')
    readonly_fields = ['id', 'created', 'modified']


class PriceAdmin(admin.ModelAdmin):
    list_display = ('display_name', 'price_type', 'start', 'price_value', 'modified')


class ParticipationAdmin(admin.ModelAdmin):
    list_filter = ('gathering', 'attending', 'character', 'team')
    list_display = ('participation_info', 'attending', 'character', 'team', 'modified')
    readonly_fields = ['id','created', 'modified']
    fieldsets = (
        (None, {"fields": (tuple(['start', 'finish']),
                           tuple(['gathering', 'team']),
                           tuple(['attending', 'character']),
                           tuple(['free', 'display_order', 'category']),
                           tuple(['id', 'created', 'modified']),
                           ), }),
    )



class ParticipationInline(admin.StackedInline):
    model = Participation
    extra = 0
    fieldsets = (
        (None, {"fields": (tuple(['start', 'finish', 'free', 'category']),
                           tuple(['gathering', 'team', 'attending', 'character'])
                           ), }),
    )


class CharacterAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("display_name",)}
    list_display = ('display_name', 'slug', 'info', 'display_order', 'modified')


class TeamAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("display_name",)}
    list_display = ('display_name', 'slug', 'meet', 'display_order', 'modified')


class MeetAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("display_name",)}
    search_fields = ('display_name',)
    list_display = ('display_name', 'slug', 'info', 'url', 'modified')
    readonly_fields = ['id', 'created', 'modified']
    fieldsets = (
        (None, {"fields": (tuple(['start', 'finish', 'slug']),
                           tuple(['display_name', 'url']),
                           tuple(['site_type', 'info', 'division', 'site_id']),
                           tuple(['id', 'created', 'modified']),
                           ), }),
    )


class GatheringAdmin(admin.ModelAdmin):
    inlines = (ParticipationInline,)
    search_fields = ('meet__display_name', 'display_name')
    list_filter = ('meet',)
    list_display = ('meet', 'start', 'display_name', 'location', 'modified')
    readonly_fields = ['id', 'created', 'modified']
    fieldsets = (
        (None, {"fields": (tuple(['start', 'finish']),
                           tuple(['display_name', 'link']),
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
admin.site.register(Participation, ParticipationAdmin)
