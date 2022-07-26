from rest_framework import serializers
from rolloutapi.models import MagicSchool


class MagicSchoolSerializer(serializers.ModelSerializer):

    class Meta:
        model = MagicSchool
        fields = ("id", "name")
