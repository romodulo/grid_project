from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.

def index(request):
	return render(request, 'grid/index.html')

def simple(request):
	return render(request, 'grid/simple.html')

def simpleweekly(request):
	return render(request, 'grid/simple-weekly.html')

def simpleweeklygrid(request):
	return render(request, 'grid/simpleweeklygrid.html')

def simplegrid(request):
	return render(request, 'grid/simplegrid.html')

def grid4(request):
	return render(request, 'grid/grid4.html')

def tutor(request):
	return render(request, 'grid/tutorial.html')

def test(request):
	return render(request, 'grid/test.html')

def test2(request):
	return render(request, 'grid/test2.html')

def home(request):
	players = TennisPlayer.objects.all()
	times = TimeBooked.objects.all()
	context = { "players":players, "times":times }
	return render(request, 'grid/home.html', context)