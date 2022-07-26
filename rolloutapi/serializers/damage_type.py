from rest_framework import serializers
from rolloutapi.models import DamageType


class DamageTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = DamageType
        fields = ("id", "type", "description")
