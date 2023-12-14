from django.contrib import admin
from django.urls import path
from .views import MarketPricesView, MarketPricesDetailView

urlpatterns = [
    path('api/prices/', MarketPricesView.as_view()),
    path('api/prices/<str:ItemTypeId>', MarketPricesDetailView.as_view()),
]
