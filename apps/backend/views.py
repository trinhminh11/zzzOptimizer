from fastapi import HTTPException
from config import *

from models import AgentModel, WEngineModel

from main import app, agents, wengines

# Agent
@app.get("/agents/", response_model=list[AgentModel])
def getAgents():
	return agents

@app.get("/agents/{agent_id}", response_model=AgentModel)
def getAgent(agent_id: int):
	for agent in agents:
		if agent.id == agent_id:
			return agent

	return HTTPException(404, "Agent Not Found")


# WEngine
@app.get("/wengines/", response_model=list[WEngineModel])
def getWEngines():
	return wengines

@app.get("/wengines/{wengine_id}", response_model=WEngineModel)
def getWEngine(wengine_id: int):
	for wengine in wengines:
		if wengine.id == wengine_id:
			return wengine

	return HTTPException(404, "W-Engine Not Found")