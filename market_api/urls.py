from django.contrib import admin
from django.urls import path
from .views import MeleeWeaponView, MagicWeaponView, RangedWeaponView

urlpatterns = [
    path('api/weapon/melee', MeleeWeaponView.as_view()),
    path('api/weapon/magic', MagicWeaponView.as_view()),
    path('api/weapon/ranged', RangedWeaponView.as_view()),

]
