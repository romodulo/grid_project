from django.db import models

class TennisPlayer(models.Model):
	name = models.CharField(max_length=200, null=True)

	def __str__(self):
		return self.name

class TimeBooked(models.Model):
	# make 48 categories
	# if 1 category is taken
	# do not allow Player to book under
	# this category
	name = models.CharField(max_length=200, null=True)

	def __str__(self):
		return self.name

class Booking(models.Model):
	booking_name = models.ForeignKey(TennisPlayer, null=True, on_delete=models.SET_NULL)
	booking_time = models.ForeignKey(TimeBooked, null=True, on_delete=models.SET_NULL)
	# I need a date created, time created (especially)

class Player(models.Model):
	name = models.CharField(max_length=10)

class Block(models.Model):
	time = models.CharField(max_length=10)


