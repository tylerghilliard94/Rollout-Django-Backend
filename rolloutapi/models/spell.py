from django.db import models


class Spell(models.Model):
    """Data model for the spell resource

        """
    name = models.CharField(max_length=15)
    description = models.TextField()
    range = models.CharField(max_length=8)
    duration = models.CharField(max_length=8)
    concentration = models.BooleanField(default=False)
    ritual = models.BooleanField(default=False)
    casting_time = models.CharField(max_length=8)
    level = models.IntegerField(default=1)
    dc_save = models.ForeignKey(
        "Attribute", on_delete=models.CASCADE, related_name="spells")
    dc_success = models.CharField(max_length=10)
    school = models.ForeignKey(
        "MagicSchool", on_delete=models.CASCADE, related_name="spells")
    damage_type = models.ForeignKey(
        "DamageType", on_delete=models.CASCADE, related_name="spells")
    classes = models.ManyToManyField("CharacterClass", related_name="spells")
    characters = models.ManyToManyField("Character", related_name="spells")
    custom = models.BooleanField(default=False)

    def __str__(self):
        return self.name
