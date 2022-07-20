from django.db import models


class CharacterClass(models.Model):
    name = models.CharField(max_length=15)
    description = models.TextField()
    hit_dice = models.IntegerField(default=6)
    image = models.CharField(max_length=100)
    spellcasting_ability = models.ForeignKey(
        "Attribute", on_delete=models.CASCADE, related_name="character_classes")
