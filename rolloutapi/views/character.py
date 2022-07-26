"""View module for handling requests about game types"""


from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
import requests
from rolloutapi.models import Character
from rolloutapi.models.feat import Feat
from rolloutapi.serializers import CharacterSerializer


class CharacterView(ViewSet):
    def list(self, request):
        """Handle get requests for multiple weapons"""

        characters = Character.objects.all()

        serializer = CharacterSerializer(characters, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)