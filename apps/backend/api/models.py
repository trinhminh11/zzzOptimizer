from django.db import models

# Create your models here.
class agentDatabase(models.Model):
	name = models.CharField(max_length=50, default="", unique=True)

	rank = models.CharField(max_length=1, default="S", unique=False, choices=(
		("S", "S"),
		("A", "A"),
		("B", "B")
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

	icon = models.ImageField(default="", upload_to ='uploads/agents/')