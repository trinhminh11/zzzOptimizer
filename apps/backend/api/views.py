from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect, JsonResponse
from .models import agentModel

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import agentModelSerializer

from Processing.agent import load_agent
from django.core import serializers

import json



# Create your views here.
class agentModelView(APIView):
	# queryset = agentModel.objects.all()
	# serializer_class = agentModelSerializer

	# def get_queryset(self):
	# 	if self.request.GET:
	# 		return agentModel.objects.filter(pk = self.request.GET['id'])
	# 	return agentModel.objects.all()

	def get(self, request: HttpRequest):

		if request.GET.get('id'):
			return Response(agentModel.objects.filter(pk = request.GET.get('id')).values()[0])

		agents = agentModel.objects.all()

		serializer = agentModelSerializer(agents, many=True)

		return Response(serializer.data)
	
	
	

def agentView(request: HttpRequest):

	agentModel.objects.all().delete()
	iconFolder = ""
	agents = load_agent()

	for agent in agents.values():
		new_agent = agentModel(
			name = agent.name, 
			realName = agent.realName,
			rank = agent.rank,
			attribute = agent.attribute,
			fightingStyle = agent.fightingStyle, 
			faction = agent.faction, 
			moduleType = agent.moduleType, 
			nameIcon = f'{iconFolder}/agents/{agent.name}.png',
			rankIcon = f'{iconFolder}/rank/{agent.rank}.png',
			attributeIcon = f'{iconFolder}/attributes/{agent.attribute}.png',
			fightingStyleIcon = f'{iconFolder}/fightingStyle/{agent.fightingStyle}.png',
			factionIcon = f'{iconFolder}/faction/{agent.faction.replace(" ", "_")}.png',
			moduleTypeIcon = f'{iconFolder}/moduleType/{agent.moduleType}.png',
			baseStat = agent.baseStat
		)

		new_agent.save()

	return agentModelView.as_view()(request)

# def optimize(request: HttpRequest):
# 	pass

# def optimize_(data: dict):
# 	agents = load_agent()
# 	agent = agents[data['name']]
# 	agent.fromJson(data)



def test(request: HttpRequest):

	print(request.GET.dict())

	return JsonResponse(request.GET.dict())