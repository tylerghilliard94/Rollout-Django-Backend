from rest_framework import serializers
from rolloutapi.models.size import Size


class SizeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Size
        fields = ("id", "name")
