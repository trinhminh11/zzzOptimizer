from fastapi import HTTPException
from config import *

from models import AgentModel, WEngineModel

from main import app, agents, wengines

# Agent
@app.get("/agents/", response_model=list[AgentModel])
def getAgents():
	return agents

@app.get("/agent/{agent_name}", response_model=AgentModel)
def getAgent(agent_name: str, promotion = 0, level = 1):
	for agent in agents:
		if agent.name == agent_name:
			return agent

	return HTTPException(404, "Agent Not Found")


# WEngine
@app.get("/wengines/", response_model=list[WEngineModel])
def getWEngines():
	return wengines

@app.get("/wengines/{wengine_name}", response_model=WEngineModel)
def getWEngine(wengine_name: str):
	for wengine in wengines:
		if wengine.name == wengine_name:
			return wengine
	

	return HTTPException(404, "W-Engine Not Found")