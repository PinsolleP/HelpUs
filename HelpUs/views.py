from django.contrib.auth import forms, login
from django.shortcuts import render, redirect
from django.views import generic

from HelpUs.config import settings
from HelpUs.models import Skills, Post


class IndexView(generic.ListView):
    """
        Displays the eight most recently published skills.

        Uses the Skills model and the HelpUs/index.html template.

        Attributes:
            template_name (str): Path of the template used.
            context_object_name (str): Name of the variable containing
            the list of skills in the template.
        """
    template_name = "HelpUs/index.html"
    context_object_name = "latest_skills_list"

    def get_queryset(self):
        """Return all skills."""
        return Skills.objects.order_by("name")[:8]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["posts"] = Post.objects.select_related(
            "author"
        ).prefetch_related(  # optimise la récupération des relations multiples.
            "skills",
            "activities",
            "availability"
        )

        return context


class AllSkillsView(generic.ListView):
    """
        Displays the complete list of recorded skills.

        Unlike IndexView, this view does not limit
        the number of skills retrieved.

        Attributes:
            template_name (str): Path to the template used.
        """
    template_name = "HelpUs/all.html"

    def get_queryset(self):
        """
            Retrieve all skills stored in the database.

             Returns:
                QuerySet: Set of existing skills.
             """
        return Skills.objects.all()


class DetailView(generic.DetailView):
    """
        Displays the details of a selected skill.

        Uses the Skills model to automatically retrieve the object corresponding to the ID passed in the URL.

        Attributes:
            model: Model used to retrieve the skill.
            template_name (str): Path to the detail template.
            context_object_name (str): Name of the variable containing
        """
    model = Skills
    template_name = "HelpUs/detail.html"
    context_object_name = "skills"
