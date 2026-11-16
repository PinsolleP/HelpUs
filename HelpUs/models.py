from django.db import models

MAX_LENGTH = 20
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
