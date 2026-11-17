"""
Module de configuration de l'administration Django de l'application polls.

Personnalise l'affichage et la gestion des modèles Question et Choice
dans l'interface d'administration Django.

Permet notamment d'intégrer les choix directement dans le formulaire
d'une question et de configurer les listes, filtres et recherches.
"""
from django.contrib import admin

from HelpUs.models import Activities


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
