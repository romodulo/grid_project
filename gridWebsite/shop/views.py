from django.shortcuts import render

def shop_home(request):

	context = {}
	return render(request, 'shop/shop_home.html', context)