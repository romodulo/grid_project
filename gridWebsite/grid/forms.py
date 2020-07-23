from django.forms import ModelForm

from .models import Block

class PlayerForm(ModelForm):
	class Meta:
		model = Block
		fields = ['player']


