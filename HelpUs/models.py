from django.db import models

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


class Category(models.Model):
    """
        Represents a category of skill.
        """
    name = models.CharField(max_length=MAX_LENGTH)

    def __str__(self):
        """
            Returns a text representation of the Activities.

            The text is limited to the length defined by MAX_LENGTH.

            Returns:
                str: Shortened text of the activities.
            """
        return text_excerpt(self.name, MAX_LENGTH)


class Skills(models.Model):
    """
        Represents a skill offered by a user.
        """
    name = models.CharField(max_length=MAX_LENGTH)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

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



