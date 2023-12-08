from django.db import models

# Create your models here.
class WeaponModel(models.Model):
    unique_name = models.CharField(default="", max_length=100)
    tier = models.IntegerField()
    image_url = models.URLField(default=None)
    weapon_class = models.CharField(max_length=50)

    def __str__(self):
        return self.unique_name


class ItemDescriptionModel(models.Model):
    unique_name = models.CharField(default="", max_length=100)
    description = models.CharField(default="", max_length=400)

    def __str__(self):
        return self.unique_name