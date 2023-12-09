from django.db.models import F
from .models import ItemDescriptionModel, WeaponModel
from .serializers import WeaponSerializer
from rest_framework import generics

class MeleeWeaponView(generics.ListCreateAPIView):
    queryset = WeaponModel.objects.filter(weapon_class = 'melee')
    serializer_class = WeaponSerializer

class MagicWeaponView(generics.ListCreateAPIView):
    queryset = WeaponModel.objects.filter(weapon_class = 'magic')
    serializer_class = WeaponSerializer

class RangedWeaponView(generics.ListCreateAPIView):
    queryset = WeaponModel.objects.filter(weapon_class = 'ranged')
    serializer_class = WeaponSerializer