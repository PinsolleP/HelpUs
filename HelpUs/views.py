from django.http import HttpResponse
from django.views import generic

from HelpUs.models import Skills


class Home(generic.ListView):

    template_name = "HelpUs/home.html"
    context_object_name = "latest_skills_list"

    def get_queryset(self):
        """Return the last ten published skills."""
        return Skills.objects.order_by("name")[:10]
