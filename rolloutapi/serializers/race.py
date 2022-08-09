from rest_framework import serializers
from rolloutapi.models.race import Race


class RaceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Race
        fields = ("id", "name",  "description")
