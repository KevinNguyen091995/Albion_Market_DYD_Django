from django.db import models
from market_api.models import ItemDescriptionModel

class MarketPricesModel(models.Model):
    ItemTypeId = models.CharField(max_length=100)
    ItemGroupTypeId = models.CharField(max_length=100)
    UnitPriceSilver = models.IntegerField()
    Tier = models.IntegerField()
    EnchantmentLevel = models.IntegerField()
    QualityLevel = models.IntegerField()
    last_updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"MarketData: {self.Id}"
    
    def get_item_name(self):
        try:
            item_description = ItemDescriptionModel.objects.get(unique_name=self.unique_name)
            return item_description.item_name
        
        except ItemDescriptionModel.DoesNotExist:
            return None