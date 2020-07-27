from django.urls import path
from .views2 import ideas_home2

urlpatterns = [
	path('ideas/newpage', ideas_home2),
]