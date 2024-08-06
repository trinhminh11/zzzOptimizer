from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .Processing import agent as Agent
from .models import agentDatabase

# Create your views here.
def main(request: HttpRequest):
	return HttpResponse("Hello World!")

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