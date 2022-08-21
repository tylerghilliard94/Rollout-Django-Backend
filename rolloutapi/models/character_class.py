from django.db import models


class CharacterClass(models.Model):
    """Data model for the character resource

    Related Names: characters, default_characters, feats, spells

        """
    name = models.CharField(max_length=15)
    description = models.TextField()
    hit_dice = models.IntegerField(default=6)
    image = models.CharField(max_length=100)
    spellcasting_ability = models.ForeignKey(
        "Attribute", on_delete=models.CASCADE, related_name="character_classes")

    def __str__(self):
        return self.name
