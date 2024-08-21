from Processing.wengine import wengines
import json


a = wengines['Deep Sea Visitor']

p = a.getPassive(2)
p = json.dumps(p, indent=4)
print(p)