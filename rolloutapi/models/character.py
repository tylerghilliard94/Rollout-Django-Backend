from django.db import models
import math


class Character(models.Model):
    characterName = models.CharField(max_length=30)
    characterClass = models.ForeignKey(
        "CharacterClass", on_delete=models.CASCADE, related_name="characters")
    level = models.IntegerField()
    race = models.ForeignKey(
        "Race", on_delete=models.CASCADE, related_name="characters")
    picture = models.CharField(max_length=100)
    description = models.TextField()
    alignment = models.ForeignKey(
        "Alignment", on_delete=models.CASCADE, related_name="characters")
    experience = models.IntegerField(default=0)
    strength = models.IntegerField(default=10)
    dexterity = models.IntegerField(default=10)
    constitution = models.IntegerField(default=10)
    intelligence = models.IntegerField(default=10)
    wisdom = models.IntegerField(default=10)
    charisma = models.IntegerField(default=10)
    proficiency_bonus = models.IntegerField(default=2)
    hitpoints = models.IntegerField(default=8)
    hitdice = models.IntegerField(default=6)
    skills = models.ManyToManyField("Skills", related_name="characters")
    armor_class = models.IntegerField(default=10)
    speed = models.IntegerField(default=30)
    languages = models.ManyToManyField("Languages", related_name="characters")
    spellcasting_ability = models.IntegerField(default=0)
    user = models.ForeignKey(
        "RolloutUser", on_delete=models.CASCADE, related_name="characters")

    @property
    def spell_attack_bonus(self):
        return self.spellcasting_ability + self.proficiency_bonus

    @property
    def spell_save_dc(self):
        return 8 + self.proficiency_bonus

    def bonus_calculator(self, attribute):
        return math.floor(attribute / 2) - 5

    @property
    def strength_bonus(self):
        return self.bonus_calculator(self.strength)

    @property
    def dexterity_bonus(self):
        return self.bonus_calculator(self.dexterity)

    @property
    def constitution_bonus(self):
        return self.bonus_calculator(self.constitution)

    @property
    def intelligence_bonus(self):
        return self.bonus_calculator(self.intelligence)

    @property
    def wisdom_bonus(self):
        return self.bonus_calculator(self.wisdom)

    @property
    def charisma_bonus(self):
        return self.bonus_calculator(self.charisma)
