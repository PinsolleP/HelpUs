"""
Defines the URL routes for the HelpUs application.

Maps each URL to its corresponding view.
Uses the HelpUs namespace to identify application routes.
"""
from django.urls import path

from . import views

app_name = "HelpUs"

# Declaration of the application's path.
urlpatterns = [
    # Homepage displaying the latest skills.
    path("", views.IndexView.as_view(), name="index"),

    # Displays all available skills.
    path("all/", views.AllSkillsView.as_view(), name="all"),

    # Displays the details of a selected skill.
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),

    # User registration page.
    path('signup/', views.signup_page, name="signup"),

    # Displays posts filtered by skill.
    path('competence/<int:skill_id>/', views.FilterSkillView.as_view(), name="filter_skill"),

    # Help request creation page.
    path('help-request/', views.create_help_request, name="create_help_request"),

    # Displays the details of a selected help request.
    path(
        'help-request/<int:pk>/',
        views.HelpRequestDetailView.as_view(),
        name="help_request_detail"
    ),
]
