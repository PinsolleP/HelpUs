from django.db import transaction
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.decorators import login_required

from HelpUs.forms import RegisterForm, HelpRequestForm
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
        """Returns the first eight skills ordered by name."""
        return Skills.objects.order_by("name")[:8]

    def get_context_data(self, **kwargs):
        """
            Adds the six latest posts and their related data to the context.

            Returns:
                dict: Updated template context.
            """
        context = super().get_context_data(**kwargs)

        context["posts"] = Post.objects.select_related(
            "author"
        ).prefetch_related(  # optimize the retrieval of multiple relationships.
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
    """
        Handles user registration and profile creation.

        Saves the user and profile data in a single transaction.
        Logs in the user after successful registration.

        Args:
            request: HTTP request received from the browser.

        Returns:
            HttpResponse: Redirects to the homepage or displays the registration form.
        """
    form = RegisterForm()

    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            with transaction.atomic():

                # Creating the user account
                user = form.save()

                # Creating the profile
                post = Post.objects.create(author=user)

                # Retrieving the selected skills
                skills = list(form.cleaned_data['skills'])

                # Creating a new skill if necessary
                new_skill_name = form.cleaned_data['new_skill'].strip()

                new_skill = None

                if new_skill_name:
                    new_skill, created = Skills.objects.get_or_create(
                        name=new_skill_name
                    )
                    skills.append(new_skill)

                # Matching skills to the profile
                post.skills.set(skills)

                # Retrieving the selected activities
                activities = list(form.cleaned_data['activities'])

                # Creating a new activity if necessary
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

                        # Also add the skill to the profile
                        post.skills.add(activity_skill)

                # Associating activities with the profile
                post.activities.set(activities)

                # Association of Availabilities
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
    """Displays posts filtered by a selected skill."""
    model = Post
    template_name = "HelpUs/index.html"
    context_object_name = "posts"

    def get_queryset(self):
        """
            Returns posts associated with the selected skill.

            Returns:
                QuerySet: Posts matching the selected skill.
            """
        return Post.objects.filter(
            skills__id=self.kwargs["skill_id"]
        ).distinct()

    def get_context_data(self, **kwargs):
        """
            Adds the complete list of skills to the template context.

            Returns:
                dict: Updated template context.
            """
        context = super().get_context_data(**kwargs)

        context["latest_skills_list"] = Skills.objects.order_by("name")

        return context


@login_required
def create_help_request(request):
    """
    Handles the creation of a help request.
    Associates the request with the currently logged-in user.
    """
    if request.method == "POST":
        form = HelpRequestForm(request.POST)

        if form.is_valid():
            help_request = form.save(commit=False)
            help_request.requester = request.user
            help_request.save()
            form.save_m2m()

            return redirect('HelpUs:index')
    else:
        form = HelpRequestForm()

    return render(
        request,
        'HelpUs/help_request_form.html',
        {'form': form}
    )
