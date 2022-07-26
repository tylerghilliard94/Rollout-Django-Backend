from rest_framework import serializers
from rolloutapi.models.alignment import Alignment


class AlignmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Alignment
        fields = ("id", "name", "description")
