from rest_framework import serializers
from rolloutapi.models import Armor


class ArmorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Armor
        fields = ("id", "name", "description", "armor_class", "cost_gp", "cost_sp",
                  "cost_cp", "str_minimum", "stealth_disadvantage", "weight", "custom")
