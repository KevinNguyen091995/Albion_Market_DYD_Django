from rest_framework import serializers
from .models import ItemModel, ItemDescriptionModel

class ItemDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemDescriptionModel
        fields = '__all__'

class ItemSerializer(serializers.ModelSerializer):
    item_name = serializers.CharField(source='get_item_name', read_only=True)

    class Meta:
        model = ItemModel
        fields = ['unique_name', 'item_name', 'tier', 'image_url', 'item_class', 'item_category']