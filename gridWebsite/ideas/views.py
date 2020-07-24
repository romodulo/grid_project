from django.shortcuts import render
from .models import Log, SecondLog

def ideas_home(request):
	obj = Log.objects.all()
	t0600 = Log.objects.filter(pk__in=[1,2,3,4,5,6,7])
	t0630 = Log.objects.filter(pk__in=[8,9,10,11,12,13,14])
	t0700 = Log.objects.filter(pk__in=[15, 16, 17, 18, 19, 20, 21])
	t0730 = Log.objects.filter(pk__in=[22, 23, 24, 25, 26, 27, 28])
	t0800 = Log.objects.filter(pk__in=[29, 30, 31, 32, 33, 34, 35])
	t0830 = Log.objects.filter(pk__in=[36, 37, 38, 39, 40, 41, 42])
	t0900 = Log.objects.filter(pk__in=[43, 44, 45, 46, 47, 48, 49])
	t0930 = Log.objects.filter(pk__in=[50, 51, 52, 53, 54, 55, 56])
	t1000 = Log.objects.filter(pk__in=[57, 58, 59, 60, 61, 62, 63])
	t1030 = Log.objects.filter(pk__in=[64, 65, 66, 67, 68, 69, 70])
	t1100 = Log.objects.filter(pk__in=[71, 72, 73, 74, 75, 76, 77])
	t1130 = Log.objects.filter(pk__in=[78, 79, 80, 81, 82, 83, 84])
	t1200 = Log.objects.filter(pk__in=[85, 86, 87, 88, 89, 90, 91])
	t1230 = Log.objects.filter(pk__in=[92, 93, 94, 95, 96, 97, 98])
	t1300 = Log.objects.filter(pk__in=[99, 100, 101, 102, 103, 104, 105])
	t1330 = Log.objects.filter(pk__in=[106, 107, 108, 109, 110, 111, 112])
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
