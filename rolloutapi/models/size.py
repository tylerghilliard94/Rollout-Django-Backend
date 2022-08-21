from django.db import models


class Size(models.Model):
    """Data model for the size resource

    Related Names: sub_races

        """
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name
