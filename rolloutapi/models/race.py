from django.db import models


class Race(models.Model):
    """Data model for the race resource

    Related Names: sub_races

        """
    name = models.CharField(max_length=15)
    description = models.TextField()

    def __str__(self):
        return self.name
