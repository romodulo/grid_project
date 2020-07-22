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

	bookings = times.bookings_set.all()
	bookings_count = bookings.count()
	# if there is something in bookings:
		# then print out this context = booking.something
		# ! print out the name possibly
		# ! yeah, that's right.
		# print out the name. 

		# can I include a new entry into the database?

		# there should be an update button.

		# update button is only visible to allowed users

		# login_required? users? ! yes.
	
	# else
		
		# print something else (the blank time)




	context = { "players":players, "times":times }

	return render(request, 'grid/home.html', context)

def createOrder(request):

	context = { }
	return render(request, 'grid/bookings_form.html', context)