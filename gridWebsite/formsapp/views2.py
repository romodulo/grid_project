from django.shortcuts import render, redirect
from .models2 import *
from .models import Log
from .forms import LogForm

def formsapp(request):

	obj = Log.objects.all()
	count = Log.objects.count()
	last = Log.objects.last()

	# Enter the number of courts
	number_of_courts = 7

	# Enter the number of slots
	number_of_slots = 36

	# 
	courts = number_of_courts
	slots = number_of_slots
	full_list = []
	counter = 0
	base = courts

	test_variable = None
	#safety-check
	cells = slots * courts
	if count < cells:
		slots = int(count/courts)
		test_variable = "Count < cells"

	for each in range(0, slots):
		t_list = []
		while counter < base:
			t_list.append(counter)
			counter += 1
		full_list.append(t_list)
		base += courts
	obj_list = []
	for each in full_list:
		abv_list = []
		for i in each:
			abv_list.append((obj[i].id, obj[i].name))
		obj_list.append(abv_list)


	context = {'obj': obj, 'full_list': full_list, 'obj_list': obj_list, 'count': count, 'test_variable': test_variable, 'last': last}
	return render(request, 'formsapp/formsapp.html', context)

def createOrder(request):

	form = LogForm()
	if request.method == "POST":
		print('Printing POST', request.POST)
		form = LogForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/formsapp')

	context = {'form': form}
	return render(request, 'formsapp/formsapp_create.html', context)

def updateOrder(request):

	form = LogForm()
	context = {'form': form}
	return render(request, 'formsapp/formsapp_create.html', context)