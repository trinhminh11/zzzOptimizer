from typing import Any
from django.db import models
from .Processing import agent as Agent

def auto_increment():
	largest = agentDatabase.objects.all().order_by('id').last()
	if not largest:
		return 1
	return largest.id + 1

# Create your models here.
class agentDatabase(models.Model):

	id = models.IntegerField(primary_key=True, default=auto_increment)

	name = models.CharField(max_length=50, default="", unique=True)

	realName = models.CharField(max_length=50, default="", unique=True)

	rank = models.CharField(max_length=1, default="S", unique=False, choices=(
		("S", "S"),
		("A", "A"),
		("B", "B")
	))

	attribute = models.CharField(max_length=20, default="", unique=False, choices=(
		('Physical', 'Physical'),
		('Electric', 'Electric'),
		('Fire', 'Fire'),
		('Ice', 'Ice'),
		('Ether', 'Ether')
	))
	
	fightingStyle = models.CharField(max_length=50, default="", unique=False, choices=(
		("Attack", "Attack"),
		("Stun", "Stun"),
		("Anomaly", "Anomaly"),
		("Support", "Support"),
		("Defense", "Defense")
	))
	faction = models.CharField(max_length=50, default="", unique=False, choices=(
		("Victoria Housekeeping", "Victoria Housekeeping"),
		("Belobog Heavy Industries", "Belobog Heavy Industries"),
		("Criminal Investigation Special Response Team", "Criminal Investigation Special Response Team"),
		("Cunning Hares", "Cunning Hares"),
		("Obol Squad", "Obol Squad"),
		("Section 6", "Section 6"),
		("Sons of Calydon", "Sons of Calydon")
	))

	moduleType = models.CharField(max_length=20, default="", unique=False, choices=(
		("Slash", "Slash"),
		("Pierce", "Pierce"),
		("Strike", "Strike")
	))

	icon = models.ImageField(default="", upload_to ='media/agents/')

	def __str__(self):
		return f'{self.name}'