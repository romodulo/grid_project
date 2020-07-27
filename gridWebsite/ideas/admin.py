from django.contrib import admin
from .models import Log
from .models2 import IdeaBookings, IdeaPlayers

admin.site.register(Log)
admin.site.register(IdeaBookings)
admin.site.register(IdeaPlayers)