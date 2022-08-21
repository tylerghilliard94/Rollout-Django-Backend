from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from rolloutapi.models import Character, RolloutUser

from rolloutapi.views import CharacterView
from rolloutapi.serializers import MultiCharacterSerializer, CharacterSerializer, CreateCharacterSerializer


class CharacterTests(APITestCase):

    fixtures = ["initial_data"]

    def setUp(self):
        # Get the first rollout_user for use in the tests
        self.rollout_user = RolloutUser.objects.first()
        token = Token.objects.get(user=self.rollout_user.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {token.key}")

    def test_get_all_characters(self):
        url = "/characters"

        characters = Character.objects.all()

        response = self.client.get(url)

        self.assertEqual(status.HTTP_200_OK, response.status_code)

        expected = MultiCharacterSerializer(characters, many=True)

        self.assertEqual(expected.data, response.data)

    def test_get_single_character(self):

        character = Character.objects.first()

        url = f"/characters/{character.id}"

        response = self.client.get(url)

        self.assertEqual(status.HTTP_200_OK, response.status_code)

        expected = CharacterSerializer(character)

        self.assertEqual(expected.data, response.data)

    def test_get_current_users_characters(self):
        url = "/characters/current_user_characters"

        characters = Character.objects.filter(rollout_user=self.rollout_user)

        response = self.client.get(url)

        self.assertEqual(status.HTTP_200_OK, response.status_code)

        expected = MultiCharacterSerializer(characters, many=True)

        self.assertEqual(expected.data, response.data)

    def test_get_characters_by_user_id(self):

        url = f"/characters/{self.rollout_user.id}/characters_by_user_id"

        characters = Character.objects.filter(
            rollout_user_id=self.rollout_user.id)

        response = self.client.get(url)

        self.assertEqual(status.HTTP_200_OK, response.status_code)

        expected = MultiCharacterSerializer(characters, many=True)

        self.assertEqual(expected.data, response.data)

    def test_create_character(self):
        url = "/characters"

        character = {
            "character_name": "Grumble McDumble",
            "character_class": 1,
            "level": 1,
            "race": 26,
            "image": "test.url",
            "description": "A brutal aspiring dragon slayer dwarf.",
            "alignment": 6,
            "experience": 0,
            "strength": 19,
            "dexterity": 17,
            "constitution": 8,
            "intelligence": 20,
            "wisdom": 15,
            "charisma": 20,
            "hit_points": 10,
            "skills": [10, 5, 8],
            "languages": [2, 9]
        }

        response = self.client.post(url, character)

        self.assertEqual(status.HTTP_201_CREATED, response.status_code)

        new_character = Character.objects.last()

        expected = CreateCharacterSerializer(new_character)

        self.assertEqual(expected.data, response.data)

    def test_update_character(self):
        character = Character.objects.first()
        edited_character = {
            "id": 1,
            "character_name": "Grumble McDumble",
            "character_class": 1,
            "level": 1,
            "race": 26,
            "image": "test.url",
            "description": "A brutal aspiring dragon slayer dwarf.",
            "alignment": 6,
            "experience": 0,
            "strength": 19,
            "dexterity": 17,
            "constitution": 8,
            "intelligence": 20,
            "wisdom": 15,
            "charisma": 20,
            "hit_points": 10,
            "skills": [10, 5, 8],
            "languages": [2, 9]
        }
        url = f"/characters/{character.id}"

        response = self.client.put(url, edited_character)

        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)

        self.assertEqual(None, response.data)
        character.refresh_from_db()

        self.assertEqual(character.character_name,
                         edited_character["character_name"])

    def test_delete_character(self):
        character = Character.objects.first()
        url = f"/characters/{character.id}"

        response = self.client.delete(url)

        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)

        self.assertEqual(None, response.data)

        response = self.client.get(url)

        self.assertEqual(status.HTTP_404_NOT_FOUND, response.status_code)
