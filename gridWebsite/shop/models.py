from django.db import models

class Court(models.Model):
	court_number = models.IntegerField()

class Time(models.Model):
	court_time = models.TimeField()

class Month(models.Model):
	name 		= models.CharField(max_length=10)
	month_date 	= models.DateField()

class Player(models.Model):
	name 		= models.CharField(max_length=10)

class Log(models.Model):
	court 		= models.ForeignKey(Court, on_delete=models.CASCADE)
	court_time 	= models.ForeignKey(Time, on_delete=models.CASCADE)
	player1 	= models.ForeignKey(Player, on_delete=models.CASCADE)
	month_date	= models.ForeignKey(Month, on_delete=models.CASCADE)
	guest		= models.CharField(max_length=10)