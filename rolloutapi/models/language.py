from django.db import models


class Language(models.Model):
    """Data model for the language resource

    Related Names: characters, default_characters

        """
    name = models.CharField(max_length=15)
    description = models.TextField()

    def __str__(self):
        return self.name
