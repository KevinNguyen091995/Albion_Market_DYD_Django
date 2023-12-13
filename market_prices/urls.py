from django.contrib import admin
from django.urls import path
from .views import MarketPricesView

urlpatterns = [
    path('api/prices/', MarketPricesView.as_view()),
]
