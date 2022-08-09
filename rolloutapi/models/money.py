from django.db import models


class Money(models.Model):
    gp = models.IntegerField()
    sp = models.IntegerField()
    cp = models.IntegerField()
    character = models.ForeignKey(
        "character", on_delete=models.CASCADE, related_name="money")

    def __str__(self):
        return self.character.character_name + "'s Money"
