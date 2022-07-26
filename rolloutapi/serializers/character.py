from rest_framework import serializers

from rolloutapi.models.character import Character
from rolloutapi.serializers.character_class import CharacterClassSerializer
from rolloutapi.serializers.feat import FeatSerializer
from rolloutapi.serializers.sub_race import SubRaceSerializer
from rolloutapi.serializers.alignment import AlignmentSerializer
from rolloutapi.serializers.skill import SkillSerializer
from rolloutapi.serializers.language import LanguageSerializer
from rolloutapi.serializers.rollout_user import RolloutUserSerializer


class CharacterSerializer(serializers.ModelSerializer):

    rollout_user = RolloutUserSerializer()
    character_class = CharacterClassSerializer()
    race = SubRaceSerializer()
    alignment = AlignmentSerializer()
    skills = SkillSerializer(many=True)
    languages = LanguageSerializer(many=True)
    feats = FeatSerializer(many=True)

    class Meta:
        model = Character
        fields = ("id", "rollout_user", "character_name", "description", "character_class", "level", "race",
                  "image", "alignment", "experience", "strength", "dexterity", "constitution",
                  "intelligence", "wisdom", "charisma", "hit_points", "skills", "armor_class", "languages",
                  "proficiency_bonus", "strength_bonus", "dexterity_bonus", "constitution_bonus", "intelligence_bonus",
                  "wisdom_bonus", "charisma_bonus", "spell_attack_bonus", "spell_save_dc", "feats", "spells")
