from django.urls import path
from .views import *

urlpatterns = [
	path('updateform/', updateform_home),
	path('updateform/create', createOrder, name="createOrder"),
	path('updateform/update/<str:pk>', updateOrder, name="updateOrder"),
	path('browser/', browser),
	path('browser/update/<str:pk>', browserUpdate, name="browserUpdate"),
	path('simpleblog/', simple_blog, name="simpleblog"),
	path('calender', calender, name="calender")
]