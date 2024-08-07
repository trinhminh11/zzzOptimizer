import json		
import os
dirname = os.path.dirname(__file__)
baseStatFile = dirname + "/agentBaseStat.json"

class Agent:
	name: str
	realName: str
	rank: str
	promotion: int
	level: int
	attribute: str
	fightingStyle: str
	faction: str
	moduleType: str

	hp: float
	hp_: float
	atk: float
	atk_: float
	_def: float
	def_: float
	impact: float
	critRate_: float
	critDmg_: float
	anoMas: float
	anoPro: float
	pen: float
	pen_: float
	enerGen: float
	electricDMG_: float
	physicalDMG_: float
	fierDMG_: float
	iceDMG_: float
	etherDMG_: float

	baseStat: dict
	
	def __init__(self, name: str, realName: str, rank: str, promotion: int, level: int, attribute: str, fightingStyle: str, faction: str, moduleType: str):
			self.name = name
			self.realName = realName
			self.rank = rank
			self.promotion = promotion
			self.level = level
			self.attribute = attribute
			self.fightingStyle = fightingStyle
			self.faction = faction
			self.moduleType = moduleType

			self.calculationStat()

	def loadBaseStat(self, data):
		self.baseStat = data

	def setLevel(self, value):
		self.level = value
		self.calculationStat()

	def calculationStat(self):
		raise NotImplementedError()

class Rina(Agent):
	def __init__(self):
		super().__init__("Rina", "Alexandrina Sebastiane", "S", 0, 1, "Electric", "Support", "Victoria Housekeeping", "Strike")

	def calculationStat(self):
		pass

class Anby(Agent):
	def __init__(self):
		super().__init__("Anby", "Anby Demara", "A", 0, 1, "Electric", "Stun", "Cunning Hares", "Slash")

	def calculationStat(self):
		pass

class Anton(Agent):
	def __init__(self):
		super().__init__("Anton", "Anton Ivanove", "A", 0, 1, "Electric", "Attack", "Belobog Heavy Industries", "Pierce")

	def calculationStat(self):
		pass

class Ben(Agent):
	def __init__(self):
		super().__init__("Ben", "Ben Bigger", "A", 0, 1, "Fire", "Defense", "Belobog Heavy Industries", "Strike")

	def calculationStat(self):
		pass

class Billy(Agent):
	def __init__(self):
		super().__init__("Billy", "Billy Kid", "A", 0, 1, "Physical", "Attack", "Cunning Hares", "Pierce")

	def calculationStat(self):
		pass

class Corin(Agent):
	def __init__(self):
		super().__init__("Corin", "Corin Wickes", "A", 0, 1, "Physical", "Attack", "Victoria Housekeeping", "Slash")

	def calculationStat(self):
		pass

class Ellen(Agent):
	def __init__(self):
		super().__init__("Ellen", "Ellen Joe", "S", 0, 1, "Ice", "Attack", "Victoria Housekeeping", "Slash")

	def calculationStat(self):
		pass

class Grace(Agent):
	def __init__(self):
		super().__init__("Grace", "Grace Howard", "S", 0, 1, "Electric", "Anomaly", "Belobog Heavy Industries", "Pierce")

	def calculationStat(self):
		pass

class Koleda(Agent):
	def __init__(self):
		super().__init__("Koleda", "Koleda Belobog", "S", 0, 1, "Fire", "Stun", "Belobog Heavy Industries", "Strike")

	def calculationStat(self):
		pass


class Lucy(Agent):
	def __init__(self):
		super().__init__("Lucy", "Luciana de Montefio", "A", 0, 1, "Fire", "Support", "Sons of Calydon", "Strike")

	def calculationStat(self):
		pass

class Nekomata(Agent):
	def __init__(self):
		super().__init__("Nekomata", "Nekomiya Mana", "S", 0, 1, "Physical", "Attack", "Cunning Hares", "Slash")

	def calculationStat(self):
		pass

class Nicole(Agent):
	def __init__(self):
		super().__init__("Nicole", "Nicole Demara", "A", 0, 1, "Ether", "Support", "Cunning Hares", "Strike")

	def calculationStat(self):
		pass

class Piper(Agent):
	def __init__(self):
		super().__init__("Piper", "Piper Wheel", "A", 0, 1, "Physical", "Anomaly", "Sons of Calydon", "Slash")

	def calculationStat(self):
		pass

class Soldier11(Agent):
	def __init__(self):
		super().__init__("Soldier11", "Soldier11", "S", 0, 1, "Fire", "Attack", "Obol Squad", "Slash")

	def calculationStat(self):
		pass

class Soukaku(Agent):
	def __init__(self):
		super().__init__("Soukaku", "Soukaku", "A", 0, 1, "Ice", "Support", "Section 6", "Slash")

	def calculationStat(self):
		pass

class Lycaon(Agent):
	def __init__(self):
		super().__init__("Lycaon", "Von Lycaon", "S", 0, 1, "Ice", "Stun", "Victoria Housekeeping", "Strike")

	def calculationStat(self):
		pass

class Yuan(Agent):
	def __init__(self):
		super().__init__("Yuan", "Zhu Yuan", "S", 0, 1, "Ether", "Attack", "Criminal Investigation Special Response Team", "Pierce")

	def calculationStat(self):
		pass


def main():
	agents: dict[str, Agent] = {
		"Rina": Rina(),
		"Anby": Anby(),
		"Anton": Anton(),
		"Ben": Ben(),
		"Billy": Billy(),
		"Corin": Corin(),
		"Ellen": Ellen(),
		"Grace": Grace(),
		"Koleda": Koleda(),
		"Lucy": Lucy(),
		"Nekomata": Nekomata(),
		"Nicole": Nicole(),
		"Piper": Piper(),
		"Soldier11": Soldier11(),
		"Soukaku": Soukaku(),
		"Lycaon": Lycaon(),
		"Yuan": Yuan(),
	}

	with open(baseStatFile, "r") as f:
		data = json.load(f)
	
	for name, stat in data.items():
		agents[name].loadBaseStat(stat)

	return agents

