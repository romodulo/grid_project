from django.shortcuts import render
from .models import Log

def shop_home(request):
	obj = Log.objects.all()




	context = {"objects": obj}
	
	return render(request, 'shop/shop_home.html', context)