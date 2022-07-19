from django.db import models


class MagicSchool(models.Model):
    name = models.CharField(max_length=15)
