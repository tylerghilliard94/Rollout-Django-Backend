from django.db import models


class WeaponType(models.Model):
    name = models.CharField(max_length=15)
