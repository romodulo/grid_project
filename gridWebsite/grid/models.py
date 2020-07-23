from django.db import models

class Player(models.Model):
	name = models.CharField(max_length=10)
	phone = models.CharField(max_length=10, null=True, blank=True)

	def __str__(self):
		return self.name

class Time(models.Model):
	name = models.CharField(max_length=10)

	def __str__(self):
		return self.name

class Block(models.Model):
	time = models.ForeignKey(Time, on_delete=models.CASCADE)
	player = models.ForeignKey(Player, on_delete=models.CASCADE)

class Blog(models.Model):
	name = models.CharField(max_length=100)
	tagline = models.TextField()

	def __str__(self):
		return self.name

