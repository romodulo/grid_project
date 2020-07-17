from django.urls import path

from . import views

urlpatterns = [
    path('', views.home),
    path('simple/', views.simple),
    path('simpleweekly/', views.simpleweekly),
	path('simpleweeklygrid/', views.simpleweeklygrid),
	path('simplegrid/', views.simplegrid),
]