from django.db import models


class CharacterClass(models.Model):
    name = models.CharField(max_length=15)
    description = models.TextField()
    hitdice = models.IntegerField(default=6)
    image = models.CharField(max_length=50)
