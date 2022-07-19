from django.db import models


class Weapon(models.Model):
    name = models.CharField(max_length=15)
    description = models.TextField()
    cost_gp = models.IntegerField(default=0)
    cost_sp = models.IntegerField(default=0)
    cost_cp = models.IntegerField(default=0)
    weight = models.IntegerField(default=1)
    weapon_type = models.ForeignKey(
        "WeaponType", on_delete=models.CASCADE, related_name="weapons")
    range = models.IntegerField(default=3)
    damage = models.IntegerField(default=0)
    damage_type = models.ForeignKey(
        "DamageType", on_delete=models.CASCADE, related_name="weapons")
    two_handed = models.BooleanField(default=False)
    two_handed_damage = models.IntegerField(default=0)
    custom = models.BooleanField(default=False)
