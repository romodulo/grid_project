from django.shortcuts import render
from .models import Log, SecondLog

def ideas_home(request):
	obj = Log.objects.all()
	t0600 = Log.objects.filter(pk__in=[1,2,3,4,5,6,7])
	t0630 = Log.objects.filter(pk__in=[8,9,10,11,12,13,14])
	t0700 = Log.objects.filter(pk__in=[8,9,10,11,12,13,14])
	t0730 = Log.objects.filter(pk__in=[8,9,10,11,12,13,14])
	t0800 = Log.objects.filter(pk__in=[8,9,10,11,12,13,14])
	t0830 = Log.objects.filter(pk__in=[8,9,10,11,12,13,14])
	t0900 = Log.objects.filter(pk__in=[8,9,10,11,12,13,14])
	t0930 = Log.objects.filter(pk__in=[8,9,10,11,12,13,14])
	t1000 = Log.objects.filter(pk__in=[8,9,10,11,12,13,14])
	t1030 = Log.objects.filter(pk__in=[8,9,10,11,12,13,14])
	t1100 = Log.objects.filter(pk__in=[8,9,10,11,12,13,14])
	t1130 = Log.objects.filter(pk__in=[8,9,10,11,12,13,14])
	t1200 = Log.objects.filter(pk__in=[8,9,10,11,12,13,14])
	t1230 = Log.objects.filter(pk__in=[8,9,10,11,12,13,14])
	t1300 = Log.objects.filter(pk__in=[8,9,10,11,12,13,14])
	t1330 = Log.objects.filter(pk__in=[8,9,10,11,12,13,14])
	context = {
	"objects":obj, "t0600":t0600, "t0630":t0630,
	"t0700":t0700, "t0730":t0730, "t0800":t0800,
	"t0830":t0830, "t0900":t0900, "t0930":t0930,
	"t1000":t1000, "t1100":t1100, "t1130":t1130,
	"t1200":t1200, "t1300":t1300, "t1330":t1330,
	}
	return render(request, "ideas/ideas_home.html", context)

def ideas_home_test(request):
	obj = HomeTest.objects.all()
	context = {"objects":obj}
	return render(request, "ideas/ideas_home_test.html", context)
