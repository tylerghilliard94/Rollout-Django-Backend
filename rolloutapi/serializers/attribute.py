from rest_framework import serializers
from rolloutapi.models import Attribute


class AttributeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Attribute
        fields = ("id", "name", "description")
