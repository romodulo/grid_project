from django.db import models

class Log(models.Model):
	name = models.CharField(max_length=200)

	def __str__(self):
		return "Log " + str(self.id)
