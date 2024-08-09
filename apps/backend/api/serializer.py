from rest_framework import serializers
from .models import agentModel

class agentModelSerializer(serializers.ModelSerializer):
	class Meta:
		model = agentModel
		# fields = [field.name for field in model._meta.fields]
		fields = ['id', 'name', 'realName', 'rank', 'attribute', 'fightingStyle', 'faction', 'moduleType', 'nameIcon', 'rankIcon', 'attributeIcon', 'fightingStyleIcon', 'factionIcon', 'moduleTypeIcon']
		# fields = ('id', 'name', 'realName', 'rank', 'attribute', 'fightingStyle', 'faction', 'moduleType', 'nameIcon', 'attributeIcon')
