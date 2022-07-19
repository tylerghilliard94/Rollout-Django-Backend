from django.db import models


class Size(models.Model):

    name = models.CharField(max_length=10)
