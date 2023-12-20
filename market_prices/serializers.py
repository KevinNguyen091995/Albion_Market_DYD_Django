# serializers.py
from rest_framework import serializers
from .models import MarketPricesModel

class MarketPricesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarketPricesModel
        fields = ['ItemTypeId', 'ItemGroupTypeId', 'Tier', 'EnchantmentLevel', 'QualityLevel', 'Location', 'UnitPriceSilver', 'last_updated']