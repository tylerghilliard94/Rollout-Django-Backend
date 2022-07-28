"""View module for handling requests about game types"""


from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
import requests
from rolloutapi.models.default_character import DefaultCharacter
from rolloutapi.serializers import DefaultCharacterSerializer, MultiDefaultCharacterSerializer


class DefaultCharacterView(ViewSet):
    def list(self, request):
        """Handle get requests for multiple default characters, serialize said objects

        Returns:
        Serialized dictionaries in a list back to the client and a response of 200"""

        default_characters = DefaultCharacter.objects.all()

        serializer = MultiDefaultCharacterSerializer(
            default_characters, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk):
        """Handle get requests for a single default-character, serialize said object

        Returns:
        Serialized dictionary to the client and a response of 200
        """

        damage_type = DefaultCharacter.objects.get(pk=pk)

        serializer = DefaultCharacterSerializer(damage_type)

        return Response(serializer.data, status=status.HTTP_200_OK)
