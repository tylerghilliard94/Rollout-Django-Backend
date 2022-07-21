"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import action
import requests
from rolloutapi.models import Armor


class ArmorView(ViewSet):
    def list(self, request):
        """Handle get requests for multiple weapons"""

        armor = Armor.objects.all()

    @action(methods=["get"], detail=False)
    def hit_dnd_5e_api(self, request):
        armor = [{
            "name": "Padded",
            "url": "/api/equipment/padded-armor"
        },
            {
            "name": "Leather",
            "url": "/api/equipment/leather-armor"
        },
            {
            "name": "Studded Leather",
            "url": "/api/equipment/studded-leather-armor"
        },
            {
            "name": "Hide",
            "url": "/api/equipment/hide-armor"
        },
            {
            "name": "Chain Shirt",
            "url": "/api/equipment/chain-shirt"
        },
            {
            "name": "Scale Mail",
            "url": "/api/equipment/scale-mail"
        },
            {
            "name": "Breastplate",
            "url": "/api/equipment/breastplate"
        },
            {
            "name": "Half Plate",
            "url": "/api/equipment/half-plate-armor"
        },
            {
            "name": "Ring Mail",
            "url": "/api/equipment/ring-mail"
        },
            {
            "name": "Chain Mail",
            "url": "/api/equipment/chain-mail"
        },
            {
            "name": "Plate",
            "url": "/api/equipment/plate-armor"
        },
            {
            "name": "Shield",
            "url": "/api/equipment/shield"
        }]

        for piece in armor:

            response = requests.get(
                f'https://www.dnd5eapi.co{piece["url"]}').json()

            piece_obj = Armor.objects.create(
                name=response["name"],
                description=response["description"] if "description" in response else "",
                armor_class=response["armor_class"]["base"],
                cost_gp=response["cost"]["quantity"],
                str_minimum=response["str_minimum"],
                stealth_disadvantage=response["stealth_disadvantage"],
                weight=response["weight"],
                custom=False

            )
