import json

with open("test.json", "r") as f:
	data = json.load(f)

agentList = []

for name in data:
	agentList.append(name)

for agent in agentList:
	print(f"\"{agent}\": {agent}(),")

