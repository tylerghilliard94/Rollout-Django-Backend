from django.db import models


class SubRace(models.Model):
    name = models.CharField(max_length=15)
    description = models.TextField()
    base_race = models.ForeignKey(
        "Race", on_delete=models.CASCADE, related_name="sub_races")
    strength_bonus = models.IntegerField()
    dexterity_bonus = models.IntegerField()
    constitution_bonus = models.IntegerField()
    intelligence_bonus = models.IntegerField()
    wisdom_bonus = models.IntegerField()
    charisma_bonus = models.IntegerField()
    able_to_choose = models.BooleanField(default=False)
    choosable_stat_num = models.IntegerField()
