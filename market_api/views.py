from django.db.models import F
from .models import ItemDescriptionModel, WeaponModel, OffHandModel, MountModel
from .serializers import WeaponSerializer, OffHandSerializer, MountSerializer
import json
from rest_framework import generics

class AllWeaponView(generics.ListCreateAPIView):
    queryset = WeaponModel.objects.all()
    serializer_class = WeaponSerializer
class MeleeWeaponView(generics.ListCreateAPIView):
    queryset = WeaponModel.objects.filter(item_class = 'melee')
    serializer_class = WeaponSerializer
    
class MagicWeaponView(generics.ListCreateAPIView):
    queryset = WeaponModel.objects.filter(item_class = 'magic')
    serializer_class = WeaponSerializer

class RangedWeaponView(generics.ListCreateAPIView):
    queryset = WeaponModel.objects.filter(item_class = 'ranged')
    serializer_class = WeaponSerializer

class WeaponDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = WeaponModel.objects.all()
    serializer_class = WeaponSerializer
    lookup_field = 'unique_name'

class OffHandView(generics.ListCreateAPIView):
    queryset = OffHandModel.objects.filter(item_class = 'offhand')
    serializer_class = OffHandSerializer

class MountView(generics.ListCreateAPIView):
    queryset = MountModel.objects.filter(item_class = 'mount')
    serializer_class = MountSerializer