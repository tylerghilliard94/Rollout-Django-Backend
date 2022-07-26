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
        """Handle get requests for multiple weapons"""

        damage_types = DamageType.objects.all()

        serializer = DamageTypeSerializer(damage_types, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
