from django.db import models


class Money(models.Model):
    gp = models.IntegerField()
    sp = models.IntegerField()
    cp = models.IntegerField()
    character = models.ForeignKey(
        "character", on_delete=models.CASCADE, related_name="money")
