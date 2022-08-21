from django.db import models


class Skill(models.Model):
    """Data model for the skill resource

    Related Names: characters, default_characters

        """
    name = models.CharField(max_length=15)
    description = models.TextField()
    attribute = models.ForeignKey(
        "Attribute", on_delete=models.CASCADE, related_name="skills")

    def __str__(self):
        return self.name
