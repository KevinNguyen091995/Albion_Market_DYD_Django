import requests

from .models import ItemDescriptionModel, WeaponModel, OffHandModel, MountModel
from .serializers import WeaponSerializer, OffHandSerializer, MountSerializer

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

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

class YourApiView(APIView):
    def get(self, request, *args, **kwargs):
        guild_id = "QLY0eIvEQNa3WJZ_tndijg"
        url = f"https://gameinfo.albiononline.com/api/gameinfo/guilds/{guild_id}/data"

        # Make the API call
        response = requests.get(url)

        # Process the response
        data = response.json() if response.status_code == 200 else {}
        return Response(data)