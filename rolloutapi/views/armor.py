"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import action
from rolloutapi.serializers import ArmorSerializer, MultiArmorSerializer
import requests
from rolloutapi.models import Armor


class ArmorView(ViewSet):
    def list(self, request):
        """Handle get requests for multiple armor pieces, serialize said objects

        Returns:
        Serialized dictionaries in a list back to the client and a response of 200"""

        armor = Armor.objects.all()

        serializer = MultiArmorSerializer(armor, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk):
        """Handle get requests for single armor pieces, serialize said object

        Returns:
        Serialized dictionary to the client and a response of 200
        """

        armor = Armor.objects.get(pk=pk)

        serializer = ArmorSerializer(armor)

        return Response(serializer.data, status=status.HTTP_200_OK)
