"""
Configures the Django administration interface for the HelpUs application.

Registers the application models and customizes their administration views.
"""
from django.contrib import admin

from HelpUs.models import Activities, Skills, Post


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


admin.site.register(Skills)
admin.site.register(Activities)
admin.site.register(Post)


