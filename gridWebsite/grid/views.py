from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
	return render(request, 'grid/main-extended.html')

def home(request):
	return render(request, 'grid/home.html')

def simple(request):
	return render(request, 'grid/simple.html')

def products(request):
	return render(request, 'grid/products.html')