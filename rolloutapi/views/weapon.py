"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rolloutapi.models import Weapon, DamageType
from rest_framework.decorators import action
import requests


from rolloutapi.serializers import MultiWeaponSerializer, WeaponSerializer


class WeaponView(ViewSet):
    def list(self, request):
        """Handle get requests for multiple weapons, serialize said objects

        Returns:
        Serialized dictionaries in a list back to the client and a response of 200"""

        weapons = Weapon.objects.all()
        serializer = MultiWeaponSerializer(weapons, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk):
        """Handle get requests for a single weapon, serialize said object

        Returns:
        Serialized dictionary to the client and a response of 200
        """

        weapon = Weapon.objects.get(pk=pk)

        serializer = WeaponSerializer(weapon)

        return Response(serializer.data, status=status.HTTP_200_OK)
