from django.db import models
import math


class Character(models.Model):
    """Data model for the character resource

    Methods: bonus_calculator, calculate_level

    Custom properties: level_by_experience, proficiency bonus, strength_bonus, dexterity_bonus,
    constitution_bonus, intelligence_bonus, wisdom_bonus, charisma_bonus, spell_attack_bonus, spell_save_dc

    Related Names: spells, money, weapons, character_items, feats

        """
    character_name = models.CharField(max_length=30)
    character_class = models.ForeignKey(
        "CharacterClass", on_delete=models.CASCADE, related_name="characters")
    level = models.IntegerField()
    race = models.ForeignKey(
        "SubRace", on_delete=models.CASCADE, related_name="characters")
    image = models.CharField(max_length=100)
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
    hit_points = models.IntegerField(default=8)
    temp_hit_points = models.IntegerField(default=0)
    skills = models.ManyToManyField("Skill", related_name="characters")
    armor_class = models.IntegerField(default=10)
    languages = models.ManyToManyField("Language", related_name="characters")
    rollout_user = models.ForeignKey(
        "RolloutUser", on_delete=models.CASCADE, related_name="characters")

    def __str__(self):
        return self.character_name

    def bonus_calculator(self, attribute):
        """Calculates the bonuses for each attribute."""
        return math.floor(attribute / 2) - 5

    def calculate_level(self):
        if self.experience < 300:
            return 1
        elif self.experience < 900:
            return 2
        elif self.experience < 2700:
            return 3
        elif self.experience < 6500:
            return 4
        elif self.experience < 14000:
            return 5
        elif self.experience < 23000:
            return 6
        elif self.experience < 34000:
            return 7
        elif self.experience < 48000:
            return 8
        elif self.experience < 64000:
            return 9
        elif self.experience < 85000:
            return 10
        elif self.experience < 100000:
            return 11
        elif self.experience < 120000:
            return 12
        elif self.experience < 140000:
            return 13
        elif self.experience < 165000:
            return 14
        elif self.experience < 195000:
            return 15
        elif self.experience < 225000:
            return 16
        elif self.experience < 265000:
            return 17
        elif self.experience < 305000:
            return 18
        elif self.experience < 355000:
            return 19
        else:
            return 20

    @property
    def level_by_experience(self):
        return self.calculate_level()

    @property
    def proficiency_bonus(self):
        return math.ceil(self.level / 4 + 1)

    @property
    def strength_bonus(self):
        return self.bonus_calculator(self.strength + self.race.strength_bonus)

    @property
    def dexterity_bonus(self):
        return self.bonus_calculator(self.dexterity + self.race.dexterity_bonus)

    @property
    def constitution_bonus(self):
        return self.bonus_calculator(self.constitution + self.race.constitution_bonus)

    @property
    def intelligence_bonus(self):
        return self.bonus_calculator(self.intelligence + self.race.intelligence_bonus)

    @property
    def wisdom_bonus(self):
        return self.bonus_calculator(self.wisdom + self.race.wisdom_bonus)

    @property
    def charisma_bonus(self):
        return self.bonus_calculator(self.charisma + self.race.charisma_bonus)

    @property
    def spell_attack_bonus(self):
        if self.character_class.name == "Barbarian":
            return 0

        switcher = {
            "Strength": self.strength_bonus,
            "Dexterity": self.dexterity_bonus,
            "Constitution": self.constitution_bonus,
            "Intelligence": self.intelligence_bonus,
            "Wisdom": self.wisdom_bonus,
            "Charisma": self.charisma_bonus
        }

        key = self.character_class.spellcasting_ability.name
        return switcher.get(key) + self.proficiency_bonus

    @property
    def spell_save_dc(self):
        if self.character_class.name == "Barbarian":
            return 0

        switcher = {
            "Strength": self.strength_bonus,
            "Dexterity": self.dexterity_bonus,
            "Constitution": self.constitution_bonus,
            "Intelligence": self.intelligence_bonus,
            "Wisdom": self.wisdom_bonus,
            "Charisma": self.charisma_bonus
        }

        key = self.character_class.spellcasting_ability.name

        return 8 + switcher.get(key) + self.proficiency_bonus
