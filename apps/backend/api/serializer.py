from rest_framework import serializers
from .models import agentDatabase

class agentDatabaseSerializer(serializers.ModelSerializer):
	class Meta:
		model = agentDatabase
		fields = ('id', 'name', 'rank', 'fightingStyle', 'faction', 'moduleType', 'icon')
