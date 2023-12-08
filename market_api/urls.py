from django.contrib import admin
from django.urls import path
from .views import WeaponView

urlpatterns = [
    path('api/weapon/', WeaponView.as_view(), name='weapon'),
]
