from django.db import models


class DCType(models.Model):
    type = models.CharField(max_length=15)
