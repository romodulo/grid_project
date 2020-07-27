from django.urls import path
from . import views

urlpatterns = [
	path('updateform/', views.updateform_home),
]