from django.db import transaction
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.views import generic

from HelpUs.forms import RegisterForm
from HelpUs.models import Skills, Post, Activities


class IndexView(generic.ListView):
    """
        Displays the eight published skills by order name.

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
        ).order_by("id")[:6]

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


def signup_page(request):
    form = RegisterForm()

    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            with transaction.atomic():

                # Création du compte utilisateur
                user = form.save()

                # Création du profil
                post = Post.objects.create(author=user)

                # Récupération des compétences sélectionnées
                skills = list(form.cleaned_data['skills'])

                # Création d'une nouvelle compétence si nécessaire
                new_skill_name = form.cleaned_data['new_skill'].strip()

                new_skill = None

                if new_skill_name:
                    new_skill, created = Skills.objects.get_or_create(
                        name=new_skill_name
                    )
                    skills.append(new_skill)

                # Association des compétences au profil
                post.skills.set(skills)

                # Récupération des activités sélectionnées
                activities = list(form.cleaned_data['activities'])

                # Création d'une nouvelle activité si nécessaire
                new_activity_description = form.cleaned_data['new_activity'].strip()

                if new_activity_description:

                    activity_skill = (
                            new_skill
                            or form.cleaned_data['activity_skill']
                    )

                    if activity_skill:
                        new_activity, created = Activities.objects.get_or_create(
                            skills=activity_skill,
                            description=new_activity_description
                        )

                        activities.append(new_activity)

                        # Ajouter aussi la compétence au profil
                        post.skills.add(activity_skill)

                # Association des activités au profil
                post.activities.set(activities)

                # Association des disponibilités
                post.availability.set(
                    form.cleaned_data['availability']
                )

            login(request, user)

            return redirect('HelpUs:index')

    return render(
        request,
        'HelpUs/register.html',
        {'form': form}
    )


class FilterSkillView(generic.ListView):
    model = Post
    template_name = "HelpUs/index.html"
    context_object_name = "posts"

    def get_queryset(self):
        return Post.objects.filter(
            skills__id=self.kwargs["skill_id"]
        ).distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["latest_skills_list"] = Skills.objects.order_by("name")

        return context
