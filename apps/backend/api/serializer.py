from rest_framework import serializers
from .models import agentDatabase

class agentDatabaseSerializer(serializers.ModelSerializer):
	class Meta:
		model = agentDatabase
		fields = ('id', 'name', 'realName', 'rank', 'attribute', 'fightingStyle', 'faction', 'moduleType', 'icon')
