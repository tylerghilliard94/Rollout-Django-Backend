from rolloutapi.models import CharacterClass
from rest_framework import serializers


class CharacterClassSerializer(serializers.ModelSerializer):

    class Meta:
        model = CharacterClass
        fields = ("id", "name", "description", "hit_dice",
                  "image", "spellcasting_ability")
