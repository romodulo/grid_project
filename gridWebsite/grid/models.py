from django.db import models

class Player(models.Model):
	name = models.CharField(max_length=10)

class Block(models.Model):
	time = models.CharField(max_length=10)


