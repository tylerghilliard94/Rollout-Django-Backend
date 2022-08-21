from django.db import models


class Armor(models.Model):
    """Data model for the armor resource

    Related Names: 

        """
    name = models.CharField(max_length=15)
    description = models.TextField()
    armor_class = models.IntegerField(default=10)
    cost_gp = models.IntegerField(default=0)
    cost_sp = models.IntegerField(default=0)
    cost_cp = models.IntegerField(default=0)
    str_minimum = models.IntegerField(default=10)
    stealth_disadvantage = models.BooleanField(default=False)
    weight = models.IntegerField(default=1)
    custom = models.BooleanField(default=False)
    characters = models.ManyToManyField("Character", related_name="armor")

    def __str__(self):
        return self.name
