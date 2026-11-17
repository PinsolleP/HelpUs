"""
Configuration des URL de l'application polls.

Ce module définit les routes accessibles pour l'application
et associe chaque URL à une vue chargée de traiter la requête.

Les noms de routes sont regroupés dans l'espace de noms "polls",
ce qui permet de les appeler sous la forme "polls:nom_de_route".
"""
from django.urls import path

from . import views

# Espace de noms de l'application.
# Permet de distinguer les routes de polls de celles des autres applications.

app_name = "HelpUs"

# Déclaration des routes de l'application.
urlpatterns = [
]
