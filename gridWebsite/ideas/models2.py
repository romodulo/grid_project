from django.db import models

class IdeaPlayers(models.Model):
	name = models.CharField(max_length=10, null=True)

class IdeaBookings(models.Model):
	player1 = models.ForeignKey(IdeaPlayers, null=True, on_delete=models.SET_NULL)
	guest1 = models.CharField(max_length=10, null=True)
