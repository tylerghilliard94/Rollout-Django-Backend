from django.db import models


class Attribute(models.Model):
    """Data model for the attribute resource

    Related Names: skills, spells, character_classes
        """
    name = models.CharField(max_length=15)
    abbr_name = models.CharField(max_length=4)
    description = models.TextField()

    def __str__(self):
        return self.name
