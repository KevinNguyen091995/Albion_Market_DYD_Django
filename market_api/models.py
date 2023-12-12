from django.db import models

class ItemDescriptionModel(models.Model):
    unique_name = models.CharField(max_length=100, unique=True)
    item_name = models.CharField(max_length=400)

    def __str__(self):
        return self.unique_name
    
class WeaponModel(models.Model):
    unique_name = models.CharField(max_length=50, primary_key=True)
    tier = models.IntegerField()
    image_url = models.URLField(default=None)
    item_class = models.CharField(max_length=50)
    item_category = models.CharField(max_length=50, default=None)

    def __str__(self):
        return self.unique_name
    
    def get_item_name(self):
        try:
            item_description = ItemDescriptionModel.objects.get(unique_name=self.unique_name)
            return item_description.item_name
        
        except ItemDescriptionModel.DoesNotExist:
            return None
        
class OffHandModel(models.Model):
    unique_name = models.CharField(max_length=50)
    tier = models.IntegerField()
    image_url = models.URLField(default=None)
    item_class = models.CharField(max_length=50)
    item_category = models.CharField(max_length=50, default=None)

    def __str__(self):
        return self.unique_name
    
    def get_item_name(self):
        try:
            item_description = ItemDescriptionModel.objects.get(unique_name=self.unique_name)
            return item_description.item_name
        
        except ItemDescriptionModel.DoesNotExist:
            return None
        
class MountModel(models.Model):
    unique_name = models.CharField(max_length=50)
    tier = models.IntegerField()
    image_url = models.URLField(default=None)
    item_class = models.CharField(max_length=50)
    item_category = models.CharField(max_length=50, default=None)

    def __str__(self):
        return self.unique_name
    
    def get_item_name(self):
        try:
            item_description = ItemDescriptionModel.objects.get(unique_name=self.unique_name)
            return item_description.item_name
        
        except ItemDescriptionModel.DoesNotExist:
            return None