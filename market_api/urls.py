from django.contrib import admin
from django.urls import path
from .views import (MeleeWeaponView, WeaponDetailView, MagicWeaponView, RangedWeaponView, OffHandView, MountView, AllWeaponView, YourApiView)

urlpatterns = [
    path('api/weapons/', AllWeaponView.as_view()),
    path('api/weapons/melee/', MeleeWeaponView.as_view()),
    path('api/weapons/detail/<str:unique_name>', WeaponDetailView.as_view()),
    path('api/weapons/magic/', MagicWeaponView.as_view()),
    path('api/weapons/ranged/', RangedWeaponView.as_view()),
    path('api/equipments/offhand/', OffHandView.as_view()),
    path('api/mounts/mount/', MountView.as_view()),
    path('api/test/', YourApiView.as_view()),
]
