from django.db import models


class Language(models.Model):
    name = models.CharField(max_length=15)
    description = models.TextField()
