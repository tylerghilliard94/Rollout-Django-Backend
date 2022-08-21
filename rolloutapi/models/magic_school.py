from django.db import models


class MagicSchool(models.Model):
    """Data model for the magicSchool resource

    Related Names: spells

        """
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name
