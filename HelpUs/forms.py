from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

from .models import Skills, Activities, Availability


class RegisterForm(UserCreationForm):
    """
        Handles user registration and profile information.

        Allows users to select or add skills, activities and availability.
        """
    skills = forms.ModelMultipleChoiceField(
        queryset=Skills.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Mes compétences"
    )

    new_skill = forms.CharField(
        required=False,
        max_length=50,
        label="Ajouter une compétence"
    )

    activities = forms.ModelMultipleChoiceField(
        queryset=Activities.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Mes activités"
    )

    new_activity = forms.CharField(
        required=False,
        max_length=50,
        label="Ajouter une activité"
    )

    availability = forms.ModelMultipleChoiceField(
        queryset=Availability.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Mes disponibilités"
    )

    activity_skill = forms.ModelChoiceField(
        queryset=Skills.objects.all(),
        required=False,
        label="Compétence associée à cette activité"
    )

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'email', 'first_name', 'last_name')

    def clean(self):
        """
           Validates the form data.

           Checks that a new activity has an associated skill.

           Returns:
               dict: Validated form data.
           """
        cleaned_data = super().clean()

        new_activity = cleaned_data.get('new_activity', '').strip()
        new_skill = cleaned_data.get('new_skill', '').strip()
        activity_skill = cleaned_data.get('activity_skill')

        if new_activity and not new_skill and not activity_skill:
            self.add_error(
                'activity_skill',
                "Vous devez sélectionner une compétence ou en créer une nouvelle."
            )

        return cleaned_data
