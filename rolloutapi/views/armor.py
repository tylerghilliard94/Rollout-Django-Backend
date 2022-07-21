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
