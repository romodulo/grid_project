from django.db import models

class Log(models.Model):
	name = models.CharField(max_length=200)
	player_1 = models.CharField(max_length=200, null=True)
	player_2 = models.CharField(max_length=200, null=True)
	guest_1 = models.CharField(max_length=200, null=True)
	guest_2 = models.CharField(max_length=200, null=True)
	guest_3 = models.CharField(max_length=200, null=True)
	guest_4 = models.CharField(max_length=200, null=True)

	def __str__(self):
		return "Log " + str(self.id)

class SecondLog(models.Model):
	name = models.CharField(max_length=200)

	def __str__(self):
		return "Log " + str(self.id)





class HomeTest(models.Model):
	name = models.CharField(max_length=200)

	def __str__(self):
		return "Log " + str(self.id)
