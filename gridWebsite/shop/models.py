from django.db import models

class Court(models.Model):
	court_number = models.IntegerField()

	def __str__(self):
		return str(self.court_number)

class Time(models.Model):
	court_time = models.TimeField()

	def __str__(self):
		return str(self.court_time)

class Month(models.Model):
	name 		= models.CharField(max_length=10)
	month_date 	= models.DateField()

	def __str__(self):
		return str(self.month_date)

class Player(models.Model):
	name 		= models.CharField(max_length=20)
	
	def __str__(self):
		return self.name

class WhatsappNum(models.Model):
	number 		= models.IntegerField()
	name 		= models.ForeignKey(Player, on_delete=models.CASCADE)

	def __str__(self):
		return self.number

class Log(models.Model):
	court 		= models.ForeignKey(Court, on_delete=models.CASCADE)
	court_time 	= models.ForeignKey(Time, on_delete=models.CASCADE)
	player1 	= models.ForeignKey(Player, on_delete=models.CASCADE)
	month_date	= models.ForeignKey(Month, on_delete=models.CASCADE)
	guest		= models.CharField(max_length=10)
	log_created	= models.DateField(auto_now_add=True)

	def __str__(self):
		return str(self.log_created)