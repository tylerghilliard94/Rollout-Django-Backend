from django.db import models


class Weapon(models.Model):
    """Data model for the weapon resource

        """
    name = models.CharField(max_length=15)
    description = models.TextField()
    cost_gp = models.IntegerField(default=0)
    cost_sp = models.IntegerField(default=0)
    cost_cp = models.IntegerField(default=0)
    weight = models.IntegerField(default=1)
    weapon_type = models.ForeignKey(
        "WeaponType", on_delete=models.CASCADE, related_name="weapons")
    range = models.IntegerField(default=3)
    damage = models.CharField(max_length=5)
    damage_type = models.ForeignKey(
        "DamageType", on_delete=models.CASCADE, related_name="weapons")
    two_handed = models.BooleanField(default=False)
    two_handed_damage = models.CharField(max_length=5)
    ranged = models.BooleanField(default=False)
    custom = models.BooleanField(default=False)
    characters = models.ManyToManyField("Character", related_name="weapons")

    def __str__(self):
        return self.name
