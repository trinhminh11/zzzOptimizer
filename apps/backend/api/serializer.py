from rest_framework import serializers
from .models import agentDatabase

class agentDatabaseSerializer(serializers.ModelSerializer):
	class Meta:
		model = agentDatabase
		fields = []
		for field in model._meta.fields:
			fields.append(field.name)
		# fields = ('id', 'name', 'realName', 'rank', 'attribute', 'fightingStyle', 'faction', 'moduleType', 'nameIcon', 'attributeIcon')
