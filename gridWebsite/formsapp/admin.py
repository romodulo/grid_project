from django.contrib import admin
from .models import Log
from .models2 import *

admin.site.register(Log)
admin.site.register(Customer)
admin.site.register(Court)
admin.site.register(Time)
admin.site.register(CourtTime)
admin.site.register(Order)