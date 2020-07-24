from django.urls import path

from . import views

urlpatterns = [
    path('shop/', views.shop_home ),
    path('shop/home', views.shop_home ),
]