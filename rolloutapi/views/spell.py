"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rolloutapi.models import Spell
from rolloutapi.serializers import SpellSerializer, MultiSpellSerializer


from rolloutapi.serializers import MultiWeaponSerializer, WeaponSerializer


class SpellView(ViewSet):
    def list(self, request):
        """Handle get requests for multiple spells, serialize said objects

        Returns:
        Serialized dictionaries in a list back to the client and a response of 200"""

        spells = Spell.objects.all()
        serializer = MultiSpellSerializer(spells, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk):
        """Handle get requests for a single spell, serialize said object

        Returns:
        Serialized dictionary to the client and a response of 200
        """

        spell = Spell.objects.get(pk=pk)

        serializer = SpellSerializer(spell)

        return Response(serializer.data, status=status.HTTP_200_OK)
