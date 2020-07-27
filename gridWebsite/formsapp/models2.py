from django.db import models

# Customer Model
class Customer(models.Model):
	name = models.CharField(max_length=10, null=True)
	def __str__(self):
		return self.name
# Court Model
class Court(models.Model):
	name = models.CharField(max_length=10, null=True)
	def __str__(self):
		return self.name
# Time Model
class Time(models.Model):
	time = models.CharField(max_length=10, null=True)
	def __str__(self):
		return self.time
# COURT AND TIME
class CourtTime(models.Model):
	time = models.ForeignKey(Time, null=True, on_delete=models.SET_NULL)
	court = models.ForeignKey(Court, null=True, on_delete=models.SET_NULL)
	def __str__(self):
		return str(self.court) + " - " + str(self.time)
# ORDER
class Order(models.Model):
	player1 = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
	book = models.OneToOneField(CourtTime, null=True, on_delete=models.SET_NULL)
	player2 = models.CharField(max_length=10,blank=True, null=True)
	guest1 = models.CharField(max_length=10,blank=True, null=True)
	guest2 = models.CharField(max_length=10,blank=True, null=True)
	guest3 = models.CharField(max_length=10,blank=True, null=True)
	guest4 = models.CharField(max_length=10,blank=True, null=True)

# JUST 


