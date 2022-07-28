"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import action
import requests
from rolloutapi.models import Item
from rolloutapi.serializers import MultiItemSerializer, ItemSerializer


class ItemView(ViewSet):
    def list(self, request):
        """Handle get requests for multiple items, serialize said objects

        Returns:
        Serialized dictionaries in a list back to the client and a response of 200"""

        items = Item.objects.all()

        serializer = MultiItemSerializer(items, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk):
        """Handle get requests for a single item, serialize said object

        Returns:
        Serialized dictionary to the client and a response of 200
        """

        item = Item.objects.get(pk=pk)

        serializer = ItemSerializer(item)

        return Response(serializer.data, status=status.HTTP_200_OK)
