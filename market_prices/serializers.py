# serializers.py
from rest_framework import serializers
from .models import MarketPricesModel

class MarketPricesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarketPricesModel
        fields = '__all__'