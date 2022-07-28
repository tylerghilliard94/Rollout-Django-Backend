from rest_framework import serializers
from rolloutapi.models import Weapon
from rolloutapi.serializers.damage_type import DamageTypeSerializer
from rolloutapi.serializers.weapon_type import WeaponTypeSerializer


class WeaponSerializer(serializers.ModelSerializer):
    weapon_type = WeaponTypeSerializer()
    damage_type = DamageTypeSerializer()

    class Meta:
        model = Weapon
        fields = ("id", "name", "description", "cost_gp", "cost_sp",
                  "cost_cp", "weapon_type", "range", "damage", "damage_type",
                  "two_handed", "two_handed_damage", "weight", "custom")


class MultiWeaponSerializer(serializers.ModelSerializer):

    class Meta:
        model = Weapon
        fields = ("id", "name", "custom")
