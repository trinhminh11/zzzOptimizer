from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .Processing import agent as Agent
from .models import agentDatabase

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import agentDatabaseSerializer

# Create your views here.
def init(request: HttpRequest):
	iconFolder = "uploads/agents/"
	agents = Agent.main()

	for agent in agents.values():
		new_agent = agentDatabase(
			name = agent.name, 
			rank = agent.rank, 
			fightingStyle = agent.fightingStyle, 
			faction = agent.faction, 
			moduleType = agent.moduleType, 
			icon = f'{iconFolder}{agent.name}.png'
		)

		new_agent.save()
	

	return HttpResponse("intialize")



class agentDatabaseView(generics.ListCreateAPIView):
	queryset = agentDatabase.objects.all()
	serializer_class = agentDatabaseSerializer

	# def get(self, request):
	# 	output = [{'name': output.name, 'rank': output.rank, 'fightingStyle': output.fightingStyle, 'faction': output.faction, 'moduleType': output.moduleType, 'icon': output.icon} 
	# 		for output in agentDatabase.objects.all()]
		
	# 	return Response(output)

	# def post(self, request):
	# 	serializer = agentDatabaseSerializer(data=request.data)
	# 	if serializer.is_valid(raise_exception=True):
	# 		serializer.save()
	# 		return Response(serializer.data)
