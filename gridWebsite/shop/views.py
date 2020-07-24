from django.shortcuts import render
from .models import Log

# These are a work in progress:
def shop_home(request):
	obj = Log.objects.all()
	context = {"objects": obj}
	return render(request, 'shop/shop_home.html', context)


# Below are all my archives
def shop_home_v1(request):
	obj = Log.objects.all()
	context = {"objects": obj}
	return render(request, 'shop/shop_home_v1.html', context)