from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *
from .forms import PlayerForm

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

def tutorial(request):
	return render(request, 'grid/tutorial.html')

def test(request):
	return render(request, 'grid/test.html')

def test2(request):
	return render(request, 'grid/test2.html')

def home(request):
	blocks = Block.objects.all()


	context = {"blocks": blocks}
	return render(request, 'grid/home.html', context)

def createOrder(request):

	form = PlayerForm()
	if request.method=="POST":
		print("Printing POST", request.POST)
		form = PlayerForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/home')

	context={'form': form}
	return render(request, 'grid/forms.html', context)