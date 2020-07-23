from django.shortcuts import render

def dashboard(request):
	context = {}
	return render(request, 'shop/dashboard.html', context)
