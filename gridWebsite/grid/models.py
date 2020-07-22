from django.db import models

class TennisPlayer(models.Model):
	name = models.CharField(max_length=200, null=True)

	def __str__(self):
		return self.name

class TimeBooked(models.Model):
	name = models.CharField(max_length=200, null=True)

	def __str__(self):
		return self.name

class Booking(models.Model):
	booking_name = models.ForeignKey(TennisPlayer, null=True, on_delete=models.SET_NULL)
	booking_time = models.ForeignKey(TimeBooked, null=True, on_delete=models.SET_NULL)

