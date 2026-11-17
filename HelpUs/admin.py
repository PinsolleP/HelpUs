"""
Module de configuration de l'administration Django de l'application polls.

Personnalise l'affichage et la gestion des modèles Question et Choice
dans l'interface d'administration Django.

Permet notamment d'intégrer les choix directement dans le formulaire
d'une question et de configurer les listes, filtres et recherches.
"""
from django.contrib import admin

from HelpUs.models import Activities, Skills, Post


class ActivitiesInline(admin.TabularInline):
    """
        Permet de gérer les activitées d'une compétence directement dans son formulaire.

        Utilise un affichage sous forme de tableau pour intégrer les objets
        Activitées associés à une compétence.

        Attributes:
            model: Modèle utilisé pour les éléments intégrés (Activities).
            extra: Nombre de formulaires vides supplémentaires affichés.
        """
    model = Activities
    extra = 3


class SkillsAdmin(admin.ModelAdmin):
    """
        Personnalise l'interface d'administration du modèle Skills.

        Organise les champs du formulaire et configure l'affichage des
        questions, les filtres, la recherche et le tri.

        Attributes:
            fieldsets: Groupes de champs affichés dans le formulaire.
            inlines: Éléments Activitées intégrés au formulaire de compétence.
            list_display: Colonnes affichées dans la liste des compétences.
            list_filter: Champs utilisés pour filtrer les compétences.
            search_fields: Champs utilisés pour rechercher des compétences.
            ordering: Ordre initial de classement des compétences.
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


