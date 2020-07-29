from django.forms import ModelForm
from .models import Log, LogPlayer

class LogForm(ModelForm):
	class Meta:
		model = Log
		fields = ['name']

class LogPlayerForm(ModelForm):
	class Meta:
		model = LogPlayer
		fields = ['player_1', 'player_2', 'guest_1', 'guest_2', 'guest_3', 'guest_4']