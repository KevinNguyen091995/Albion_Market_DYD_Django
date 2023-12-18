from django.db.models import Q
from .models import ItemModel
from .serializers import ItemSerializer
from rest_framework import generics

class AllWeaponView(generics.ListCreateAPIView):
    queryset = queryset = ItemModel.objects.filter(Q(item_category = 'melee') | Q(item_category = 'magic') | Q(item_category = 'ranged'))
    serializer_class = ItemSerializer

class ItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ItemModel.objects.all()
    serializer_class = ItemSerializer
    lookup_field = 'unique_name'

class MeleeView(generics.ListCreateAPIView):
    queryset = ItemModel.objects.filter(Q(item_category = 'melee') & Q(item_class = 'weapon'))
    serializer_class = ItemSerializer
    
class MagicView(generics.ListCreateAPIView):
    queryset = ItemModel.objects.filter(Q(item_category = 'magic') & Q(item_class = 'weapon'))
    serializer_class = ItemSerializer

class RangedView(generics.ListCreateAPIView):
    queryset = ItemModel.objects.filter(Q(item_category = 'ranged') & Q(item_class = 'weapon'))
    serializer_class = ItemSerializer

class OffHandView(generics.ListCreateAPIView):
    queryset = ItemModel.objects.filter(item_category = 'offhand')
    serializer_class = ItemSerializer

class MountView(generics.ListCreateAPIView):
    queryset = ItemModel.objects.filter(item_category = 'mounts')
    serializer_class = ItemSerializer

class ResourceView(generics.ListCreateAPIView):
    queryset = ItemModel.objects.filter(item_category = 'resources')
    serializer_class = ItemSerializer

class ConsumeableView(generics.ListCreateAPIView):
    queryset = ItemModel.objects.filter(item_category = 'consumables')
    serializer_class = ItemSerializer

class SkillBookView(generics.ListCreateAPIView):
    queryset = ItemModel.objects.filter(item_category = 'skillbooks')
    serializer_class = ItemSerializer

class AccessoryView(generics.ListCreateAPIView):
    queryset = ItemModel.objects.filter(item_category = 'accessories')
    serializer_class = ItemSerializer

class ArmorView(generics.ListCreateAPIView):
    queryset = ItemModel.objects.filter(item_category = 'armor')
    serializer_class = ItemSerializer

class ToolView(generics.ListCreateAPIView):
    queryset = ItemModel.objects.filter(item_category = 'tools')
    serializer_class = ItemSerializer

