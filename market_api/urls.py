from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('api/detail/<str:unique_name>', ItemDetailView.as_view()),
    path('api/weapons/', AllWeaponView.as_view()),
    path('api/weapons/melee/', MeleeView.as_view()),
    path('api/weapons/magic/', MagicView.as_view()),
    path('api/weapons/ranged/', RangedView.as_view()),
    path('api/equipments/offhands/', OffHandView.as_view()),
    path('api/equipments/armors/', ArmorView.as_view()),
    path('api/equipments/tools/', ToolView.as_view()),
    path('api/equipments/accessories/', AccessoryView.as_view()),
    path('api/mounts/mount/', MountView.as_view()),
    path('api/item/consumable/', ConsumeableView.as_view()),
    path('api/item/resources/', ResourceView.as_view()),
    path('api/item/skillbooks/', SkillBookView.as_view()),
]
