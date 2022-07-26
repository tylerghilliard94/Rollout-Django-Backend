"""View module for handling requests about game types"""


from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
import requests
from rolloutapi.models.default_character import DefaultCharacter
from rolloutapi.serializers import DefaultCharacterSerializer


class DefaultCharacterView(ViewSet):
    def list(self, request):
        """Handle get requests for multiple weapons"""

        default_characters = DefaultCharacter.objects.all()

        serializer = DefaultCharacterSerializer(default_characters, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
