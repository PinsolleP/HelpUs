from django.contrib.auth import get_user_model
from django.db import models

from HelpUs.static.constant import Day_choices

MAX_LENGTH = 50
"""Maximum length of texts displayed in summary views."""


def text_excerpt(text, max_length):
    """
        Return a text snippet limited to a given length.

        Add three dots if the text exceeds the limit.

        Args:
            text (str): Text to shorten.
            max_length (int): Maximum number of characters to keep.

        Returns:
            str: Full text or snippet followed by ellipsis.
        """
    return text[:max_length] + ('...' if len(text) > max_length else '')


class Skills(models.Model):
    """
        Represents a skill offered by a user.
        """
    name = models.CharField(max_length=MAX_LENGTH)

    def __str__(self):
        """
            Returns a text representation of the skills.

            The text is limited to the length defined by MAX_LENGTH.

            Returns:
                str: Shortened text of the skills.
            """
        return text_excerpt(self.name, MAX_LENGTH)


class Activities(models.Model):
    """
            Represents a specific activity for a skill.
            """
    skills = models.ForeignKey(Skills, on_delete=models.CASCADE)
    description = models.CharField(max_length=MAX_LENGTH)

    def __str__(self):
        """
            Returns a text representation of the Activities.

            The text is limited to the length defined by MAX_LENGTH.

            Returns:
                str: Shortened text of the activities.
            """
        return text_excerpt(self.description, MAX_LENGTH)


class Availability(models.Model):
    day = models.CharField(
        max_length=MAX_LENGTH,
        choices=Day_choices,
        default=Day_choices[0][0]
    )

    def __str__(self):
        return self.day


User = get_user_model()


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    skills = models.ManyToManyField(Skills, related_name='posts', blank=True)
    activities = models.ManyToManyField(Activities, related_name='posts', blank=True)
    availability = models.ManyToManyField(Availability, related_name='posts', blank=True)

    def __str__(self):
        username = self.author.username

        skill_names = ", ".join(
            skill.name for skill in self.skills.all()
        ) or "Aucune compétence"

        activity_names = ", ".join(
            activity.description for activity in self.activities.all()
        ) or "Aucune activité"

        availability_days = ", ".join(
            availability.day for availability in self.availability.all()
        ) or "Non spécifié"

        return (
            f"{username} - {skill_names} | "
            f"{activity_names} | {availability_days}"
        )