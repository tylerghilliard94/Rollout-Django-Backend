from django.db import models


class Alignment(models.Model):
    """Data model for the alignment resource


    Related Names: characters, default_characters

        """
    name = models.CharField(max_length=15)
    description = models.TextField()

    def __str__(self):
        return self.name
