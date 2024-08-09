from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from config.config import *
import uvicorn
from models.agent import AgentModel
import json
import api.views


from fastapi.staticfiles import StaticFiles




app = FastAPI()
app.mount("/media", StaticFiles(directory = MEDIA_DIR))

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

agents: list[AgentModel] = []

with open('agent.json', 'r') as f:
	agentsJSON = json.load(f)

for agent in agentsJSON:
	id = agent['id']
	name = agent['name']
	realName = agent['realName']
	rank = agent['rank']
	attribute = agent['attribute']
	fightingStyle = agent['fightingStyle']
	faction = agent['faction']
	moduleType = agent['moduleType']
	baseStat = agent['baseStat']

	agents.append(AgentModel(
		id = id, 
		name = name, 
		realName = realName, 
		rank = rank,
		attribute=attribute,
		fightingStyle=fightingStyle,
		faction = faction,
		moduleType = moduleType,
		baseStat = baseStat, 
		nameIcon = f'{BASE_DIR}/{MEDIA_DIR}/agents/{name}.png',
		rankIcon = f'{BASE_DIR}/{MEDIA_DIR}/rank/{rank}.png',
		attributeIcon = f'{BASE_DIR}/{MEDIA_DIR}/attributes/{attribute}.png',
		fightingStyleIcon = f'{BASE_DIR}/{MEDIA_DIR}/fightingStyle/{fightingStyle}.png',
		factionIcon = f'{BASE_DIR}/{MEDIA_DIR}/faction/{faction.replace(" ", "_")}.png',
		moduleTypeIcon = f'{BASE_DIR}/{MEDIA_DIR}/moduleType/{moduleType}.png',
	))


def main():
	uvicorn.run("main:app", host = host, port = port, reload=True)

if __name__ == "__main__":
	main()
