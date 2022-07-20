from django.db import models


class DefaultCharacter(models.Model):
    character_name = models.CharField(max_length=30)
    character_class = models.ForeignKey(
        "CharacterClass", on_delete=models.CASCADE, related_name="default_characters")
    level = models.IntegerField()
    race = models.ForeignKey(
        "SubRace", on_delete=models.CASCADE, related_name="default_characters")
    image = models.CharField(max_length=100)
    description = models.TextField()
    alignment = models.ForeignKey(
        "Alignment", on_delete=models.CASCADE, related_name="default_characters")
    experience = models.IntegerField(default=0)
    strength = models.IntegerField(default=10)
    dexterity = models.IntegerField(default=10)
    constitution = models.IntegerField(default=10)
    intelligence = models.IntegerField(default=10)
    wisdom = models.IntegerField(default=10)
    charisma = models.IntegerField(default=10)
    hit_points = models.IntegerField(default=8)
    skills = models.ManyToManyField("Skill", related_name="default_characters")
    armor_class = models.IntegerField(default=10)
    languages = models.ManyToManyField(
        "Language", related_name="default_characters")
