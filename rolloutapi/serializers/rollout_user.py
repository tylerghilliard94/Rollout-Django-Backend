from rolloutapi.models import RolloutUser
from rest_framework import serializers
from rolloutapi.serializers.django_user import DjangoUserSerializer


class RolloutUserSerializer(serializers.ModelSerializer):
    user = DjangoUserSerializer()

    class Meta:
        model = RolloutUser
        fields = ("id", "user", "bio", "profile_image")
