from django.db import models

class Log(models.Model):
	name = models.CharField(max_length=200)

	def __str__(self):
		return "Log " + str(self.id)

class LogPlayer(models.Model):
	name = models.CharField(max_length=200)
	player_1 = models.CharField(max_length=200, blank = False, null=True)
	player_2 = models.CharField(max_length=200, blank = False, null=True)
	guest_1 = models.CharField(max_length=200, blank = True, null=False)
	guest_2 = models.CharField(max_length=200, blank = True, null=False)
	guest_3 = models.CharField(max_length=200, blank = True, null=False)
	guest_4 = models.CharField(max_length=200, blank = True, null=False)

	def __str__(self):
		return "Log " + str(self.id)
