from rest_framework import serializers
from rolloutapi.models.feat import Feat


class FeatSerializer(serializers.ModelSerializer):

    class Meta:
        model = Feat
        fields = ("id", "name", "description", "level",
                  "classes", "characters", "custom")
