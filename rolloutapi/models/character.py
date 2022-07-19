from django.db import models
import math


class Character(models.Model):
    character_name = models.CharField(max_length=30)
    character_class = models.ForeignKey(
        "CharacterClass", on_delete=models.CASCADE, related_name="characters")
    level = models.IntegerField()
    race = models.ForeignKey(
        "SubRace", on_delete=models.CASCADE, related_name="characters")
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
    hit_points = models.IntegerField(default=8)
    temp_hit_points = models.IntegerField(default=0)
    skills = models.ManyToManyField("Skills", related_name="characters")
    armor_class = models.IntegerField(default=10)
    languages = models.ManyToManyField("Languages", related_name="characters")
    rollout_user = models.ForeignKey(
        "RolloutUser", on_delete=models.CASCADE, related_name="characters")

    def bonus_calculator(self, attribute):
        """Calculates the bonuses for each attribute."""
        return math.floor(attribute / 2) - 5

    @property
    def strength_bonus(self):
        return self.bonus_calculator(self.strength) + self.race.objects.get(self.race).strength_bonus

    @property
    def dexterity_bonus(self):
        return self.bonus_calculator(self.dexterity) + self.race.objects.get(self.race).dexterity_bonus

    @property
    def constitution_bonus(self):
        return self.bonus_calculator(self.constitution) + self.race.objects.get(self.race).constitution_bonus

    @property
    def intelligence_bonus(self):
        return self.bonus_calculator(self.intelligence) + self.race.objects.get(self.race).intelligence_bonus

    @property
    def wisdom_bonus(self):
        return self.bonus_calculator(self.wisdom) + self.race.objects.get(self.race).wisdom_bonus

    @property
    def charisma_bonus(self):
        return self.bonus_calculator(self.charisma) + self.race.objects.get(self.race).charisma_bonus

    @property
    def spell_attack_bonus(self):
        if self.character_class.all().name == "Barbarian":
            return 0

        switcher = {
            "Strength": self.strength_bonus,
            "Dexterity": self.dexterity_bonus,
            "Constitution": self.constitution_bonus,
            "Intelligence": self.intelligence_bonus,
            "Wisdom": self.wisdom_bonus,
            "Charisma": self.charisma_bonus
        }

        key = self.character_class.all().spellcasting_ability.name
        return switcher.get(key) + self.proficiency_bonus

    @property
    def spell_save_dc(self):
        if self.character_class.all().name == "Barbarian":
            return 0

        switcher = {
            "Strength": self.strength_bonus,
            "Dexterity": self.dexterity_bonus,
            "Constitution": self.constitution_bonus,
            "Intelligence": self.intelligence_bonus,
            "Wisdom": self.wisdom_bonus,
            "Charisma": self.charisma_bonus
        }

        key = self.character_class.all().spellcasting_ability.name

        return 8 + switcher.get(key) + self.proficiency_bonus
