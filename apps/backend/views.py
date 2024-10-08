from config import *
from typing import Literal
import json
from pydantic import Field
from fastapi import HTTPException, Body
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse, Response, PlainTextResponse
import re


from models import AgentModel, WEngineModel, DriveDiscModel
from Processing import wengines, agents, drivediscs

from main import app

# Agent
agentModels: list[AgentModel] = []
for agent in agents.values():
	agentModels.append(AgentModel(
		name = agent.name, 
		realName = agent.realName, 
		rank = agent.rank,
		attribute = agent.attribute,
		specialty = agent.specialty,
		faction = agent.faction,
		attackType = agent.attackType,
	))
@app.get("/agents/", response_model=list[AgentModel])
def getAgents():
	return agentModels

# @app.get("/agent/{agent_name}", response_model=AgentModel)
# def getAgent(agent_name: str, promotion = 0, level = 1):
# 	for agent in agents:
# 		if agent.name == agent_name:
# 			return agent

# 	return HTTPException(404, "Agent Not Found")


# WEngine
wengineModels: list[WEngineModel] = []
for wengine in wengines.values():
	mainStat, subStat = wengine.getStat().values()
	passive = wengine.getPassive()['passive']
	wengineModels.append(WEngineModel(
		name = wengine.name,
		rank = wengine.rank,
		specialty= wengine.specialty,
		# nameIcon=f'{BASE_DIR}/{MEDIA_DIR}/wengines/' + re.sub('[^0-9a-zA-Z]+', '_', f'{wengine.name}').strip("_") + '.png',
		mainStat=mainStat,
		subStat=subStat,
		passive=passive
	))
@app.get("/wengines/", response_model=list[WEngineModel])
def getWEngines():
	return wengineModels


@app.get("/wengine-passive/{wengine_name}", responses={
    200: {
        "description": "Successful Response",
        "content": {
            "application/json": {
                "example": 
                    {
                        "passive": "string",
                    }
            }
        }
    },
    404: {"description": "W-Engine Not Found"}
})
def getWEnginePassive(wengine_name: str, upgrade: int = 1):
	if upgrade < 1 or upgrade > 5:
		return HTTPException(422, "upgrade must be in between [1, 5]")
	for name, wengine in wengines.items():
		if name == wengine_name:
			response = wengine.getPassive(upgrade) # type: ignore
			return response

	return HTTPException(404, "W-Engine Not Found")


@app.get("/wengine-stat/{wengine_name}", responses={
    200: {
        "description": "Successful Response",
        "content": {
            "application/json": {
                "example": 
                    {
                        "mainStat": [
							"string",
							"float"
						],
                        "subStat": [
							"string",
							"float"
						],
                    },
                
            }
        }
    },
    404: {"description": "W-Engine Not Found"}
})
def getWEngineStat(wengine_name: str, modification: int = 0, level: int = 0):
	if modification < 0 or modification > 5:
		return HTTPException(422, "modification must be in between [0, 5]")

	
	if level < modification*10 or level > (modification+1)*10:
		return HTTPException(422, f"with modification: {modification}, level must be in between [{modification*10}, {(modification+1)*10}]")

	for name, wengine in wengines.items():
		if name == wengine_name:
			stats = wengine.getStat(modification, level) # type: ignore
			return stats

	return HTTPException(404, "W-Engine Not Found")



# DriveDisc
driveDiscModels: list[DriveDiscModel] = []
for drivedisc in drivediscs.values():
	passive2 = drivedisc.getPassive(2)['passive']
	passive4 = drivedisc.getPassive(4)['passive']
	driveDiscModels.append(DriveDiscModel(
		name = drivedisc.name,
		passiveDescription2Pieces = passive2,
		passiveDescription4Pieces = passive4
	))
@app.get("/drivediscs/", response_model=list[DriveDiscModel])
def getDriveDiscs():
	return driveDiscModels

import Processing.driveDisc as dd

@app.get("/drivediscs/property", responses = {
	200: {
        "description": "Successful Response",
        "content": {
            "application/json": {
                "example": 
                    {
                        "initialNoSubStat": dd.initialNoSubStat,
						"availabelMainStats": dd.availabelMainStats,
						"mainStatIncrement": dd.mainStatIncrement,
						"subStatIncrement": dd.subStatIncrement,
						"incrementLevel": dd.incrementLevel,
						"levelCap": dd.levelCap
                    },
                
            }
        }
    },
    404: {"description": "W-Engine Not Found"}
})
def getDriveDiscProperty():
	return {
		"initialNoSubStat": dd.initialNoSubStat,
		"availabelMainStats": dd.availabelMainStats,
		'mainStatBase': dd.mainStatBase,
		"mainStatIncrement": dd.mainStatIncrement,
		"subStatIncrement": dd.subStatIncrement,
		"incrementLevel": dd.incrementLevel,
		"levelCap": dd.levelCap
	}