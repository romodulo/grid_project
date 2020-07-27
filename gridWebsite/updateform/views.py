from django.shortcuts import render
from .models import Log

def updateform_home(request):
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
	t1400 = Log.objects.filter(pk__in=[113, 114, 115, 116, 117, 118, 119])
	t1430 = Log.objects.filter(pk__in=[120, 121, 122, 123, 124, 125, 126])
	t1500 = Log.objects.filter(pk__in=[127, 128, 129, 130, 131, 132, 133])
	t1530 = Log.objects.filter(pk__in=[134, 135, 136, 137, 138, 139, 140])
	t1600 = Log.objects.filter(pk__in=[141, 142, 143, 144, 145, 146, 147])
	t1630 = Log.objects.filter(pk__in=[148, 149, 150, 151, 152, 153, 154])
	t1700 = Log.objects.filter(pk__in=[155, 156, 157, 158, 159, 160, 161])
	t1730 = Log.objects.filter(pk__in=[162, 163, 164, 165, 166, 167, 168])
	t1800 = Log.objects.filter(pk__in=[169, 170, 171, 172, 173, 174, 175])
	t1830 = Log.objects.filter(pk__in=[176, 177, 178, 179, 180, 181, 182])
	t1900 = Log.objects.filter(pk__in=[183, 184, 185, 186, 187, 188, 189])
	t1930 = Log.objects.filter(pk__in=[190, 191, 192, 193, 194, 195, 196])
	t2000 = Log.objects.filter(pk__in=[197, 198, 199, 200, 201, 202, 203])
	t2030 = Log.objects.filter(pk__in=[204, 205, 206, 207, 208, 209, 210])
	t2100 = Log.objects.filter(pk__in=[211, 212, 213, 214, 215, 216, 217])
	t2130 = Log.objects.filter(pk__in=[218, 219, 220, 221, 222, 223, 224])
	t2200 = Log.objects.filter(pk__in=[225, 226, 227, 228, 229, 230, 231])
	t2230 = Log.objects.filter(pk__in=[232, 233, 234, 235, 236, 237, 238])
	t2300 = Log.objects.filter(pk__in=[239, 240, 241, 242, 243, 244, 245])
	t2330 = Log.objects.filter(pk__in=[246, 247, 248, 249, 250, 251, 252])
	context = {
	"objects":obj, 
	"t0600":t0600, "t0630":t0630, "t0700":t0700, "t0730":t0730, 
	"t0800":t0800, "t0830":t0830, "t0900":t0900, "t0930":t0930,
	"t1000":t1000, "t1030":t1030, "t1100":t1100, "t1130":t1130, 
	"t1200":t1200, "t1230":t1230, "t1300":t1300, "t1330":t1330, 
	"t1400":t1400, "t1430":t1430, "t1500":t1500, "t1530":t1530,
	"t1600":t1600, "t1630":t1630, "t1700":t1700, "t1730":t1730, 
	"t1800":t1800, "t1830":t1830, "t1900":t1900, "t1930":t1930,
	"t2000":t2000, "t2030":t2030, "t2100":t2100, "t2130":t2130,
	"t2200":t2200, "t2230":t2230, "t2300":t2300, "t2330":t2330,
	}
	return render(request, "ideas/ideas_home.html", context)
