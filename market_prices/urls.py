from django.contrib import admin
from django.urls import path
from .views import MarketPricesView, MarketPricesListView

urlpatterns = [
    path('api/prices/', MarketPricesView.as_view()),
    path('api/prices/<str:ItemTypeId>', MarketPricesListView.as_view()),
]
