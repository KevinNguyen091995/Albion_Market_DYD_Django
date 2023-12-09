from django.contrib import admin
from django.urls import path
from .views import MeleeWeaponView, MagicWeaponView, RangedWeaponView, OffHandView, MountView, AllWeaponView

urlpatterns = [
    path('api/weapon/', AllWeaponView.as_view()),
    path('api/weapon/melee', MeleeWeaponView.as_view()),
    path('api/weapon/magic', MagicWeaponView.as_view()),
    path('api/weapon/ranged', RangedWeaponView.as_view()),
    path('api/equipment/offhand', OffHandView.as_view()),
    path('api/mounts/mount', MountView.as_view()),
]
