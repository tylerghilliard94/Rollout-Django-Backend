from django.db import models


class CharacterItem(models.Model):
    character = models.ForeignKey(
        "Character", on_delete=models.CASCADE, related_name="characters")
