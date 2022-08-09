"""View module for handling requests about game types"""


from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
import requests
from rolloutapi.models import Character
from rolloutapi.models.feat import Feat
from rolloutapi.serializers import CharacterSerializer, MultiCharacterSerializer


class CharacterView(ViewSet):
    def list(self, request):
        """Handle get requests for multiple characters, serialize said objects

        Returns:
        Serialized dictionaries in a list back to the client and a response of 200
        """

        characters = Character.objects.all()

        serializer = MultiCharacterSerializer(characters, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk):
        """Handle get requests for a single characters, serialize said object

        Returns:
        Serialized dictionary to the client and a response of 200
        """

        character = Character.objects.get(pk=pk)

        serializer = CharacterSerializer(character)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):

        Character.objects.get(pk=pk).delete()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    @action(methods=["get"], detail=False)
    def current_user_characters(self, request):
        characters = Character.objects.filter(
            rollout_user__user=request.auth.user)
        serializer = MultiCharacterSerializer(characters, many=True)
        return Response(serializer.data)

    @action(methods=["get"], detail=True)
    def characters_by_user_id(self, request, pk):
        characters = Character.objects.filter(rollout_user__user_id=pk)
        serializer = MultiCharacterSerializer(characters, many=True)
        return Response(serializer.data)
