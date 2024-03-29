"""rollout URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from rolloutapi.views import (WeaponView,
                              DamageTypeView,
                              ArmorView,
                              DataCollectionView,
                              ItemView,
                              CharacterView,
                              SpellView,
                              login_user,
                              register_user,
                              SkillView)
from rolloutapi.views.default_characters import DefaultCharacterView


router = routers.DefaultRouter(trailing_slash=False)
router.register(r'weapons', WeaponView, 'weapon')
router.register(r'spells', SpellView, 'spell')
router.register(r'damage-types', DamageTypeView, 'damage-type')
router.register(r'armor', ArmorView, 'armor')
router.register(r'items', ItemView, 'item')
router.register(r'default-characters',
                DefaultCharacterView, 'default-character')
router.register(r'characters',
                CharacterView, 'character')
router.register(r'data-collection', DataCollectionView, 'data-collection')
router.register(r'skills', SkillView, 'skill')

urlpatterns = [
    path('register', register_user),
    path('login', login_user),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
