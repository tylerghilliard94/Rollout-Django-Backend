from django.db import models


class CharacterItem(models.Model):
    character = models.ForeignKey(
        "Character", on_delete=models.CASCADE, related_name="characters")
    item = models.ForeignKey(
        "Item", on_delete=models.CASCADE, related_name="characterItems")
    quantity = models.IntegerField(default=1)
