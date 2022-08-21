from django.db import models


class WeaponType(models.Model):
    """Data model for the weaponType resource

    Related Names: weapons

        """
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name
