from django.db.models import Q
import json
from .models import ItemModel
from .serializers import ItemSerializer
from rest_framework import generics
from django.db.utils import IntegrityError, DataError

data_categories = ['weapon', 'mount', 'equipmentitem', 'consumableitem', 'consumablefrominventoryitem', 'simpleitem', 'trackingitem' 'farmableitem', 'hideoutitem']

def put_item_db():
    with open('assets/items.json', 'r') as f:
        weapon = json.load(f)
        
        for data in weapon['items']:
            if data in data_categories:
                for item in weapon['items'][data]:
                    if (type(item)) == dict:
                        try:
                            print(item['@uniquename'])
                            ItemModel.objects.create(unique_name=item['@uniquename'], 
                                                    tier=item['@tier'], 
                                                    image_url=f"https://render.albiononline.com/v1/item/{item['@uniquename']}", 
                                                    item_class=data.replace('item', ""), 
                                                    item_category=item['@shopcategory'],
                                                    item_sub_category = item['@shopsubcategory1'])
                        except (IntegrityError, DataError):
                            pass
                                        
                
put_item_db()

class AllItemView(generics.ListCreateAPIView):
    queryset = queryset = ItemModel.objects.all()
    serializer_class = ItemSerializer

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

