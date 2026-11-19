"""
Configuration of the HelpUs app URLs.

This module defines the routes accessible for the app
and links each URL to a view responsible for handling the request.

The route names are grouped in the "HelpUs" namespace,
which allows you to call them like "HelpUs:route_name".
"""
from django.urls import path

from . import views

app_name = "HelpUs"

# Declaration of the application's path.
urlpatterns = [
    # Home page: shows the last eight skills.
    path("", views.IndexView.as_view(), name="index"),

    # Display of all skills.
    path("all/", views.AllSkillsView.as_view(), name="all"),

    # Detail of available skills.
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),

    # Register page
    path('signup/', views.signup_page, name="signup"),
]
