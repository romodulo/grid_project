from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('home/', views.home),
    path('simple/', views.simple),
    path('products/', views.products),
]