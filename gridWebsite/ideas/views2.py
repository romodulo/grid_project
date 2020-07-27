from django.shortcuts import render
from .models2 import IdeaBookings, IdeaPlayers
from .models import Log

def ideas_home2(request):
	obj = Log.objects.all()
	count = Log.objects.count()

	# Enter the number of courts
	number_of_courts = 7

	# Enter the number of slots
	number_of_slots = 38

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


	context = {'obj': obj, 'full_list': full_list, 'obj_list': obj_list, 'count': count, 'test_variable': test_variable}
	return render(request, 'ideas/ideas_home2.html', context)