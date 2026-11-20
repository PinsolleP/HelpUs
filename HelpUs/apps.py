"""
Configuration module for the HelpUs application.

Defines the application settings used by Django
during initialization.
"""
from django.apps import AppConfig


class HelpUsConfig(AppConfig):
    """
        Main configuration class for the HelpUs application.
        """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'HelpUs'
