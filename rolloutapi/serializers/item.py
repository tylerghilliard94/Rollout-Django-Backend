from rest_framework import serializers
from rolloutapi.models import Item


class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = ("id", "name", "description", "cost_gp", "cost_sp",
                  "cost_cp", "weight", "custom")


class MultiItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = ("id", "name", "custom")
