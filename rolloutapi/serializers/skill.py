from rest_framework import serializers
from rolloutapi.models.skill import Skill
from rolloutapi.serializers import AttributeSerializer


class SkillSerializer(serializers.ModelSerializer):

    attribute = AttributeSerializer()

    class Meta:
        model = Skill
        fields = ("id", "name", "description", "attribute")
