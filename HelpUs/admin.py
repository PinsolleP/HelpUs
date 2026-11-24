"""
Configures the Django administration interface for the HelpUs application.

Registers the application models and customizes their administration views.
"""
from django.contrib import admin

from HelpUs.models import Activities, Skills, Post, HelpRequest


class ActivitiesInline(admin.TabularInline):
    """
    Allows activities to be managed directly from a skill's admin form.
    """
    model = Activities
    extra = 3


class SkillsAdmin(admin.ModelAdmin):
    """
    Customizes the administration interface for skills.

    Configures form fields, inline activities, list display,
    filters, search and ordering.
    """
    fieldsets = [
        (None, {"fields": ['name']}),
    ]
    inlines = [ActivitiesInline]
    list_display = ('name')
    list_filter = ('name')
    search_fields = ('name')
    ordering = ('name')


class HelpRequestAdmin(admin.ModelAdmin):
    """
    Customizes the administration interface for help requests.
    """
    list_display = (
        'requester',
        'skill',
        'display_availability',
        'volunteer',
        'created_at',
    )
    list_filter = ('skill', 'availability', 'created_at')
    search_fields = (
        'requester__username',
        'volunteer__username',
        'skill__name',
        'activity_description',
    )
    ordering = ('-created_at',)
    readonly_fields = ('created_at',)

    @admin.display(description="Disponibilités")
    def display_availability(self, obj):
        return ", ".join(
            availability.day for availability in obj.availability.all()
        )


admin.site.register(Skills)
admin.site.register(Activities)
admin.site.register(Post)
admin.site.register(HelpRequest, HelpRequestAdmin)
