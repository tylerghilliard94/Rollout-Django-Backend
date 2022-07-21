"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rolloutapi.models import Weapon, DamageType
from rest_framework.decorators import action
import requests

from rolloutapi.models.weapon_type import WeaponType


class WeaponView(ViewSet):
    def list(self, request):
        """Handle get requests for multiple weapons"""

        weapons = Weapon.objects.all()

    @action(methods=["get"], detail=False)
    def hit_dnd_5e_api(self, request):
        weapons = [{
            "name": "Club",
            "url": "/api/equipment/club"
        },
            {
            "name": "Dagger",
            "url": "/api/equipment/dagger"
        },
            {
            "name": "Greatclub",
            "url": "/api/equipment/greatclub"
        },
            {
            "name": "Handaxe",
            "url": "/api/equipment/handaxe"
        },
            {
            "name": "Javelin",
            "url": "/api/equipment/javelin"
        },
            {
            "name": "Light hammer",
            "url": "/api/equipment/light-hammer"
        },
            {
            "name": "Mace",
            "url": "/api/equipment/mace"
        },
            {
            "name": "Quarterstaff",
            "url": "/api/equipment/quarterstaff"
        },
            {
            "name": "Sickle",
            "url": "/api/equipment/sickle"
        },
            {
            "name": "Spear",
            "url": "/api/equipment/spear"
        },
            {
            "name": "Crossbow, light",
            "url": "/api/equipment/crossbow-light"
        },
            {
            "name": "Dart",
            "url": "/api/equipment/dart"
        },
            {
            "name": "Shortbow",
            "url": "/api/equipment/shortbow"
        },
            {
            "name": "Sling",
            "url": "/api/equipment/sling"
        },
            {
            "name": "Battleaxe",
            "url": "/api/equipment/battleaxe"
        },
            {
            "name": "Flail",
            "url": "/api/equipment/flail"
        },
            {
            "name": "Glaive",
            "url": "/api/equipment/glaive"
        },
            {
            "name": "Greataxe",
            "url": "/api/equipment/greataxe"
        },
            {
            "name": "Greatsword",
            "url": "/api/equipment/greatsword"
        },
            {
            "name": "Halberd",
            "url": "/api/equipment/halberd"
        },
            {
            "name": "Lance",
            "url": "/api/equipment/lance"
        },
            {
            "name": "Longsword",
            "url": "/api/equipment/longsword"
        },
            {
            "name": "Maul",
            "url": "/api/equipment/maul"
        },
            {
            "name": "Morningstar",
            "url": "/api/equipment/morningstar"
        },
            {
            "name": "Pike",
            "url": "/api/equipment/pike"
        },
            {
            "name": "Rapier",
            "url": "/api/equipment/rapier"
        },
            {
            "name": "Scimitar",
            "url": "/api/equipment/scimitar"
        },
            {
            "name": "Shortsword",
            "url": "/api/equipment/shortsword"
        },
            {
            "name": "Trident",
            "url": "/api/equipment/trident"
        },
            {
            "name": "War pick",
            "url": "/api/equipment/war-pick"
        },
            {
            "name": "Warhammer",
            "url": "/api/equipment/warhammer"
        },
            {
            "name": "Whip",
            "url": "/api/equipment/whip"
        },
            {
            "name": "Blowgun",
            "url": "/api/equipment/blowgun"
        },
            {
            "name": "Crossbow, hand",
            "url": "/api/equipment/crossbow-hand"
        },
            {
            "name": "Crossbow, heavy",
            "url": "/api/equipment/crossbow-heavy"
        },
            {
            "name": "Longbow",
            "url": "/api/equipment/longbow"
        }]
        for weapon in weapons:

            response = requests.get(
                f'https://www.dnd5eapi.co{weapon["url"]}').json()

            damage_type = DamageType.objects.get(
                type=response["damage"]["damage_type"]["name"])

            weapon_obj = Weapon.objects.create(
                name=response["name"],
                description=response["description"] if "description" in response else "",
                cost_gp=response["cost"]["quantity"],
                weight=response["weight"],
                weapon_type=WeaponType.objects.get(
                    name=response["weapon_category"]),
                range=response["range"]["normal"],
                damage=response["damage"]["damage_dice"],
                damage_type=damage_type,
                two_handed=True if "two_handed_damage" in response else False,
                two_handed_damage=response["two_handed_damage"]["damage_dice"] if "two_handed_damage" in response else "NA",
                ranged=True if response["weapon_range"] == "Ranged" else False,
                custom=False

            )
