from django.urls import path

from . import views

urlpatterns = [
    path('shop/', views.shop_home ),
    path('shop/home', views.shop_home ),
    path('shop/home/v1', views.shop_home_v1 ),
]