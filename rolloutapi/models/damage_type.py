from django.db import models


class DamageType(models.Model):
    """Data model for the damageType resource

    Related Names: weapons, spells

        """
    type = models.CharField(max_length=15)
    description = models.TextField()

    def __str__(self):
        return self.type
