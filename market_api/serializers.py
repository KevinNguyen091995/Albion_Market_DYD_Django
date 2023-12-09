from rest_framework import serializers
from .models import WeaponModel, ItemDescriptionModel, OffHandModel

class ItemDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemDescriptionModel
        fields = '__all__'

class WeaponSerializer(serializers.ModelSerializer):
    item_name = serializers.CharField(source='get_item_name', read_only=True)

    class Meta:
        model = WeaponModel
        fields = ['unique_name', 'item_name', 'tier', 'image_url', 'item_class', 'item_category']

class OffHandSerializer(serializers.ModelSerializer):
    item_name = serializers.CharField(source='get_item_name', read_only=True)

    class Meta:
        model = WeaponModel
        fields = ['unique_name', 'item_name', 'tier', 'image_url', 'item_class', 'item_category']

class MountSerializer(serializers.ModelSerializer):
    item_name = serializers.CharField(source='get_item_name', read_only=True)

    class Meta:
        model = WeaponModel
        fields = ['unique_name', 'item_name', 'tier', 'image_url', 'item_class', 'item_category']