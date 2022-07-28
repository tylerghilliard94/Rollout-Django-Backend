from rest_framework import serializers
from rolloutapi.models.weapon_type import WeaponType


class WeaponTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = WeaponType
        fields = ("id", "name")
