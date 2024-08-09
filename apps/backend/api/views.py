from fastapi import HTTPException
from config.config import *
from models.agent import AgentModel

from main import app, agents

APP_DIR = "/api"


@app.post(APP_DIR+"/agents/", response_model=AgentModel)
def addAgent(agent: AgentModel):
	agents.append(agent)

	return agent

@app.get(APP_DIR+"/agents/", response_model=list[AgentModel])
def getAgents():
	return agents

@app.get(APP_DIR+"/agents/{agent_id}", response_model=AgentModel)
def getAgent(agent_id: int):
	for agent in agents:
		if agent.id == agent_id:
			print(agent.id)
			return agent

	return HTTPException(404, "Agent Not Found")