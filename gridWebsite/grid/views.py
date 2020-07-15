from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
	return render(request, 'grid/main.html')

def home(request):
	return render(request, 'grid/products.html')