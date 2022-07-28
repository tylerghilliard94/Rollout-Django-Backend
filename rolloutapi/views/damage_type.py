"""View module for handling requests about game types"""

from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rolloutapi.models import DamageType
from rolloutapi.serializers import DamageTypeSerializer
from rest_framework.decorators import action


class DamageTypeView(ViewSet):
    def list(self, request):
        """Handle get requests for multiple DamageTypes, serialize said objects

        Returns:
        Serialized dictionaries in a list back to the client and a response of 200"""

        damage_types = DamageType.objects.all()

        serializer = DamageTypeSerializer(damage_types, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk):
        """Handle get requests for a single damage-type, serialize said object

        Returns:
        Serialized dictionary to the client and a response of 200
        """

        damage_type = DamageType.objects.get(pk=pk)

        serializer = DamageTypeSerializer(damage_type)

        return Response(serializer.data, status=status.HTTP_200_OK)
