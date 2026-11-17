"""
Configuration des URL de l'application HelpUs.

Ce module définit les routes accessibles pour l'application
et associe chaque URL à une vue chargée de traiter la requête.

Les noms de routes sont regroupés dans l'espace de noms "HelpUs",
ce qui permet de les appeler sous la forme "HelpUs:nom_de_route".
"""
from django.urls import path

from . import views

# Espace de noms de l'application.
# Permet de distinguer les routes de HelpUS de celles des autres applications.

app_name = "HelpUs"

# Déclaration des routes de l'application.
urlpatterns = [
    # Page d'accueil : affiche les dix dernières compétences.
    path("", views.IndexView.as_view(), name="index"),

    # Affichage de l'ensemble des compétences.
    path("all/", views.AllSkillsView.as_view(), name="all"),
]
