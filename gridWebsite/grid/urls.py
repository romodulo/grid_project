from django.urls import path

from . import views

urlpatterns = [
    path('', index.home),
    path('home', views.home),
    path('simple/', views.simple),
    path('simpleweekly/', views.simpleweekly),
	path('simpleweeklygrid/', views.simpleweeklygrid),
	path('simplegrid/', views.simplegrid),
	path('grid4/', views.grid4),
	path('tutor/', views.tutor),
	path('test/', views.test),
	path('test2/', views.test2),
]