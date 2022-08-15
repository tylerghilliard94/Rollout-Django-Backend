"""View module for handling requests about game types"""


from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from django.core.exceptions import ValidationError
from rolloutapi.models import Character, SubRace, RolloutUser, Alignment, CharacterClass
from rolloutapi.serializers import CharacterSerializer, MultiCharacterSerializer, CreateCharacterSerializer


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

    def create(self, request):
        """Handle post requests for characters and validates incoming data

        Returns:
        Serialized dictionary to the client and a response of 201
        """

        character_class = CharacterClass.objects.get(
            pk=request.data["character_class"])
        race = SubRace.objects.get(pk=request.data["race"])
        alignment = Alignment.objects.get(pk=request.data["alignment"])
        rollout_user = RolloutUser.objects.get(user=request.auth.user)
        serializer = CreateCharacterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        character = serializer.save(race=race, alignment=alignment,
                                    rollout_user=rollout_user,
                                    character_class=character_class)

        character.skills.add(*request.data["skills"])
        character.languages.add(*request.data["languages"])

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        """Handle put requests for characters and validates incoming data

        Returns:
        None to the client and a response of 204
        """
        character = Character.objects.get(pk=pk)
        character_class = CharacterClass.objects.get(
            pk=request.data["character_class"])
        race = SubRace.objects.get(pk=request.data["race"])
        alignment = Alignment.objects.get(pk=request.data["alignment"])
        rollout_user = RolloutUser.objects.get(user=request.auth.user)
        serializer = CreateCharacterSerializer(character, data=request.data)
        serializer.is_valid(raise_exception=True)
        character = serializer.save(race=race, alignment=alignment,
                                    rollout_user=rollout_user,
                                    character_class=character_class)

        character.skills.add(*request.data["skills"])
        character.languages.add(*request.data["languages"])

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def delete(self, request, pk):
        """Handle delete quests for characters.

        Returns:
        None and a response of 204
        """

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
