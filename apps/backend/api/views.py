from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from .models import agentModel

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import agentModelSerializer

from Processing.agent import load_agent


# Create your views here.
class agentModelView(generics.ListAPIView):
	queryset = agentModel.objects.all()
	serializer_class = agentModelSerializer

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
	print(request.method)
	print(request.body)
	return HttpResponse("Hello")