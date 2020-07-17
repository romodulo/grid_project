from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
	return render(request, 'grid/home.html')

def simple(request):
	return render(request, 'grid/simple.html')

def simpleweekly(request):
	return render(request, 'grid/simple-weekly.html')