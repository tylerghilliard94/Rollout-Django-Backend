from django.db import models


class Feat(models.Model):
    """Data model for the feat resource

    Related Names: characters, character_classes

        """
    name = models.CharField(max_length=15)
    description = models.TextField()
    level = models.IntegerField(default=1)
    classes = models.ManyToManyField("CharacterClass", related_name="feats")
    characters = models.ManyToManyField("Character", related_name="feats")
    custom = models.BooleanField(default=False)

    def __str__(self):
        return self.name
