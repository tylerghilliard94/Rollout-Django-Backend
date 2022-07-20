"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rolloutapi.models import DamageType
from rest_framework.decorators import action
import requests


class DamageTypeView(ViewSet):
    def list(self, request):
        """Handle get requests for multiple weapons"""

    @action(methods=["get"], detail=False)
    def hit_dnd_5e_api(self, request):

        response = requests.get(
            f'https://www.dnd5eapi.co/api/damage-types').json()

        for damage_type in response["results"]:
            response_obj = requests.get(
                f'https://www.dnd5eapi.co{damage_type["url"]}').json()
            type = DamageType.objects.create(
                type=response_obj["name"],
                description=response_obj["desc"][0]
            )
