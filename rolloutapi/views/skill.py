"""View module for handling requests about game types"""

from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action

from rolloutapi.models import Skill, Attribute
from rolloutapi.serializers import SkillSerializer


class SkillView(ViewSet):

    @action(methods=["get"], detail=False)
    def get_all_skills_sorted_by_attribute(self, request):
        """Handles get requests for skills and sorts them into separate lists by attribute

        Returns:
        Serialized dictionaries in a list back to the client and a response of 200
        """
        skills_dict = {}

        attributes = Attribute.objects.all()

        for attribute in attributes:
            skills_dict[attribute.name] = SkillSerializer(
                Skill.objects.filter(attribute=attribute), many=True).data

        return Response(skills_dict, status=status.HTTP_200_OK)
