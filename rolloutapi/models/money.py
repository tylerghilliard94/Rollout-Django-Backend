from django.db import models


class Money(models.Model):
    """Data model for the money resource

        """
    gp = models.IntegerField(default=0)
    sp = models.IntegerField(default=0)
    cp = models.IntegerField(default=0)
    character = models.ForeignKey(
        "character", on_delete=models.CASCADE, related_name="money")

    def __str__(self):
        return self.character.character_name + "'s Money"
