from rest_framework import serializers
from rolloutapi.models import DefaultCharacter
from rolloutapi.serializers.character_class import CharacterClassSerializer
from rolloutapi.serializers.sub_race import SubRaceSerializer
from rolloutapi.serializers.alignment import AlignmentSerializer
from rolloutapi.serializers.skill import SkillSerializer
from rolloutapi.serializers.language import LanguageSerializer


class DefaultCharacterSerializer(serializers.ModelSerializer):

    character_class = CharacterClassSerializer()
    race = SubRaceSerializer()
    alignment = AlignmentSerializer()
    skills = SkillSerializer(many=True)
    languages = LanguageSerializer(many=True)

    class Meta:
        model = DefaultCharacter
        fields = ("id", "character_name", "description", "character_class", "level", "race",
                  "image", "alignment", "experience", "strength", "dexterity", "constitution",
                  "intelligence", "wisdom", "charisma", "hit_points", "skills", "armor_class", "languages")
