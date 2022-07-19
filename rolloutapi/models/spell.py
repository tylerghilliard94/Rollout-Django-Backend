from django.db import models


class Spell(models.Model):
    name = models.CharField(max_length=15)
    description = models.TextField()
    range = models.CharField(max_length=8)
    duration = models.CharField(max_length=8)
    concentration = models.BooleanField(default=False)
    ritual = models.BooleanField(default=False)
    casting_time = models.CharField(max_length=8)
    level = models.IntegerField(default=1)
    dc_save = models.ForeignKey(
        "DCType", on_delete=models.CASCADE, related_name="spells")
    dc_success = models.CharField(max_length=10)
    school = models.ForeignKey(
        "MagicSchool", on_delete=models.CASCADE, related_name="spells")
    damage_type = models.ForeignKey(
        "DamageType", on_delete=models.CASCADE, related_name="spells")
