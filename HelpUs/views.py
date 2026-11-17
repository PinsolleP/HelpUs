from django.views import generic

from HelpUs.models import Skills


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
