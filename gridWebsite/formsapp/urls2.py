from django.urls import path
from .views2 import *

urlpatterns = [
	path('formsapp/', formsapp),
	path('formsapp/create', createOrder, name="createOrder"),
	path('formsapp/update/', updateOrder, name="updateOrder"),
	
]