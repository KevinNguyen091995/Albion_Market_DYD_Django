import requests
from .models import ItemModel
from .serializers import ItemSerializer
from rest_framework import generics

class AllWeaponView(generics.ListCreateAPIView):
    queryset = ItemModel.objects.all()
    serializer_class = ItemSerializer

class ItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ItemModel.objects.all()
    serializer_class = ItemSerializer
    lookup_field = 'unique_name'

class MeleeView(generics.ListCreateAPIView):
    queryset = ItemModel.objects.filter(item_class = 'melee')
    serializer_class = ItemSerializer
    
class MagicView(generics.ListCreateAPIView):
    queryset = ItemModel.objects.filter(item_class = 'magic')
    serializer_class = ItemSerializer

class RangedView(generics.ListCreateAPIView):
    queryset = ItemModel.objects.filter(item_class = 'ranged')
    serializer_class = ItemSerializer

class EquipmentView(generics.ListCreateAPIView):
    queryset = ItemModel.objects.filter(item_class = 'offhand')
    serializer_class = ItemSerializer

class MountView(generics.ListCreateAPIView):
    queryset = ItemModel.objects.filter(item_class = 'mounts')
    serializer_class = ItemSerializer

class ResourceView(generics.ListCreateAPIView):
    queryset = ItemModel.objects.filter(item_class = 'resources')
    serializer_class = ItemSerializer

class ConsumeableView(generics.ListCreateAPIView):
    queryset = ItemModel.objects.filter(item_class = 'consumables')
    serializer_class = ItemSerializer

class SkillBookView(generics.ListCreateAPIView):
    queryset = ItemModel.objects.filter(item_class = 'skillbooks')
    serializer_class = ItemSerializer

class AccessoryView(generics.ListCreateAPIView):
    queryset = ItemModel.objects.filter(item_class = 'accessories')
    serializer_class = ItemSerializer

class ArmorView(generics.ListCreateAPIView):
    queryset = ItemModel.objects.filter(item_class = 'armor')
    serializer_class = ItemSerializer

class ToolView(generics.ListCreateAPIView):
    queryset = ItemModel.objects.filter(item_class = 'tools')
    serializer_class = ItemSerializer

