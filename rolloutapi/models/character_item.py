from django.db import models


class CharacterItem(models.Model):
    """Data model for the characterItem resource

        """
    character = models.ForeignKey(
        "Character", on_delete=models.CASCADE, related_name="character_items")
    item = models.ForeignKey(
        "Item", on_delete=models.CASCADE, related_name="character_items")
    quantity = models.IntegerField(default=1)
