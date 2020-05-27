from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.weather_view, name='weather_view'),
    path('search/', views.search, name='search'),
]
