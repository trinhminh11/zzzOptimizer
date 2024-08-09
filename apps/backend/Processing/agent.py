import json		
import os
dirname = os.path.dirname(__file__)
baseStatFile = dirname + "/agentBaseStat.json"

class Agent:
	name: str
	realName: str
	rank: str
	mindScape: int = 0
	promotion: int = 0
	level: int = 1
	attribute: str
	fightingStyle: str
	faction: str
	moduleType: str

	hp: float = 0
	hp_: float = 0
	atk: float = 0
	atk_: float = 0
	_def: float = 0
	def_: float = 0
	imp: float = 0
	criRate_: float = 0
	criDmg_: float = 0
	anoMas: float = 0
	anoPro: float = 0
	pen: float = 0
	pen_: float = 0
	eneGen: float = 0
	eleDMG_: float = 0
	phyDMG_: float = 0
	firDMG_: float = 0
	iceDMG_: float = 0
	ethDMG_: float = 0

	atkBuff: float

	baseStatLevel: dict = {}
	baseStat: dict = {}

	core: int = 1
	basic: int = 1
	dogde: int = 1
	assist: int = 1
	special: int = 1
	chain: int = 1
	
	def __init__(self, name: str, realName: str, rank: str, attribute: str, fightingStyle: str, faction: str, moduleType: str):
			self.name = name
			self.realName = realName
			self.rank = rank
			self.attribute = attribute
			self.fightingStyle = fightingStyle
			self.faction = faction
			self.moduleType = moduleType

			self.calculationStat()
	
	def fromJson(self, data: dict):
		self.mindScape = data['mindScape']

		if self.mindScape < 0 or self.mindScape > 6:
			raise ValueError(f'Agent Mind Scape can only be from 0->6, got {self.mindScape} instead')

		self.promotion = data['promotion']
		self.level = data['level']

		if self.promotion < 0 or self.promotion > 6:
			raise ValueError(f"Agent promotion must be between 0 and 6, got {self.promotion} instead")

		if self.promotion == 0:
			min_level = 1
		else:
			min_level = self.promotion*10

		max_level = (self.promotion+1)*10

		if self.level < min_level or self.level > max_level:
			raise ValueError(f'with promotion {self.promotion}, level must be between {min_level} and {max_level}, got {self.level} instead')

		if self.level == min_level or self.level == max_level:
			stat_min = self.baseStatLevel[str(self.promotion)][str(self.level)]
			stat_max = self.baseStatLevel[str(self.promotion)][str(self.level)]
		else:
			stat_min = self.baseStatLevel[str(self.promotion)][str(min_level)]
			stat_max = self.baseStatLevel[str(self.promotion)][str(max_level)]

		self.baseStat['hp'] = (stat_min[0] + stat_max[0]) / 2
		self.baseStat['atk'] = (stat_min[1] + stat_max[1]) / 2
		self.baseStat['def'] = (stat_min[2] + stat_max[2]) / 2

		self.core = int(data['core'])
		self.basic = int(data['basic'])
		self.dogde = int(data['dogde'])
		self.assist = int(data['assist'])
		self.special = int(data['special'])
		self.chain = int(data['chain'])



	def loadBaseStat(self, data):
		self.baseStat = data

	def setLevel(self, value):
		self.level = value
		self.calculationStat()

	def calculationStat(self):
		raise NotImplementedError()

class Rina(Agent):
	def __init__(self):
		super().__init__("Rina", "Alexandrina Sebastiane", "S", "Electric", "Support", "Victoria Housekeeping", "Strike")

	def calculationStat(self):
		pass

class Anby(Agent):
	def __init__(self):
		super().__init__("Anby", "Anby Demara", "A", "Electric", "Stun", "Cunning Hares", "Slash")

	def calculationStat(self):
		pass

class Anton(Agent):
	def __init__(self):
		super().__init__("Anton", "Anton Ivanove", "A", "Electric", "Attack", "Belobog Heavy Industries", "Pierce")

	def calculationStat(self):
		pass

class Ben(Agent):
	def __init__(self):
		super().__init__("Ben", "Ben Bigger", "A", "Fire", "Defense", "Belobog Heavy Industries", "Strike")

	def calculationStat(self):
		pass

class Billy(Agent):
	def __init__(self):
		super().__init__("Billy", "Billy Kid", "A", "Physical", "Attack", "Cunning Hares", "Pierce")

	def calculationStat(self):
		pass

class Corin(Agent):
	def __init__(self):
		super().__init__("Corin", "Corin Wickes", "A", "Physical", "Attack", "Victoria Housekeeping", "Slash")

	def calculationStat(self):
		pass

class Ellen(Agent):
	def __init__(self):
		super().__init__("Ellen", "Ellen Joe", "S", "Ice", "Attack", "Victoria Housekeeping", "Slash")

	def calculationStat(self):
		pass

class Grace(Agent):
	def __init__(self):
		super().__init__("Grace", "Grace Howard", "S", "Electric", "Anomaly", "Belobog Heavy Industries", "Pierce")

	def calculationStat(self):
		pass

class Koleda(Agent):
	def __init__(self):
		super().__init__("Koleda", "Koleda Belobog", "S", "Fire", "Stun", "Belobog Heavy Industries", "Strike")

	def calculationStat(self):
		pass


class Lucy(Agent):
	def __init__(self):
		super().__init__("Lucy", "Luciana de Montefio", "A", "Fire", "Support", "Sons of Calydon", "Strike")

	def calculationStat(self):
		pass

class Nekomata(Agent):
	def __init__(self):
		super().__init__("Nekomata", "Nekomiya Mana", "S", "Physical", "Attack", "Cunning Hares", "Slash")

	def calculationStat(self):
		pass

class Nicole(Agent):
	def __init__(self):
		super().__init__("Nicole", "Nicole Demara", "A", "Ether", "Support", "Cunning Hares", "Strike")

	def calculationStat(self):
		pass

class Piper(Agent):
	def __init__(self):
		super().__init__("Piper", "Piper Wheel", "A", "Physical", "Anomaly", "Sons of Calydon", "Slash")

	def calculationStat(self):
		pass

class Soldier11(Agent):
	def __init__(self):
		super().__init__("Soldier11", "Soldier11", "S", "Fire", "Attack", "Obol Squad", "Slash")

	def calculationStat(self):
		pass

class Soukaku(Agent):
	def __init__(self):
		super().__init__("Soukaku", "Soukaku", "A", "Ice", "Support", "Section 6", "Slash")

	def calculationStat(self):
		pass

class Lycaon(Agent):
	def __init__(self):
		super().__init__("Lycaon", "Von Lycaon", "S", "Ice", "Stun", "Victoria Housekeeping", "Strike")

	def calculationStat(self):
		pass

class Yuan(Agent):
	def __init__(self):
		super().__init__("Yuan", "Zhu Yuan", "S", "Ether", "Attack", "Criminal Investigation Special Response Team", "Pierce")

	def calculationStat(self):
		pass


def load_agent():
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

