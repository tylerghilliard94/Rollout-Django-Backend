from django.db import models


class Skill(models.Model):
    name = models.CharField(max_length=15)
    description = models.TextField()
    attribute = models.ForeignKey(
        "Attribute", on_delete=models.CASCADE, related_name="skills")

    def __str__(self):
        return self.name
