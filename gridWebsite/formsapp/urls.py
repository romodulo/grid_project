from django.urls import path
from . import views

urlpatterns = [
	path('ideas/', views.ideas_home),
	path('ideas/home', views.ideas_home),
	path('ideas/test', views.ideas_home_test),
	path('ideas/test/test', views.ideas_home_test_test),
]