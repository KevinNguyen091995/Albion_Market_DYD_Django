from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ItemDescriptionModel, WeaponModel
import json

class WeaponView(APIView):
    def get(self, request):
        return
