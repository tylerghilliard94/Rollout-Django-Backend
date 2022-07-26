from rest_framework import serializers
from rolloutapi.models.language import Language


class LanguageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Language
        fields = ("id", "name", "description")
