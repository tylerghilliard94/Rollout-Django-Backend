"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rolloutapi.models import DamageType, Item, Armor, Weapon, WeaponType, Spell, MagicSchool, Attribute
from rest_framework.decorators import action
import requests
from rolloutapi.api_data import weapons, armor, items
from rolloutapi.models.character_class import CharacterClass
from rolloutapi.models.feat import Feat


class DataCollectionView(ViewSet):

    @action(methods=["get"], detail=False)
    def damage_types(self, request):
        """Skims data off DND5E api and constructs DamageType objects to be inserted into my own db

        Returns:
            None with a status of 204
        """
        DamageType.objects.all().delete()
        response = requests.get(
            f'https://www.dnd5eapi.co/api/damage-types').json()

        for damage_type in response["results"]:
            response_obj = requests.get(
                f'https://www.dnd5eapi.co{damage_type["url"]}').json()
            type = DamageType.objects.create(
                type=response_obj["name"],
                description=response_obj["desc"][0]
            )

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    @action(methods=["get"], detail=False)
    def weapons(self, request):
        """Skims data off DND5E api and constructs Weapon objects to be inserted into my own db

        Returns:
            None with a status of 204
        """
        Weapon.objects.all().delete()
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

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    @action(methods=["get"], detail=False)
    def armor(self, request):
        """Skims data off DND5E api and constructs Armor objects to be inserted into my own db

        Returns:
            None with a status of 204
        """
        Armor.objects.all().delete()
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

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    @action(methods=["get"], detail=False)
    def items(self, request):
        """Skims data off DND5E api and constructs Item objects to be inserted into my own db

        Returns:
            None with a status of 204
        """
        Item.objects.all().delete()

        for piece in items:

            response = requests.get(
                f'https://www.dnd5eapi.co{piece["url"]}').json()

            piece_obj = Item.objects.create(
                name=response["name"],
                description=response["description"] if "description" in response else "",
                cost_gp=response["cost"]["quantity"],
                weight=response["weight"] if "weight" in response else 0,
                custom=False

            )
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    @action(methods=["get"], detail=False)
    def spells(self, request):
        """Skims data off DND5E api and constructs Spell objects to be inserted into my own db

        Returns:
            None with a status of 204
        """
        Spell.objects.all().delete()

        spells = requests.get('https://www.dnd5eapi.co/api/spells').json()

        for spell in spells["results"]:
            damage_type = None
            dc_save = None
            description = ""

            response = requests.get(
                f'https://www.dnd5eapi.co{spell["url"]}').json()

            if "damage" in response:
                try:
                    damage_type = DamageType.objects.get(
                        type=response["damage"]["damage_type"]["name"])
                except:
                    damage_type = DamageType.objects.get(pk=14)
            else:
                damage_type = DamageType.objects.get(pk=14)

            if "dc" in response:
                dc_save = Attribute.objects.get(
                    abbr_name=response["dc"]["dc_type"]["name"])
            else:
                dc_save = Attribute.objects.get(
                    name="None")

            magic_school = MagicSchool.objects.get(
                name=response["school"]["name"])

            for desc in response["desc"]:
                description += f" {desc}"

            spell_obj = Spell.objects.create(
                name=response["name"],
                description=description if "desc" in response else "",
                range=response["range"],
                duration=response["duration"],
                school=magic_school,
                damage_type=damage_type,
                concentration=response["concentration"],
                ritual=response["ritual"],
                casting_time=response["casting_time"],
                level=response["level"],
                dc_save=dc_save,
                dc_success=response["dc"]["dc_success"] if "dc" in response else "NA",
                custom=False


            )

            for class_dict in response["classes"]:
                spell_obj.classes.add(
                    CharacterClass.objects.get(name=class_dict["name"]))

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    @action(methods=["get"], detail=False)
    def feats(self, request):
        """Skims data off DND5E api and constructs Feat objects to be inserted into my own db

        Returns:
            None with a status of 204
        """
        Feat.objects.all().delete()

        feats = requests.get('https://www.dnd5eapi.co/api/features').json()

        for feat in feats["results"]:

            description = ""

            response = requests.get(
                f'https://www.dnd5eapi.co{feat["url"]}').json()

            for desc in response["desc"]:
                description += f" {desc}"

            feat_obj = Feat.objects.create(
                name=response["name"],
                description=description if "desc" in response else "",
                level=response["level"],
                custom=False

            )

            feat_obj.classes.add(
                CharacterClass.objects.get(name=response["class"]["name"]))

        return Response(None, status=status.HTTP_204_NO_CONTENT)
