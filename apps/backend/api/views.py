from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from .Processing import agent as Agent
from .models import agentDatabase

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import agentDatabaseSerializer


# Create your views here.
class agentDatabaseView(generics.ListAPIView):
	queryset = agentDatabase.objects.all()
	serializer_class = agentDatabaseSerializer

def agentView(request: HttpRequest):

	print(request.body)

	agentDatabase.objects.all().delete()
	iconFolder = "agents/"
	agents = Agent.main()

	for agent in agents.values():
		new_agent = agentDatabase(
			name = agent.name, 
			realName = agent.realName,
			rank = agent.rank,
			attribute = agent.attribute,
			fightingStyle = agent.fightingStyle, 
			faction = agent.faction, 
			moduleType = agent.moduleType, 
			icon = f'{iconFolder}{agent.name}.png'
		)

		new_agent.save()

	return agentDatabaseView.as_view()(request)

def optimize(request: HttpRequest):
	pass

def optimize_(data: dict):
	agents = Agent.main()
	agent = agents[data['name']]
	agent.fromJson(data)

