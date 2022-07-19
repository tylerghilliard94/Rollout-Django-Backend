from django.db import models


class Armor(models.Model):
    name = models.CharField(max_length=15)
    description = models.TextField()
    cost_gp = models.IntegerField(default=0)
    cost_sp = models.IntegerField(default=0)
    cost_cp = models.IntegerField(default=0)
    weight = models.IntegerField(default=1)
    custom = models.BooleanField(default=False)
