from django.contrib import admin
from rolloutapi.models import Character
from rolloutapi.models.alignment import Alignment
from rolloutapi.models.armor import Armor
from rolloutapi.models.attribute import Attribute
from rolloutapi.models.character_class import CharacterClass
from rolloutapi.models.damage_type import DamageType
from rolloutapi.models.default_character import DefaultCharacter
from rolloutapi.models.feat import Feat
from rolloutapi.models.friend import Friend
from rolloutapi.models.item import Item
from rolloutapi.models.language import Language
from rolloutapi.models.magic_school import MagicSchool
from rolloutapi.models.money import Money
from rolloutapi.models.race import Race
from rolloutapi.models.rollout_user import RolloutUser
from rolloutapi.models.size import Size
from rolloutapi.models.skill import Skill
from rolloutapi.models.spell import Spell
from rolloutapi.models.sub_race import SubRace
from rolloutapi.models.weapon import Weapon
from rolloutapi.models.weapon_type import WeaponType

# Register your models here.
admin.site.register(Character)
admin.site.register(Alignment)
admin.site.register(Armor)
admin.site.register(Attribute)
admin.site.register(CharacterClass)
admin.site.register(DamageType)
admin.site.register(DefaultCharacter)
admin.site.register(Feat)
admin.site.register(Friend)
admin.site.register(Item)
admin.site.register(Language)
admin.site.register(MagicSchool)
admin.site.register(Money)
admin.site.register(Race)
admin.site.register(RolloutUser)
admin.site.register(Size)
admin.site.register(Skill)
admin.site.register(Spell)
admin.site.register(SubRace)
admin.site.register(WeaponType)
admin.site.register(Weapon)
