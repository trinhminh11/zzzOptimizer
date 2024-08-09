import json
from pyperclip import copy


with open("agent.json", 'r') as f:
	data = json.load(f)

with open("Processing/agentBaseStat.json", 'r') as f:
	stats = json.load(f)


real_data: list[dict] = []

keys = ['pk', 'name', 'realName', 'rank', 'attribute', 'fightingStyle', 'faction', 'moduleType']

for i in range(len(data)):
	real_data.append({})
	
	for key in keys:
		real_data[i][key] = data[i][key]
	
	real_data[i]['baseStat'] = stats[real_data[i]['name']]


with open('agent2.json', 'w') as f:
	json.dump(real_data, f)