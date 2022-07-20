from django.db import models


class DamageType(models.Model):
    type = models.CharField(max_length=15)
    description = models.TextField()
