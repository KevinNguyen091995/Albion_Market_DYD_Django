from rest_framework import serializers
from .models import WeaponModel, ItemDescriptionModel

class ItemDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemDescriptionModel
        fields = '__all__'

class WeaponSerializer(serializers.ModelSerializer):
    item_name = serializers.CharField(source='get_description', read_only=True)

    class Meta:
        model = WeaponModel
        fields = '__all__'