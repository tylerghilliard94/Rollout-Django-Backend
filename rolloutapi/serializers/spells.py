from rest_framework import serializers

from rolloutapi.models.character import Character
from rolloutapi.models.spell import Spell
from rolloutapi.serializers.attribute import AttributeSerializer
from rolloutapi.serializers.magic_school import MagicSchoolSerializer
from rolloutapi.serializers.damage_type import DamageTypeSerializer


class SpellSerializer(serializers.ModelSerializer):
    attribute = AttributeSerializer()
    school = MagicSchoolSerializer()
    damage_type = DamageTypeSerializer()

    class Meta:
        model = Spell
        fields = ("id", "name", "description", "range", "duration", "concentration", "ritual",
                  "casting_time", "level", "dc_save", "dc_success", "school", "damage_type", "classes", "custom")
