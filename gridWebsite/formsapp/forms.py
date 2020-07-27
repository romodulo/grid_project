from django.forms import ModelForm
from .models import Log

class LogForm(ModelForm):
	class Meta:
		model = Log
		fields = ['player_1', 'player_2', 'guest_1', 'guest_2', 'guest_3', 'guest_4']








# name = models.CharField(max_length=200)
# player1 = models.CharField(max_length=200, null=True)
# player2 = models.CharField(max_length=200, null=True)
# guest1 = models.CharField(max_length=200, null=True)
# guest2 = models.CharField(max_length=200, null=True)
# guest3 = models.CharField(max_length=200, null=True)
# guest4 = models.CharF