from rest_framework import serializers

from rolloutapi.models.character import Character
from rolloutapi.models.spell import Spell
from rolloutapi.serializers.character_class import CharacterClassSerializer

from rolloutapi.serializers.magic_school import MagicSchoolSerializer
from rolloutapi.serializers.damage_type import DamageTypeSerializer


class SpellSerializer(serializers.ModelSerializer):

    school = MagicSchoolSerializer()
    damage_type = DamageTypeSerializer()
    classes = CharacterClassSerializer(many=True)

    class Meta:
        model = Spell
        fields = ("id", "name", "description", "range", "duration", "concentration", "ritual",
                  "casting_time", "level", "dc_save", "dc_success", "school", "damage_type", "classes", "custom")


class MultiSpellSerializer(serializers.ModelSerializer):

    school = MagicSchoolSerializer()
    damage_type = DamageTypeSerializer()
    classes = CharacterClassSerializer(many=True)

    class Meta:
        model = Spell
        fields = ("id", "name", "description", "level",
                  "school", "damage_type", "classes", "custom")
