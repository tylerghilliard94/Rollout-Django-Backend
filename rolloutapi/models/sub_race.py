from django.db import models


class SubRace(models.Model):
    """Data model for the subRace resource

    Related Names: characters, default_characters

        """
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
    size = models.ForeignKey(
        "Size", on_delete=models.CASCADE, related_name="sub_races")
    able_to_choose_1 = models.BooleanField(default=False)
    choosable_stat_num_1 = models.IntegerField()
    able_to_choose_2 = models.BooleanField(default=False)
    choosable_stat_num_2 = models.IntegerField()
    flight_capable = models.BooleanField(default=False)
    speed = models.IntegerField(default=30)
    flight_speed = models.IntegerField(default=30)

    def __str__(self):
        return self.name
