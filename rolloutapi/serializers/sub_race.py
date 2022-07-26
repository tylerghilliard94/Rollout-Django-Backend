
from rest_framework import serializers
from rolloutapi.models.sub_race import SubRace
from rolloutapi.serializers.race import RaceSerializer
from rolloutapi.serializers.size import SizeSerializer


class SubRaceSerializer(serializers.ModelSerializer):

    base_race = RaceSerializer()
    size = SizeSerializer()

    class Meta:
        model = SubRace
        fields = ("id", "description", "base_race", "strength_bonus", "dexterity_bonus",
                  "constitution_bonus", "intelligence_bonus", "wisdom_bonus", "charisma_bonus",
                  "size", "able_to_choose_1", "choosable_stat_num_1", "able_to_choose_2",
                  "choosable_stat_num_2", "flight_capable", "speed", "flight_speed")
