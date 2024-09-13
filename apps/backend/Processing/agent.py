import config
from typing import Literal, Type
from copy import deepcopy

baseStatLevelTemplate: dict[int, dict[int, dict[str, float]]] = { # type: ignore
	0: {
		1: {
			"hp": None,
			"atk": None,
			"def": None,
			"anomalyProficiency": None,
			"anomalyMastery": None,
			"impact": None,
			"critRate_": 5,
			"critDMG_": 50,
			"pen": 0,
			"pen_": 0,
			"energyRegen": 1.2
		},
		10: {
			"hp": None,
			"atk": None,
			"def": None,
			"anomalyProficiency": None,
			"anomalyMastery": None,
			"impact": None,
			"critRate_": 5,
			"critDMG_": 50,
			"pen": 0,
			"pen_": 0,
			"energyRegen": 1.2
		}
	},
	1: {
		10: {
			"hp": None,
			"atk": None,
			"def": None,
			"anomalyProficiency": None,
			"anomalyMastery": None,
			"impact": None,
			"critRate_": 5,
			"critDMG_": 50,
			"pen": 0,
			"pen_": 0,
			"energyRegen": 1.2
		},
		20: {
			"hp": None,
			"atk": None,
			"def": None,
			"anomalyProficiency": None,
			"anomalyMastery": None,
			"impact": None,
			"critRate_": 5,
			"critDMG_": 50,
			"pen": 0,
			"pen_": 0,
			"energyRegen": 1.2
		}
	},
	2: {
		20: {
			"hp": None,
			"atk": None,
			"def": None,
			"anomalyProficiency": None,
			"anomalyMastery": None,
			"impact": None,
			"critRate_": 5,
			"critDMG_": 50,
			"pen": 0,
			"pen_": 0,
			"energyRegen": 1.2
		},
		30: {
			"hp": None,
			"atk": None,
			"def": None,
			"anomalyProficiency": None,
			"anomalyMastery": None,
			"impact": None,
			"critRate_": 5,
			"critDMG_": 50,
			"pen": 0,
			"pen_": 0,
			"energyRegen": 1.2
		}
	},
	3: {
		30: {
			"hp": None,
			"atk": None,
			"def": None,
			"anomalyProficiency": None,
			"anomalyMastery": None,
			"impact": None,
			"critRate_": 5,
			"critDMG_": 50,
			"pen": 0,
			"pen_": 0,
			"energyRegen": 1.2
		},
		40: {
			"hp": None,
			"atk": None,
			"def": None,
			"anomalyProficiency": None,
			"anomalyMastery": None,
			"impact": None,
			"critRate_": 5,
			"critDMG_": 50,
			"pen": 0,
			"pen_": 0,
			"energyRegen": 1.2
		}
	},
	4: {
		40: {
			"hp": None,
			"atk": None,
			"def": None,
			"anomalyProficiency": None,
			"anomalyMastery": None,
			"impact": None,
			"critRate_": 5,
			"critDMG_": 50,
			"pen": 0,
			"pen_": 0,
			"energyRegen": 1.2
		},
		50: {
			"hp": None,
			"atk": None,
			"def": None,
			"anomalyProficiency": None,
			"anomalyMastery": None,
			"impact": None,
			"critRate_": 5,
			"critDMG_": 50,
			"pen": 0,
			"pen_": 0,
			"energyRegen": 1.2
		}
	},
	5: {
		50: {
			"hp": None,
			"atk": None,
			"def": None,
			"anomalyProficiency": None,
			"anomalyMastery": None,
			"impact": None,
			"critRate_": 5,
			"critDMG_": 50,
			"pen": 0,
			"pen_": 0,
			"energyRegen": 1.2
		},
		60: {
			"hp": None,
			"atk": None,
			"def": None,
			"anomalyProficiency": None,
			"anomalyMastery": None,
			"impact": None,
			"critRate_": 5,
			"critDMG_": 50,
			"pen": 0,
			"pen_": 0,
			"energyRegen": 1.2
		}
	},
}

class Agent:
	name: str
	realName: str
	rank: config.RANKS
	attribute: config.ATTRIBUTES
	specialty: config.SPECIALTY
	faction: config.FACTIONS
	attackType: config.ATTACKTYPE

	baseStatLevel: dict[int, dict[int, dict[str, float]]]

	mindScape: Literal[0, 1, 2, 3, 4, 5, 6]
	promotion: Literal[0, 1, 2, 3, 4, 5]
	level: int


	core: int
	basic: int
	dogde: int
	assist: int
	special: int
	chain: int
	
	def __init__(self):
		self.mindScape = 0
		self.promotion = 0
		self.level = 1
		
		
		self.core = 1
		self.basic = 1
		self.dodge = 1
		self.assist = 1
		self.special = 1
		self.chain = 1

	@property
	def baseStat(self):
		res: dict[str, float] = {}
		if self.promotion == 0:
			min_level = 1
		else:
			min_level = self.promotion*10

		max_level = (self.promotion+1)*10

		if self.level < min_level or self.level > max_level:
			raise ValueError(f'with promotion {self.promotion}, level must be between {min_level} and {max_level}, got {self.level} instead')

		if self.level == min_level or self.level == max_level:
			stat_min = self.baseStatLevel[self.promotion][self.level]
			stat_max = self.baseStatLevel[self.promotion][self.level]
		else:
			stat_min = self.baseStatLevel[self.promotion][min_level]
			stat_max = self.baseStatLevel[self.promotion][max_level]

		for stat, value in self.baseStatLevel[self.promotion][self.level].items():
			res[stat] = value

		res['hp'] = (stat_min['hp'] + stat_max['hp']) / 2
		res['atk'] = (stat_min['atk'] + stat_max['atk']) / 2
		res['def'] = (stat_min['def'] + stat_max['def']) / 2

		return res
	
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

		self.core = int(data['core'])
		self.basic = int(data['basic'])
		self.dogde = int(data['dogde'])
		self.assist = int(data['assist'])
		self.special = int(data['special'])
		self.chain = int(data['chain'])

	def setLevel(self, value):
		self.level = value
		self.calculationStat()

	def calculationStat(self):
		raise NotImplementedError()

class Rina(Agent):
	name = "Rina"
	realName = "Alexandrina Sebastiane"
	rank = "S"
	attribute = "Electric"
	specialty = "Support"
	faction = "Victoria Housekeeping"
	attackType = "Strike"
	baseStatLevel = deepcopy(baseStatLevelTemplate)

	baseStatLevel[0][1]['hp'], baseStatLevel[0][1]['atk'], baseStatLevel[0][1]['def'], baseStatLevel[0][1]['anomalyProficiency'], baseStatLevel[0][1]['anomalyMastery'], baseStatLevel[0][1]['impact'] = (692, 103, 48, 93, 92, 83)
	baseStatLevel[0][10]['hp'], baseStatLevel[0][10]['atk'], baseStatLevel[0][10]['def'], baseStatLevel[0][10]['anomalyProficiency'], baseStatLevel[0][10]['anomalyMastery'], baseStatLevel[0][10]['impact'] = (1537, 157, 106, 93, 92, 83)
	baseStatLevel[1][10]['hp'], baseStatLevel[1][10]['atk'], baseStatLevel[1][10]['def'], baseStatLevel[1][10]['anomalyProficiency'], baseStatLevel[1][10]['anomalyMastery'], baseStatLevel[1][10]['impact'] = (2012, 194, 139, 93, 92, 83)
	baseStatLevel[1][20]['hp'], baseStatLevel[1][20]['atk'], baseStatLevel[1][20]['def'], baseStatLevel[1][20]['anomalyProficiency'], baseStatLevel[1][20]['anomalyMastery'], baseStatLevel[1][20]['impact'] = (2951, 254, 205, 93, 92, 83)
	baseStatLevel[2][20]['hp'], baseStatLevel[2][20]['atk'], baseStatLevel[2][20]['def'], baseStatLevel[2][20]['anomalyProficiency'], baseStatLevel[2][20]['anomalyMastery'], baseStatLevel[2][20]['impact'] = (3426, 291, 238, 93, 92, 83)
	baseStatLevel[2][30]['hp'], baseStatLevel[2][30]['atk'], baseStatLevel[2][30]['def'], baseStatLevel[2][30]['anomalyProficiency'], baseStatLevel[2][30]['anomalyMastery'], baseStatLevel[2][30]['impact'] = (4366, 351, 304, 93, 92, 83)
	baseStatLevel[3][30]['hp'], baseStatLevel[3][30]['atk'], baseStatLevel[3][30]['def'], baseStatLevel[3][30]['anomalyProficiency'], baseStatLevel[3][30]['anomalyMastery'], baseStatLevel[3][30]['impact'] = (4841, 388, 337, 93, 92, 83)
	baseStatLevel[3][40]['hp'], baseStatLevel[3][40]['atk'], baseStatLevel[3][40]['def'], baseStatLevel[3][40]['anomalyProficiency'], baseStatLevel[3][40]['anomalyMastery'], baseStatLevel[3][40]['impact'] = (5780, 448, 402, 93, 92, 83)
	baseStatLevel[4][40]['hp'], baseStatLevel[4][40]['atk'], baseStatLevel[4][40]['def'], baseStatLevel[4][40]['anomalyProficiency'], baseStatLevel[4][40]['anomalyMastery'], baseStatLevel[4][40]['impact'] = (6255, 484, 436, 93, 92, 83)
	baseStatLevel[4][50]['hp'], baseStatLevel[4][50]['atk'], baseStatLevel[4][50]['def'], baseStatLevel[4][50]['anomalyProficiency'], baseStatLevel[4][50]['anomalyMastery'], baseStatLevel[4][50]['impact'] = (7194, 544, 502, 93, 92, 83)
	baseStatLevel[5][50]['hp'], baseStatLevel[5][50]['atk'], baseStatLevel[5][50]['def'], baseStatLevel[5][50]['anomalyProficiency'], baseStatLevel[5][50]['anomalyMastery'], baseStatLevel[5][50]['impact'] = (7669, 581, 535, 93, 92, 83)
	baseStatLevel[5][60]['hp'], baseStatLevel[5][60]['atk'], baseStatLevel[5][60]['def'], baseStatLevel[5][60]['anomalyProficiency'], baseStatLevel[5][60]['anomalyMastery'], baseStatLevel[5][60]['impact'] = (8609, 642, 600, 93, 92, 83)

	def __init__(self):
		super().__init__()



class Anby(Agent):
	name = "Anby"
	realName = "Anby Demara"
	rank = "A"
	attribute = "Electric"
	specialty = "Stun"
	faction = "Cunning Hares"
	attackType = "Slash"
	baseStatLevel = deepcopy(baseStatLevelTemplate)

	baseStatLevel[0][1]['hp'], baseStatLevel[0][1]['atk'], baseStatLevel[0][1]['def'], baseStatLevel[0][1]['anomalyProficiency'], baseStatLevel[0][1]['anomalyMastery'], baseStatLevel[0][1]['impact'] = (603, 95, 49, 94, 93, 118)
	baseStatLevel[0][10]['hp'], baseStatLevel[0][10]['atk'], baseStatLevel[0][10]['def'], baseStatLevel[0][10]['anomalyProficiency'], baseStatLevel[0][10]['anomalyMastery'], baseStatLevel[0][10]['impact'] = (1339, 143, 109, 94, 93, 118)
	baseStatLevel[1][10]['hp'], baseStatLevel[1][10]['atk'], baseStatLevel[1][10]['def'], baseStatLevel[1][10]['anomalyProficiency'], baseStatLevel[1][10]['anomalyMastery'], baseStatLevel[1][10]['impact'] = (1753, 177, 143, 94, 93, 118)
	baseStatLevel[1][20]['hp'], baseStatLevel[1][20]['atk'], baseStatLevel[1][20]['def'], baseStatLevel[1][20]['anomalyProficiency'], baseStatLevel[1][20]['anomalyMastery'], baseStatLevel[1][20]['impact'] = (2572, 232, 210, 94, 93, 118)
	baseStatLevel[2][20]['hp'], baseStatLevel[2][20]['atk'], baseStatLevel[2][20]['def'], baseStatLevel[2][20]['anomalyProficiency'], baseStatLevel[2][20]['anomalyMastery'], baseStatLevel[2][20]['impact'] = (2986, 266, 244, 94, 93, 118)
	baseStatLevel[2][30]['hp'], baseStatLevel[2][30]['atk'], baseStatLevel[2][30]['def'], baseStatLevel[2][30]['anomalyProficiency'], baseStatLevel[2][30]['anomalyMastery'], baseStatLevel[2][30]['impact'] = (3804, 320, 310, 94, 93, 118)
	baseStatLevel[3][30]['hp'], baseStatLevel[3][30]['atk'], baseStatLevel[3][30]['def'], baseStatLevel[3][30]['anomalyProficiency'], baseStatLevel[3][30]['anomalyMastery'], baseStatLevel[3][30]['impact'] = (4218, 354, 343, 94, 93, 118)
	baseStatLevel[3][40]['hp'], baseStatLevel[3][40]['atk'], baseStatLevel[3][40]['def'], baseStatLevel[3][40]['anomalyProficiency'], baseStatLevel[3][40]['anomalyMastery'], baseStatLevel[3][40]['impact'] = (5036, 408, 410, 94, 93, 118)
	baseStatLevel[4][40]['hp'], baseStatLevel[4][40]['atk'], baseStatLevel[4][40]['def'], baseStatLevel[4][40]['anomalyProficiency'], baseStatLevel[4][40]['anomalyMastery'], baseStatLevel[4][40]['impact'] = (5450, 441, 444, 94, 93, 118)
	baseStatLevel[4][50]['hp'], baseStatLevel[4][50]['atk'], baseStatLevel[4][50]['def'], baseStatLevel[4][50]['anomalyProficiency'], baseStatLevel[4][50]['anomalyMastery'], baseStatLevel[4][50]['impact'] = (6269, 495, 511, 94, 93, 118)
	baseStatLevel[5][50]['hp'], baseStatLevel[5][50]['atk'], baseStatLevel[5][50]['def'], baseStatLevel[5][50]['anomalyProficiency'], baseStatLevel[5][50]['anomalyMastery'], baseStatLevel[5][50]['impact'] = (6682, 529, 545, 94, 93, 118)
	baseStatLevel[5][60]['hp'], baseStatLevel[5][60]['atk'], baseStatLevel[5][60]['def'], baseStatLevel[5][60]['anomalyProficiency'], baseStatLevel[5][60]['anomalyMastery'], baseStatLevel[5][60]['impact'] = (7500, 583, 612, 94, 93, 118)

	def __init__(self):
		super().__init__()



class Anton(Agent):
	name = "Anton"
	realName = "Anton Ivanove"
	rank = "A"
	attribute = "Electric"
	specialty = "Attack"
	faction = "Belobog Heavy Industries"
	attackType = "Pierce"
	baseStatLevel = deepcopy(baseStatLevelTemplate)

	baseStatLevel[0][1]['hp'], baseStatLevel[0][1]['atk'], baseStatLevel[0][1]['def'], baseStatLevel[0][1]['anomalyProficiency'], baseStatLevel[0][1]['anomalyMastery'], baseStatLevel[0][1]['impact'] = (580, 114, 50, 86, 90, 95)
	baseStatLevel[0][10]['hp'], baseStatLevel[0][10]['atk'], baseStatLevel[0][10]['def'], baseStatLevel[0][10]['anomalyProficiency'], baseStatLevel[0][10]['anomalyMastery'], baseStatLevel[0][10]['impact'] = (1288, 174, 111, 86, 90, 95)
	baseStatLevel[1][10]['hp'], baseStatLevel[1][10]['atk'], baseStatLevel[1][10]['def'], baseStatLevel[1][10]['anomalyProficiency'], baseStatLevel[1][10]['anomalyMastery'], baseStatLevel[1][10]['impact'] = (1686, 215, 145, 86, 90, 95)
	baseStatLevel[1][20]['hp'], baseStatLevel[1][20]['atk'], baseStatLevel[1][20]['def'], baseStatLevel[1][20]['anomalyProficiency'], baseStatLevel[1][20]['anomalyMastery'], baseStatLevel[1][20]['impact'] = (2474, 283, 213, 86, 90, 95)
	baseStatLevel[2][20]['hp'], baseStatLevel[2][20]['atk'], baseStatLevel[2][20]['def'], baseStatLevel[2][20]['anomalyProficiency'], baseStatLevel[2][20]['anomalyMastery'], baseStatLevel[2][20]['impact'] = (2873, 323, 248, 86, 90, 95)
	baseStatLevel[2][30]['hp'], baseStatLevel[2][30]['atk'], baseStatLevel[2][30]['def'], baseStatLevel[2][30]['anomalyProficiency'], baseStatLevel[2][30]['anomalyMastery'], baseStatLevel[2][30]['impact'] = (3661, 391, 315, 86, 90, 95)
	baseStatLevel[3][30]['hp'], baseStatLevel[3][30]['atk'], baseStatLevel[3][30]['def'], baseStatLevel[3][30]['anomalyProficiency'], baseStatLevel[3][30]['anomalyMastery'], baseStatLevel[3][30]['impact'] = (4059, 432, 349, 86, 90, 95)
	baseStatLevel[3][40]['hp'], baseStatLevel[3][40]['atk'], baseStatLevel[3][40]['def'], baseStatLevel[3][40]['anomalyProficiency'], baseStatLevel[3][40]['anomalyMastery'], baseStatLevel[3][40]['impact'] = (4846, 500, 417, 86, 90, 95)
	baseStatLevel[4][40]['hp'], baseStatLevel[4][40]['atk'], baseStatLevel[4][40]['def'], baseStatLevel[4][40]['anomalyProficiency'], baseStatLevel[4][40]['anomalyMastery'], baseStatLevel[4][40]['impact'] = (5244, 541, 451, 86, 90, 95)
	baseStatLevel[4][50]['hp'], baseStatLevel[4][50]['atk'], baseStatLevel[4][50]['def'], baseStatLevel[4][50]['anomalyProficiency'], baseStatLevel[4][50]['anomalyMastery'], baseStatLevel[4][50]['impact'] = (6032, 608, 519, 86, 90, 95)
	baseStatLevel[5][50]['hp'], baseStatLevel[5][50]['atk'], baseStatLevel[5][50]['def'], baseStatLevel[5][50]['anomalyProficiency'], baseStatLevel[5][50]['anomalyMastery'], baseStatLevel[5][50]['impact'] = (6431, 648, 554, 86, 90, 95)
	baseStatLevel[5][60]['hp'], baseStatLevel[5][60]['atk'], baseStatLevel[5][60]['def'], baseStatLevel[5][60]['anomalyProficiency'], baseStatLevel[5][60]['anomalyMastery'], baseStatLevel[5][60]['impact'] = (7219, 716, 622, 86, 90, 95)

	def __init__(self):
		super().__init__()



class Ben(Agent):
	name = "Ben"
	realName = "Ben Bigger"
	rank = "A"
	attribute = "Fire"
	specialty = "Defense"
	faction = "Belobog Heavy Industries"
	attackType = "Strike"
	baseStatLevel = deepcopy(baseStatLevelTemplate)

	baseStatLevel[0][1]['hp'], baseStatLevel[0][1]['atk'], baseStatLevel[0][1]['def'], baseStatLevel[0][1]['anomalyProficiency'], baseStatLevel[0][1]['anomalyMastery'], baseStatLevel[0][1]['impact'] = (690, 94, 58, 86, 90, 95)
	baseStatLevel[0][10]['hp'], baseStatLevel[0][10]['atk'], baseStatLevel[0][10]['def'], baseStatLevel[0][10]['anomalyProficiency'], baseStatLevel[0][10]['anomalyMastery'], baseStatLevel[0][10]['impact'] = (1532, 142, 129, 86, 90, 95)
	baseStatLevel[1][10]['hp'], baseStatLevel[1][10]['atk'], baseStatLevel[1][10]['def'], baseStatLevel[1][10]['anomalyProficiency'], baseStatLevel[1][10]['anomalyMastery'], baseStatLevel[1][10]['impact'] = (2005, 176, 169, 86, 90, 95)
	baseStatLevel[1][20]['hp'], baseStatLevel[1][20]['atk'], baseStatLevel[1][20]['def'], baseStatLevel[1][20]['anomalyProficiency'], baseStatLevel[1][20]['anomalyMastery'], baseStatLevel[1][20]['impact'] = (2941, 229, 248, 86, 90, 95)
	baseStatLevel[2][20]['hp'], baseStatLevel[2][20]['atk'], baseStatLevel[2][20]['def'], baseStatLevel[2][20]['anomalyProficiency'], baseStatLevel[2][20]['anomalyMastery'], baseStatLevel[2][20]['impact'] = (3415, 262, 288, 86, 90, 95)
	baseStatLevel[2][30]['hp'], baseStatLevel[2][30]['atk'], baseStatLevel[2][30]['def'], baseStatLevel[2][30]['anomalyProficiency'], baseStatLevel[2][30]['anomalyMastery'], baseStatLevel[2][30]['impact'] = (4350, 316, 367, 86, 90, 95)
	baseStatLevel[3][30]['hp'], baseStatLevel[3][30]['atk'], baseStatLevel[3][30]['def'], baseStatLevel[3][30]['anomalyProficiency'], baseStatLevel[3][30]['anomalyMastery'], baseStatLevel[3][30]['impact'] = (4823, 350, 407, 86, 90, 95)
	baseStatLevel[3][40]['hp'], baseStatLevel[3][40]['atk'], baseStatLevel[3][40]['def'], baseStatLevel[3][40]['anomalyProficiency'], baseStatLevel[3][40]['anomalyMastery'], baseStatLevel[3][40]['impact'] = (5759, 403, 486, 86, 90, 95)
	baseStatLevel[4][40]['hp'], baseStatLevel[4][40]['atk'], baseStatLevel[4][40]['def'], baseStatLevel[4][40]['anomalyProficiency'], baseStatLevel[4][40]['anomalyMastery'], baseStatLevel[4][40]['impact'] = (6232, 436, 526, 86, 90, 95)
	baseStatLevel[4][50]['hp'], baseStatLevel[4][50]['atk'], baseStatLevel[4][50]['def'], baseStatLevel[4][50]['anomalyProficiency'], baseStatLevel[4][50]['anomalyMastery'], baseStatLevel[4][50]['impact'] = (7168, 490, 605, 86, 90, 95)
	baseStatLevel[5][50]['hp'], baseStatLevel[5][50]['atk'], baseStatLevel[5][50]['def'], baseStatLevel[5][50]['anomalyProficiency'], baseStatLevel[5][50]['anomalyMastery'], baseStatLevel[5][50]['impact'] = (7641, 524, 645, 86, 90, 95)
	baseStatLevel[5][60]['hp'], baseStatLevel[5][60]['atk'], baseStatLevel[5][60]['def'], baseStatLevel[5][60]['anomalyProficiency'], baseStatLevel[5][60]['anomalyMastery'], baseStatLevel[5][60]['impact'] = (8577, 578, 724, 86, 90, 95)


	def __init__(self):
		super().__init__()



class Billy(Agent):
	name = "Billy"
	realName = "Billy Kid"
	rank = "A"
	attribute = "Physical"
	specialty = "Attack"
	faction = "Cunning Hares"
	attackType = "Pierce"
	baseStatLevel = deepcopy(baseStatLevelTemplate)

	baseStatLevel[0][1]['hp'], baseStatLevel[0][1]['atk'], baseStatLevel[0][1]['def'], baseStatLevel[0][1]['anomalyProficiency'], baseStatLevel[0][1]['anomalyMastery'], baseStatLevel[0][1]['impact'] = (555, 113, 49, 92, 91, 91)
	baseStatLevel[0][10]['hp'], baseStatLevel[0][10]['atk'], baseStatLevel[0][10]['def'], baseStatLevel[0][10]['anomalyProficiency'], baseStatLevel[0][10]['anomalyMastery'], baseStatLevel[0][10]['impact'] = (1233, 173, 108, 92, 91, 91)
	baseStatLevel[1][10]['hp'], baseStatLevel[1][10]['atk'], baseStatLevel[1][10]['def'], baseStatLevel[1][10]['anomalyProficiency'], baseStatLevel[1][10]['anomalyMastery'], baseStatLevel[1][10]['impact'] = (1614, 213, 141, 92, 91, 91)
	baseStatLevel[1][20]['hp'], baseStatLevel[1][20]['atk'], baseStatLevel[1][20]['def'], baseStatLevel[1][20]['anomalyProficiency'], baseStatLevel[1][20]['anomalyMastery'], baseStatLevel[1][20]['impact'] = (2367, 280, 207, 92, 91, 91)
	baseStatLevel[2][20]['hp'], baseStatLevel[2][20]['atk'], baseStatLevel[2][20]['def'], baseStatLevel[2][20]['anomalyProficiency'], baseStatLevel[2][20]['anomalyMastery'], baseStatLevel[2][20]['impact'] = (2748, 321, 241, 92, 91, 91)
	baseStatLevel[2][30]['hp'], baseStatLevel[2][30]['atk'], baseStatLevel[2][30]['def'], baseStatLevel[2][30]['anomalyProficiency'], baseStatLevel[2][30]['anomalyMastery'], baseStatLevel[2][30]['impact'] = (3502, 389, 307, 92, 91, 91)
	baseStatLevel[3][30]['hp'], baseStatLevel[3][30]['atk'], baseStatLevel[3][30]['def'], baseStatLevel[3][30]['anomalyProficiency'], baseStatLevel[3][30]['anomalyMastery'], baseStatLevel[3][30]['impact'] = (3883, 429, 340, 92, 91, 91)
	baseStatLevel[3][40]['hp'], baseStatLevel[3][40]['atk'], baseStatLevel[3][40]['def'], baseStatLevel[3][40]['anomalyProficiency'], baseStatLevel[3][40]['anomalyMastery'], baseStatLevel[3][40]['impact'] = (4637, 496, 407, 92, 91, 91)
	baseStatLevel[4][40]['hp'], baseStatLevel[4][40]['atk'], baseStatLevel[4][40]['def'], baseStatLevel[4][40]['anomalyProficiency'], baseStatLevel[4][40]['anomalyMastery'], baseStatLevel[4][40]['impact'] = (5018, 537, 441, 92, 91, 91)
	baseStatLevel[4][50]['hp'], baseStatLevel[4][50]['atk'], baseStatLevel[4][50]['def'], baseStatLevel[4][50]['anomalyProficiency'], baseStatLevel[4][50]['anomalyMastery'], baseStatLevel[4][50]['impact'] = (5771, 604, 507, 92, 91, 91)
	baseStatLevel[5][50]['hp'], baseStatLevel[5][50]['atk'], baseStatLevel[5][50]['def'], baseStatLevel[5][50]['anomalyProficiency'], baseStatLevel[5][50]['anomalyMastery'], baseStatLevel[5][50]['impact'] = (6153, 644, 540, 92, 91, 91)
	baseStatLevel[5][60]['hp'], baseStatLevel[5][60]['atk'], baseStatLevel[5][60]['def'], baseStatLevel[5][60]['anomalyProficiency'], baseStatLevel[5][60]['anomalyMastery'], baseStatLevel[5][60]['impact'] = (6907, 712, 606, 92, 91, 91)


	def __init__(self):
		super().__init__()



class Corin(Agent):
	name = "Corin"
	realName = "Corin Wickes"
	rank = "A"
	attribute = "Physical"
	specialty = "Attack"
	faction = "Victoria Housekeeping"
	attackType = "Slash"
	baseStatLevel = deepcopy(baseStatLevelTemplate)

	baseStatLevel[0][1]['hp'], baseStatLevel[0][1]['atk'], baseStatLevel[0][1]['def'], baseStatLevel[0][1]['anomalyProficiency'], baseStatLevel[0][1]['anomalyMastery'], baseStatLevel[0][1]['impact'] = (561, 116, 49, 93, 96, 93)
	baseStatLevel[0][10]['hp'], baseStatLevel[0][10]['atk'], baseStatLevel[0][10]['def'], baseStatLevel[0][10]['anomalyProficiency'], baseStatLevel[0][10]['anomalyMastery'], baseStatLevel[0][10]['impact'] = (1246, 178, 108, 93, 96, 93)
	baseStatLevel[1][10]['hp'], baseStatLevel[1][10]['atk'], baseStatLevel[1][10]['def'], baseStatLevel[1][10]['anomalyProficiency'], baseStatLevel[1][10]['anomalyMastery'], baseStatLevel[1][10]['impact'] = (1631, 219, 141, 93, 96, 93)
	baseStatLevel[1][20]['hp'], baseStatLevel[1][20]['atk'], baseStatLevel[1][20]['def'], baseStatLevel[1][20]['anomalyProficiency'], baseStatLevel[1][20]['anomalyMastery'], baseStatLevel[1][20]['impact'] = (2392, 288, 207, 93, 96, 93)
	baseStatLevel[2][20]['hp'], baseStatLevel[2][20]['atk'], baseStatLevel[2][20]['def'], baseStatLevel[2][20]['anomalyProficiency'], baseStatLevel[2][20]['anomalyMastery'], baseStatLevel[2][20]['impact'] = (2777, 330, 241, 93, 96, 93)
	baseStatLevel[2][30]['hp'], baseStatLevel[2][30]['atk'], baseStatLevel[2][30]['def'], baseStatLevel[2][30]['anomalyProficiency'], baseStatLevel[2][30]['anomalyMastery'], baseStatLevel[2][30]['impact'] = (3538, 400, 307, 93, 96, 93)
	baseStatLevel[3][30]['hp'], baseStatLevel[3][30]['atk'], baseStatLevel[3][30]['def'], baseStatLevel[3][30]['anomalyProficiency'], baseStatLevel[3][30]['anomalyMastery'], baseStatLevel[3][30]['impact'] = (3923, 441, 340, 93, 96, 93)
	baseStatLevel[3][40]['hp'], baseStatLevel[3][40]['atk'], baseStatLevel[3][40]['def'], baseStatLevel[3][40]['anomalyProficiency'], baseStatLevel[3][40]['anomalyMastery'], baseStatLevel[3][40]['impact'] = (4684, 510, 405, 93, 96, 93)
	baseStatLevel[4][40]['hp'], baseStatLevel[4][40]['atk'], baseStatLevel[4][40]['def'], baseStatLevel[4][40]['anomalyProficiency'], baseStatLevel[4][40]['anomalyMastery'], baseStatLevel[4][40]['impact'] = (5069, 552, 438, 93, 96, 93)
	baseStatLevel[4][50]['hp'], baseStatLevel[4][50]['atk'], baseStatLevel[4][50]['def'], baseStatLevel[4][50]['anomalyProficiency'], baseStatLevel[4][50]['anomalyMastery'], baseStatLevel[4][50]['impact'] = (5830, 621, 504, 93, 96, 93)
	baseStatLevel[5][50]['hp'], baseStatLevel[5][50]['atk'], baseStatLevel[5][50]['def'], baseStatLevel[5][50]['anomalyProficiency'], baseStatLevel[5][50]['anomalyMastery'], baseStatLevel[5][50]['impact'] = (6215, 662, 538, 93, 96, 93)
	baseStatLevel[5][60]['hp'], baseStatLevel[5][60]['atk'], baseStatLevel[5][60]['def'], baseStatLevel[5][60]['anomalyProficiency'], baseStatLevel[5][60]['anomalyMastery'], baseStatLevel[5][60]['impact'] = (6976, 732, 604, 93, 96, 93)


	def __init__(self):
		super().__init__()



class Ellen(Agent):
	name = "Ellen"
	realName = "Ellen Joe"
	rank = "S"
	attribute = "Ice"
	specialty = "Attack"
	faction = "Victoria Housekeeping"
	attackType = "Slash"
	baseStatLevel = deepcopy(baseStatLevelTemplate)

	baseStatLevel[0][1]['hp'], baseStatLevel[0][1]['atk'], baseStatLevel[0][1]['def'], baseStatLevel[0][1]['anomalyProficiency'], baseStatLevel[0][1]['anomalyMastery'], baseStatLevel[0][1]['impact'] = (617, 135, 49, 94, 93, 93)
	baseStatLevel[0][10]['hp'], baseStatLevel[0][10]['atk'], baseStatLevel[0][10]['def'], baseStatLevel[0][10]['anomalyProficiency'], baseStatLevel[0][10]['anomalyMastery'], baseStatLevel[0][10]['impact'] = (1370, 209, 108, 94, 93, 93)
	baseStatLevel[1][10]['hp'], baseStatLevel[1][10]['atk'], baseStatLevel[1][10]['def'], baseStatLevel[1][10]['anomalyProficiency'], baseStatLevel[1][10]['anomalyMastery'], baseStatLevel[1][10]['impact'] = (1793, 257, 141, 94, 93, 93)
	baseStatLevel[1][20]['hp'], baseStatLevel[1][20]['atk'], baseStatLevel[1][20]['def'], baseStatLevel[1][20]['anomalyProficiency'], baseStatLevel[1][20]['anomalyMastery'], baseStatLevel[1][20]['impact'] = (2630, 339, 207, 94, 93, 93)
	baseStatLevel[2][20]['hp'], baseStatLevel[2][20]['atk'], baseStatLevel[2][20]['def'], baseStatLevel[2][20]['anomalyProficiency'], baseStatLevel[2][20]['anomalyMastery'], baseStatLevel[2][20]['impact'] = (3054, 387, 241, 94, 93, 93)
	baseStatLevel[2][30]['hp'], baseStatLevel[2][30]['atk'], baseStatLevel[2][30]['def'], baseStatLevel[2][30]['anomalyProficiency'], baseStatLevel[2][30]['anomalyMastery'], baseStatLevel[2][30]['impact'] = (3891, 470, 307, 94, 93, 93)
	baseStatLevel[3][30]['hp'], baseStatLevel[3][30]['atk'], baseStatLevel[3][30]['def'], baseStatLevel[3][30]['anomalyProficiency'], baseStatLevel[3][30]['anomalyMastery'], baseStatLevel[3][30]['impact'] = (4314, 519, 340, 94, 93, 93)
	baseStatLevel[3][40]['hp'], baseStatLevel[3][40]['atk'], baseStatLevel[3][40]['def'], baseStatLevel[3][40]['anomalyProficiency'], baseStatLevel[3][40]['anomalyMastery'], baseStatLevel[3][40]['impact'] = (5152, 602, 407, 94, 93, 93)
	baseStatLevel[4][40]['hp'], baseStatLevel[4][40]['atk'], baseStatLevel[4][40]['def'], baseStatLevel[4][40]['anomalyProficiency'], baseStatLevel[4][40]['anomalyMastery'], baseStatLevel[4][40]['impact'] = (5576, 650, 441, 94, 93, 93)
	baseStatLevel[4][50]['hp'], baseStatLevel[4][50]['atk'], baseStatLevel[4][50]['def'], baseStatLevel[4][50]['anomalyProficiency'], baseStatLevel[4][50]['anomalyMastery'], baseStatLevel[4][50]['impact'] = (6413, 732, 507, 94, 93, 93)
	baseStatLevel[5][50]['hp'], baseStatLevel[5][50]['atk'], baseStatLevel[5][50]['def'], baseStatLevel[5][50]['anomalyProficiency'], baseStatLevel[5][50]['anomalyMastery'], baseStatLevel[5][50]['impact'] = (6836, 780, 540, 94, 93, 93)
	baseStatLevel[5][60]['hp'], baseStatLevel[5][60]['atk'], baseStatLevel[5][60]['def'], baseStatLevel[5][60]['anomalyProficiency'], baseStatLevel[5][60]['anomalyMastery'], baseStatLevel[5][60]['impact'] = (7673, 863, 606, 94, 93, 93)


	def __init__(self):
		super().__init__()



class Grace(Agent):
	name = "Grace"
	realName = "Grace Howard"
	rank = "S"
	attribute = "Electric"
	specialty = "Anomaly"
	faction = "Belobog Heavy Industries"
	attackType = "Pierce"
	baseStatLevel = deepcopy(baseStatLevelTemplate)

	baseStatLevel[0][1]['hp'], baseStatLevel[0][1]['atk'], baseStatLevel[0][1]['def'], baseStatLevel[0][1]['anomalyProficiency'], baseStatLevel[0][1]['anomalyMastery'], baseStatLevel[0][1]['impact'] = (602, 119, 48, 115, 116, 83)
	baseStatLevel[0][10]['hp'], baseStatLevel[0][10]['atk'], baseStatLevel[0][10]['def'], baseStatLevel[0][10]['anomalyProficiency'], baseStatLevel[0][10]['anomalyMastery'], baseStatLevel[0][10]['impact'] = (1336, 183, 106, 115, 116, 83)
	baseStatLevel[1][10]['hp'], baseStatLevel[1][10]['atk'], baseStatLevel[1][10]['def'], baseStatLevel[1][10]['anomalyProficiency'], baseStatLevel[1][10]['anomalyMastery'], baseStatLevel[1][10]['impact'] = (1749, 225, 139, 115, 116, 83)
	baseStatLevel[1][20]['hp'], baseStatLevel[1][20]['atk'], baseStatLevel[1][20]['def'], baseStatLevel[1][20]['anomalyProficiency'], baseStatLevel[1][20]['anomalyMastery'], baseStatLevel[1][20]['impact'] = (2566, 296, 205, 115, 116, 83)
	baseStatLevel[2][20]['hp'], baseStatLevel[2][20]['atk'], baseStatLevel[2][20]['def'], baseStatLevel[2][20]['anomalyProficiency'], baseStatLevel[2][20]['anomalyMastery'], baseStatLevel[2][20]['impact'] = (2979, 339, 238, 115, 116, 83)
	baseStatLevel[2][30]['hp'], baseStatLevel[2][30]['atk'], baseStatLevel[2][30]['def'], baseStatLevel[2][30]['anomalyProficiency'], baseStatLevel[2][30]['anomalyMastery'], baseStatLevel[2][30]['impact'] = (3795, 410, 304, 115, 116, 83)
	baseStatLevel[3][30]['hp'], baseStatLevel[3][30]['atk'], baseStatLevel[3][30]['def'], baseStatLevel[3][30]['anomalyProficiency'], baseStatLevel[3][30]['anomalyMastery'], baseStatLevel[3][30]['impact'] = (4208, 452, 337, 115, 116, 83)
	baseStatLevel[3][40]['hp'], baseStatLevel[3][40]['atk'], baseStatLevel[3][40]['def'], baseStatLevel[3][40]['anomalyProficiency'], baseStatLevel[3][40]['anomalyMastery'], baseStatLevel[3][40]['impact'] = (5024, 523, 402, 115, 116, 83)
	baseStatLevel[4][40]['hp'], baseStatLevel[4][40]['atk'], baseStatLevel[4][40]['def'], baseStatLevel[4][40]['anomalyProficiency'], baseStatLevel[4][40]['anomalyMastery'], baseStatLevel[4][40]['impact'] = (5436, 566, 436, 115, 116, 83)
	baseStatLevel[4][50]['hp'], baseStatLevel[4][50]['atk'], baseStatLevel[4][50]['def'], baseStatLevel[4][50]['anomalyProficiency'], baseStatLevel[4][50]['anomalyMastery'], baseStatLevel[4][50]['impact'] = (6253, 637, 502, 115, 116, 83)
	baseStatLevel[5][50]['hp'], baseStatLevel[5][50]['atk'], baseStatLevel[5][50]['def'], baseStatLevel[5][50]['anomalyProficiency'], baseStatLevel[5][50]['anomalyMastery'], baseStatLevel[5][50]['impact'] = (6666, 679, 535, 115, 116, 83)
	baseStatLevel[5][60]['hp'], baseStatLevel[5][60]['atk'], baseStatLevel[5][60]['def'], baseStatLevel[5][60]['anomalyProficiency'], baseStatLevel[5][60]['anomalyMastery'], baseStatLevel[5][60]['impact'] = (7482, 750, 600, 115, 116, 83)


	def __init__(self):
		super().__init__()



class Koleda(Agent):
	name = "Koleda"
	realName = "Koleda Belobog"
	rank = "S"
	attribute = "Fire"
	specialty = "Stun"
	faction = "Belobog Heavy Industries"
	attackType = "Strike"
	baseStatLevel = deepcopy(baseStatLevelTemplate)

	baseStatLevel[0][1]['hp'], baseStatLevel[0][1]['atk'], baseStatLevel[0][1]['def'], baseStatLevel[0][1]['anomalyProficiency'], baseStatLevel[0][1]['anomalyMastery'], baseStatLevel[0][1]['impact'] = (653, 106, 48, 97, 96, 116)
	baseStatLevel[0][10]['hp'], baseStatLevel[0][10]['atk'], baseStatLevel[0][10]['def'], baseStatLevel[0][10]['anomalyProficiency'], baseStatLevel[0][10]['anomalyMastery'], baseStatLevel[0][10]['impact'] = (1451, 161, 106, 97, 96, 116)
	baseStatLevel[1][10]['hp'], baseStatLevel[1][10]['atk'], baseStatLevel[1][10]['def'], baseStatLevel[1][10]['anomalyProficiency'], baseStatLevel[1][10]['anomalyMastery'], baseStatLevel[1][10]['impact'] = (1899, 199, 139, 97, 96, 116)
	baseStatLevel[1][20]['hp'], baseStatLevel[1][20]['atk'], baseStatLevel[1][20]['def'], baseStatLevel[1][20]['anomalyProficiency'], baseStatLevel[1][20]['anomalyMastery'], baseStatLevel[1][20]['impact'] = (2785, 261, 204, 97, 96, 116)
	baseStatLevel[2][20]['hp'], baseStatLevel[2][20]['atk'], baseStatLevel[2][20]['def'], baseStatLevel[2][20]['anomalyProficiency'], baseStatLevel[2][20]['anomalyMastery'], baseStatLevel[2][20]['impact'] = (3234, 299, 237, 97, 96, 116)
	baseStatLevel[2][30]['hp'], baseStatLevel[2][30]['atk'], baseStatLevel[2][30]['def'], baseStatLevel[2][30]['anomalyProficiency'], baseStatLevel[2][30]['anomalyMastery'], baseStatLevel[2][30]['impact'] = (4121, 361, 302, 97, 96, 116)
	baseStatLevel[3][30]['hp'], baseStatLevel[3][30]['atk'], baseStatLevel[3][30]['def'], baseStatLevel[3][30]['anomalyProficiency'], baseStatLevel[3][30]['anomalyMastery'], baseStatLevel[3][30]['impact'] = (4569, 398, 334, 97, 96, 116)
	baseStatLevel[3][40]['hp'], baseStatLevel[3][40]['atk'], baseStatLevel[3][40]['def'], baseStatLevel[3][40]['anomalyProficiency'], baseStatLevel[3][40]['anomalyMastery'], baseStatLevel[3][40]['impact'] = (5456, 460, 398, 97, 96, 116)
	baseStatLevel[4][40]['hp'], baseStatLevel[4][40]['atk'], baseStatLevel[4][40]['def'], baseStatLevel[4][40]['anomalyProficiency'], baseStatLevel[4][40]['anomalyMastery'], baseStatLevel[4][40]['impact'] = (5905, 498, 431, 97, 96, 116)
	baseStatLevel[4][50]['hp'], baseStatLevel[4][50]['atk'], baseStatLevel[4][50]['def'], baseStatLevel[4][50]['anomalyProficiency'], baseStatLevel[4][50]['anomalyMastery'], baseStatLevel[4][50]['impact'] = (6792, 560, 496, 97, 96, 116)
	baseStatLevel[5][50]['hp'], baseStatLevel[5][50]['atk'], baseStatLevel[5][50]['def'], baseStatLevel[5][50]['anomalyProficiency'], baseStatLevel[5][50]['anomalyMastery'], baseStatLevel[5][50]['impact'] = (7240, 598, 529, 97, 96, 116)
	baseStatLevel[5][60]['hp'], baseStatLevel[5][60]['atk'], baseStatLevel[5][60]['def'], baseStatLevel[5][60]['anomalyProficiency'], baseStatLevel[5][60]['anomalyMastery'], baseStatLevel[5][60]['impact'] = (8127, 660, 594, 97, 96, 116)



	def __init__(self):
		super().__init__()



class Lucy(Agent):
	name = "Lucy"
	realName = "Luciana de Montefio"
	rank = "A"
	attribute = "Fire"
	specialty = "Support"
	faction = "Sons of Calydon"
	attackType = "Strike"
	baseStatLevel = deepcopy(baseStatLevelTemplate)

	baseStatLevel[0][1]['hp'], baseStatLevel[0][1]['atk'], baseStatLevel[0][1]['def'], baseStatLevel[0][1]['anomalyProficiency'], baseStatLevel[0][1]['anomalyMastery'], baseStatLevel[0][1]['impact'] = (645, 95, 49, 94, 93, 86)
	baseStatLevel[0][10]['hp'], baseStatLevel[0][10]['atk'], baseStatLevel[0][10]['def'], baseStatLevel[0][10]['anomalyProficiency'], baseStatLevel[0][10]['anomalyMastery'], baseStatLevel[0][10]['impact'] = (1433, 143, 109, 94, 93, 86)
	baseStatLevel[1][10]['hp'], baseStatLevel[1][10]['atk'], baseStatLevel[1][10]['def'], baseStatLevel[1][10]['anomalyProficiency'], baseStatLevel[1][10]['anomalyMastery'], baseStatLevel[1][10]['impact'] = (1876, 177, 143, 94, 93, 86)
	baseStatLevel[1][20]['hp'], baseStatLevel[1][20]['atk'], baseStatLevel[1][20]['def'], baseStatLevel[1][20]['anomalyProficiency'], baseStatLevel[1][20]['anomalyMastery'], baseStatLevel[1][20]['impact'] = (2751, 232, 210, 94, 93, 86)
	baseStatLevel[2][20]['hp'], baseStatLevel[2][20]['atk'], baseStatLevel[2][20]['def'], baseStatLevel[2][20]['anomalyProficiency'], baseStatLevel[2][20]['anomalyMastery'], baseStatLevel[2][20]['impact'] = (3194, 266, 244, 94, 93, 86)
	baseStatLevel[2][30]['hp'], baseStatLevel[2][30]['atk'], baseStatLevel[2][30]['def'], baseStatLevel[2][30]['anomalyProficiency'], baseStatLevel[2][30]['anomalyMastery'], baseStatLevel[2][30]['impact'] = (4070, 320, 310, 94, 93, 86)
	baseStatLevel[3][30]['hp'], baseStatLevel[3][30]['atk'], baseStatLevel[3][30]['def'], baseStatLevel[3][30]['anomalyProficiency'], baseStatLevel[3][30]['anomalyMastery'], baseStatLevel[3][30]['impact'] = (4513, 354, 343, 94, 93, 86)
	baseStatLevel[3][40]['hp'], baseStatLevel[3][40]['atk'], baseStatLevel[3][40]['def'], baseStatLevel[3][40]['anomalyProficiency'], baseStatLevel[3][40]['anomalyMastery'], baseStatLevel[3][40]['impact'] = (5389, 408, 410, 94, 93, 86)
	baseStatLevel[4][40]['hp'], baseStatLevel[4][40]['atk'], baseStatLevel[4][40]['def'], baseStatLevel[4][40]['anomalyProficiency'], baseStatLevel[4][40]['anomalyMastery'], baseStatLevel[4][40]['impact'] = (5832, 441, 444, 94, 93, 86)
	baseStatLevel[4][50]['hp'], baseStatLevel[4][50]['atk'], baseStatLevel[4][50]['def'], baseStatLevel[4][50]['anomalyProficiency'], baseStatLevel[4][50]['anomalyMastery'], baseStatLevel[4][50]['impact'] = (6708, 495, 511, 94, 93, 86)
	baseStatLevel[5][50]['hp'], baseStatLevel[5][50]['atk'], baseStatLevel[5][50]['def'], baseStatLevel[5][50]['anomalyProficiency'], baseStatLevel[5][50]['anomalyMastery'], baseStatLevel[5][50]['impact'] = (7150, 529, 545, 94, 93, 86)
	baseStatLevel[5][60]['hp'], baseStatLevel[5][60]['atk'], baseStatLevel[5][60]['def'], baseStatLevel[5][60]['anomalyProficiency'], baseStatLevel[5][60]['anomalyMastery'], baseStatLevel[5][60]['impact'] = (8025, 583, 612, 94, 93, 86)


	def __init__(self):
		super().__init__()



class Nekomata(Agent):
	name = "Nekomata"
	realName = "Nekomiya Mana"
	rank = "S"
	attribute = "Physical"
	specialty = "Attack"
	faction = "Cunning Hares"
	attackType = "Slash"
	baseStatLevel = deepcopy(baseStatLevelTemplate)

	baseStatLevel[0][1]['hp'], baseStatLevel[0][1]['atk'], baseStatLevel[0][1]['def'], baseStatLevel[0][1]['anomalyProficiency'], baseStatLevel[0][1]['anomalyMastery'], baseStatLevel[0][1]['impact'] = (608, 131, 47, 97, 96, 92)
	baseStatLevel[0][10]['hp'], baseStatLevel[0][10]['atk'], baseStatLevel[0][10]['def'], baseStatLevel[0][10]['anomalyProficiency'], baseStatLevel[0][10]['anomalyMastery'], baseStatLevel[0][10]['impact'] = (1350, 202, 104, 97, 96, 92)
	baseStatLevel[1][10]['hp'], baseStatLevel[1][10]['atk'], baseStatLevel[1][10]['def'], baseStatLevel[1][10]['anomalyProficiency'], baseStatLevel[1][10]['anomalyMastery'], baseStatLevel[1][10]['impact'] = (1767, 249, 136, 97, 96, 92)
	baseStatLevel[1][20]['hp'], baseStatLevel[1][20]['atk'], baseStatLevel[1][20]['def'], baseStatLevel[1][20]['anomalyProficiency'], baseStatLevel[1][20]['anomalyMastery'], baseStatLevel[1][20]['impact'] = (2592, 329, 200, 97, 96, 92)
	baseStatLevel[2][20]['hp'], baseStatLevel[2][20]['atk'], baseStatLevel[2][20]['def'], baseStatLevel[2][20]['anomalyProficiency'], baseStatLevel[2][20]['anomalyMastery'], baseStatLevel[2][20]['impact'] = (3009, 376, 233, 97, 96, 92)
	baseStatLevel[2][30]['hp'], baseStatLevel[2][30]['atk'], baseStatLevel[2][30]['def'], baseStatLevel[2][30]['anomalyProficiency'], baseStatLevel[2][30]['anomalyMastery'], baseStatLevel[2][30]['impact'] = (3833, 456, 298, 97, 96, 92)
	baseStatLevel[3][30]['hp'], baseStatLevel[3][30]['atk'], baseStatLevel[3][30]['def'], baseStatLevel[3][30]['anomalyProficiency'], baseStatLevel[3][30]['anomalyMastery'], baseStatLevel[3][30]['impact'] = (4250, 502, 330, 97, 96, 92)
	baseStatLevel[3][40]['hp'], baseStatLevel[3][40]['atk'], baseStatLevel[3][40]['def'], baseStatLevel[3][40]['anomalyProficiency'], baseStatLevel[3][40]['anomalyMastery'], baseStatLevel[3][40]['impact'] = (5075, 582, 394, 97, 96, 92)
	baseStatLevel[4][40]['hp'], baseStatLevel[4][40]['atk'], baseStatLevel[4][40]['def'], baseStatLevel[4][40]['anomalyProficiency'], baseStatLevel[4][40]['anomalyMastery'], baseStatLevel[4][40]['impact'] = (5492, 629, 427, 97, 96, 92)
	baseStatLevel[4][50]['hp'], baseStatLevel[4][50]['atk'], baseStatLevel[4][50]['def'], baseStatLevel[4][50]['anomalyProficiency'], baseStatLevel[4][50]['anomalyMastery'], baseStatLevel[4][50]['impact'] = (6317, 708, 491, 97, 96, 92)
	baseStatLevel[5][50]['hp'], baseStatLevel[5][50]['atk'], baseStatLevel[5][50]['def'], baseStatLevel[5][50]['anomalyProficiency'], baseStatLevel[5][50]['anomalyMastery'], baseStatLevel[5][50]['impact'] = (6735, 755, 523, 97, 96, 92)
	baseStatLevel[5][60]['hp'], baseStatLevel[5][60]['atk'], baseStatLevel[5][60]['def'], baseStatLevel[5][60]['anomalyProficiency'], baseStatLevel[5][60]['anomalyMastery'], baseStatLevel[5][60]['impact'] = (7560, 835, 587, 97, 96, 92)


	def __init__(self):
		super().__init__()



class Nicole(Agent):
	name = "Nicole"
	realName = "Nicole Demara"
	rank = "A"
	attribute = "Ether"
	specialty = "Support"
	faction = "Cunning Hares"
	attackType = "Strike"
	baseStatLevel = deepcopy(baseStatLevelTemplate)

	baseStatLevel[0][1]['hp'], baseStatLevel[0][1]['atk'], baseStatLevel[0][1]['def'], baseStatLevel[0][1]['anomalyProficiency'], baseStatLevel[0][1]['anomalyMastery'], baseStatLevel[0][1]['impact'] = (655, 93, 50, 90, 93, 88)
	baseStatLevel[0][10]['hp'], baseStatLevel[0][10]['atk'], baseStatLevel[0][10]['def'], baseStatLevel[0][10]['anomalyProficiency'], baseStatLevel[0][10]['anomalyMastery'], baseStatLevel[0][10]['impact'] = (1454, 140, 111, 90, 93, 88)
	baseStatLevel[1][10]['hp'], baseStatLevel[1][10]['atk'], baseStatLevel[1][10]['def'], baseStatLevel[1][10]['anomalyProficiency'], baseStatLevel[1][10]['anomalyMastery'], baseStatLevel[1][10]['impact'] = (1903, 173, 145, 90, 93, 88)
	baseStatLevel[1][20]['hp'], baseStatLevel[1][20]['atk'], baseStatLevel[1][20]['def'], baseStatLevel[1][20]['anomalyProficiency'], baseStatLevel[1][20]['anomalyMastery'], baseStatLevel[1][20]['impact'] = (2792, 227, 213, 90, 93, 88)
	baseStatLevel[2][20]['hp'], baseStatLevel[2][20]['atk'], baseStatLevel[2][20]['def'], baseStatLevel[2][20]['anomalyProficiency'], baseStatLevel[2][20]['anomalyMastery'], baseStatLevel[2][20]['impact'] = (3242, 261, 248, 90, 93, 88)
	baseStatLevel[2][30]['hp'], baseStatLevel[2][30]['atk'], baseStatLevel[2][30]['def'], baseStatLevel[2][30]['anomalyProficiency'], baseStatLevel[2][30]['anomalyMastery'], baseStatLevel[2][30]['impact'] = (4131, 314, 315, 90, 93, 88)
	baseStatLevel[3][30]['hp'], baseStatLevel[3][30]['atk'], baseStatLevel[3][30]['def'], baseStatLevel[3][30]['anomalyProficiency'], baseStatLevel[3][30]['anomalyMastery'], baseStatLevel[3][30]['impact'] = (4580, 347, 349, 90, 93, 88)
	baseStatLevel[3][40]['hp'], baseStatLevel[3][40]['atk'], baseStatLevel[3][40]['def'], baseStatLevel[3][40]['anomalyProficiency'], baseStatLevel[3][40]['anomalyMastery'], baseStatLevel[3][40]['impact'] = (5469, 400, 417, 90, 93, 88)
	baseStatLevel[4][40]['hp'], baseStatLevel[4][40]['atk'], baseStatLevel[4][40]['def'], baseStatLevel[4][40]['anomalyProficiency'], baseStatLevel[4][40]['anomalyMastery'], baseStatLevel[4][40]['impact'] = (5919, 433, 451, 90, 93, 88)
	baseStatLevel[4][50]['hp'], baseStatLevel[4][50]['atk'], baseStatLevel[4][50]['def'], baseStatLevel[4][50]['anomalyProficiency'], baseStatLevel[4][50]['anomalyMastery'], baseStatLevel[4][50]['impact'] = (6808, 486, 519, 90, 93, 88)
	baseStatLevel[5][50]['hp'], baseStatLevel[5][50]['atk'], baseStatLevel[5][50]['def'], baseStatLevel[5][50]['anomalyProficiency'], baseStatLevel[5][50]['anomalyMastery'], baseStatLevel[5][50]['impact'] = (7257, 520, 554, 90, 93, 88)
	baseStatLevel[5][60]['hp'], baseStatLevel[5][60]['atk'], baseStatLevel[5][60]['def'], baseStatLevel[5][60]['anomalyProficiency'], baseStatLevel[5][60]['anomalyMastery'], baseStatLevel[5][60]['impact'] = (8145, 574, 622, 90, 93, 88)


	def __init__(self):
		super().__init__()



class Piper(Agent):
	name = "Piper"
	realName = "Piper Wheel"
	rank = "A"
	attribute = "Physical"
	specialty = "Anomaly"
	faction = "Sons of Calydon"
	attackType = "Slash"
	baseStatLevel = deepcopy(baseStatLevelTemplate)

	baseStatLevel[0][1]['hp'], baseStatLevel[0][1]['atk'], baseStatLevel[0][1]['def'], baseStatLevel[0][1]['anomalyProficiency'], baseStatLevel[0][1]['anomalyMastery'], baseStatLevel[0][1]['impact'] = (561, 109, 49, 116, 118, 86)
	baseStatLevel[0][10]['hp'], baseStatLevel[0][10]['atk'], baseStatLevel[0][10]['def'], baseStatLevel[0][10]['anomalyProficiency'], baseStatLevel[0][10]['anomalyMastery'], baseStatLevel[0][10]['impact'] = (1246, 166, 109, 116, 118, 86)
	baseStatLevel[1][10]['hp'], baseStatLevel[1][10]['atk'], baseStatLevel[1][10]['def'], baseStatLevel[1][10]['anomalyProficiency'], baseStatLevel[1][10]['anomalyMastery'], baseStatLevel[1][10]['impact'] = (1631, 205, 143, 116, 118, 86)
	baseStatLevel[1][20]['hp'], baseStatLevel[1][20]['atk'], baseStatLevel[1][20]['def'], baseStatLevel[1][20]['anomalyProficiency'], baseStatLevel[1][20]['anomalyMastery'], baseStatLevel[1][20]['impact'] = (2392, 270, 210, 116, 118, 86)
	baseStatLevel[2][20]['hp'], baseStatLevel[2][20]['atk'], baseStatLevel[2][20]['def'], baseStatLevel[2][20]['anomalyProficiency'], baseStatLevel[2][20]['anomalyMastery'], baseStatLevel[2][20]['impact'] = (2777, 309, 244, 116, 118, 86)
	baseStatLevel[2][30]['hp'], baseStatLevel[2][30]['atk'], baseStatLevel[2][30]['def'], baseStatLevel[2][30]['anomalyProficiency'], baseStatLevel[2][30]['anomalyMastery'], baseStatLevel[2][30]['impact'] = (3538, 373, 310, 116, 118, 86)
	baseStatLevel[3][30]['hp'], baseStatLevel[3][30]['atk'], baseStatLevel[3][30]['def'], baseStatLevel[3][30]['anomalyProficiency'], baseStatLevel[3][30]['anomalyMastery'], baseStatLevel[3][30]['impact'] = (3923, 412, 343, 116, 118, 86)
	baseStatLevel[3][40]['hp'], baseStatLevel[3][40]['atk'], baseStatLevel[3][40]['def'], baseStatLevel[3][40]['anomalyProficiency'], baseStatLevel[3][40]['anomalyMastery'], baseStatLevel[3][40]['impact'] = (4684, 476, 410, 116, 118, 86)
	baseStatLevel[4][40]['hp'], baseStatLevel[4][40]['atk'], baseStatLevel[4][40]['def'], baseStatLevel[4][40]['anomalyProficiency'], baseStatLevel[4][40]['anomalyMastery'], baseStatLevel[4][40]['impact'] = (5069, 515, 444, 116, 118, 86)
	baseStatLevel[4][50]['hp'], baseStatLevel[4][50]['atk'], baseStatLevel[4][50]['def'], baseStatLevel[4][50]['anomalyProficiency'], baseStatLevel[4][50]['anomalyMastery'], baseStatLevel[4][50]['impact'] = (5830, 580, 511, 116, 118, 86)
	baseStatLevel[5][50]['hp'], baseStatLevel[5][50]['atk'], baseStatLevel[5][50]['def'], baseStatLevel[5][50]['anomalyProficiency'], baseStatLevel[5][50]['anomalyMastery'], baseStatLevel[5][50]['impact'] = (6215, 619, 545, 116, 118, 86)
	baseStatLevel[5][60]['hp'], baseStatLevel[5][60]['atk'], baseStatLevel[5][60]['def'], baseStatLevel[5][60]['anomalyProficiency'], baseStatLevel[5][60]['anomalyMastery'], baseStatLevel[5][60]['impact'] = (6976, 683, 612, 116, 118, 86)



	def __init__(self):
		super().__init__()



class Qingyi(Agent):
	name = "Qingyi"
	realName = "Qingyi"
	rank = "S"
	attribute = "Electric"
	specialty = "Stun"
	faction = "Criminal Investigation Special Response Team"
	attackType = "Strike"
	baseStatLevel = deepcopy(baseStatLevelTemplate)

	baseStatLevel[0][1]['hp'], baseStatLevel[0][1]['atk'], baseStatLevel[0][1]['def'], baseStatLevel[0][1]['anomalyProficiency'], baseStatLevel[0][1]['anomalyMastery'], baseStatLevel[0][1]['impact'] = (663, 109, 49, 93, 94, 118)
	baseStatLevel[0][10]['hp'], baseStatLevel[0][10]['atk'], baseStatLevel[0][10]['def'], baseStatLevel[0][10]['anomalyProficiency'], baseStatLevel[0][10]['anomalyMastery'], baseStatLevel[0][10]['impact'] = (1473, 166, 109, 93, 94, 118)
	baseStatLevel[1][10]['hp'], baseStatLevel[1][10]['atk'], baseStatLevel[1][10]['def'], baseStatLevel[1][10]['anomalyProficiency'], baseStatLevel[1][10]['anomalyMastery'], baseStatLevel[1][10]['impact'] = (1928, 205, 143, 93, 94, 118)
	baseStatLevel[1][20]['hp'], baseStatLevel[1][20]['atk'], baseStatLevel[1][20]['def'], baseStatLevel[1][20]['anomalyProficiency'], baseStatLevel[1][20]['anomalyMastery'], baseStatLevel[1][20]['impact'] = (2828, 270, 210, 93, 94, 118)
	baseStatLevel[2][20]['hp'], baseStatLevel[2][20]['atk'], baseStatLevel[2][20]['def'], baseStatLevel[2][20]['anomalyProficiency'], baseStatLevel[2][20]['anomalyMastery'], baseStatLevel[2][20]['impact'] = (3284, 309, 244, 93, 94, 118)
	baseStatLevel[2][30]['hp'], baseStatLevel[2][30]['atk'], baseStatLevel[2][30]['def'], baseStatLevel[2][30]['anomalyProficiency'], baseStatLevel[2][30]['anomalyMastery'], baseStatLevel[2][30]['impact'] = (4184, 373, 310, 93, 94, 118)
	baseStatLevel[3][30]['hp'], baseStatLevel[3][30]['atk'], baseStatLevel[3][30]['def'], baseStatLevel[3][30]['anomalyProficiency'], baseStatLevel[3][30]['anomalyMastery'], baseStatLevel[3][30]['impact'] = (4639, 412, 343, 93, 94, 118)
	baseStatLevel[3][40]['hp'], baseStatLevel[3][40]['atk'], baseStatLevel[3][40]['def'], baseStatLevel[3][40]['anomalyProficiency'], baseStatLevel[3][40]['anomalyMastery'], baseStatLevel[3][40]['impact'] = (5540, 476, 410, 93, 94, 118)
	baseStatLevel[4][40]['hp'], baseStatLevel[4][40]['atk'], baseStatLevel[4][40]['def'], baseStatLevel[4][40]['anomalyProficiency'], baseStatLevel[4][40]['anomalyMastery'], baseStatLevel[4][40]['impact'] = (5995, 515, 444, 93, 94, 118)
	baseStatLevel[4][50]['hp'], baseStatLevel[4][50]['atk'], baseStatLevel[4][50]['def'], baseStatLevel[4][50]['anomalyProficiency'], baseStatLevel[4][50]['anomalyMastery'], baseStatLevel[4][50]['impact'] = (6895, 579, 511, 93, 94, 118)
	baseStatLevel[5][50]['hp'], baseStatLevel[5][50]['atk'], baseStatLevel[5][50]['def'], baseStatLevel[5][50]['anomalyProficiency'], baseStatLevel[5][50]['anomalyMastery'], baseStatLevel[5][50]['impact'] = (7350, 618, 545, 93, 94, 118)
	baseStatLevel[5][60]['hp'], baseStatLevel[5][60]['atk'], baseStatLevel[5][60]['def'], baseStatLevel[5][60]['anomalyProficiency'], baseStatLevel[5][60]['anomalyMastery'], baseStatLevel[5][60]['impact'] = (8250, 683, 612, 93, 94, 118)

	def __init__(self):
		super().__init__()



class Soldier11(Agent):
	name = "Soldier11"
	realName = "Soldier11"
	rank = "S"
	attribute = "Fire"
	specialty = "Attack"
	faction = "Obol Squad"
	attackType = "Slash"
	baseStatLevel = deepcopy(baseStatLevelTemplate)

	baseStatLevel[0][1]['hp'], baseStatLevel[0][1]['atk'], baseStatLevel[0][1]['def'], baseStatLevel[0][1]['anomalyProficiency'], baseStatLevel[0][1]['anomalyMastery'], baseStatLevel[0][1]['impact'] = (617, 128, 49, 94, 93, 93)
	baseStatLevel[0][10]['hp'], baseStatLevel[0][10]['atk'], baseStatLevel[0][10]['def'], baseStatLevel[0][10]['anomalyProficiency'], baseStatLevel[0][10]['anomalyMastery'], baseStatLevel[0][10]['impact'] = (1370, 197, 109, 94, 93, 93)
	baseStatLevel[1][10]['hp'], baseStatLevel[1][10]['atk'], baseStatLevel[1][10]['def'], baseStatLevel[1][10]['anomalyProficiency'], baseStatLevel[1][10]['anomalyMastery'], baseStatLevel[1][10]['impact'] = (1793, 243, 143, 94, 93, 93)
	baseStatLevel[1][20]['hp'], baseStatLevel[1][20]['atk'], baseStatLevel[1][20]['def'], baseStatLevel[1][20]['anomalyProficiency'], baseStatLevel[1][20]['anomalyMastery'], baseStatLevel[1][20]['impact'] = (2630, 321, 210, 94, 93, 93)
	baseStatLevel[2][20]['hp'], baseStatLevel[2][20]['atk'], baseStatLevel[2][20]['def'], baseStatLevel[2][20]['anomalyProficiency'], baseStatLevel[2][20]['anomalyMastery'], baseStatLevel[2][20]['impact'] = (3054, 366, 244, 94, 93, 93)
	baseStatLevel[2][30]['hp'], baseStatLevel[2][30]['atk'], baseStatLevel[2][30]['def'], baseStatLevel[2][30]['anomalyProficiency'], baseStatLevel[2][30]['anomalyMastery'], baseStatLevel[2][30]['impact'] = (3891, 443, 310, 94, 93, 93)
	baseStatLevel[3][30]['hp'], baseStatLevel[3][30]['atk'], baseStatLevel[3][30]['def'], baseStatLevel[3][30]['anomalyProficiency'], baseStatLevel[3][30]['anomalyMastery'], baseStatLevel[3][30]['impact'] = (4314, 489, 343, 94, 93, 93)
	baseStatLevel[3][40]['hp'], baseStatLevel[3][40]['atk'], baseStatLevel[3][40]['def'], baseStatLevel[3][40]['anomalyProficiency'], baseStatLevel[3][40]['anomalyMastery'], baseStatLevel[3][40]['impact'] = (5152, 567, 410, 94, 93, 93)
	baseStatLevel[4][40]['hp'], baseStatLevel[4][40]['atk'], baseStatLevel[4][40]['def'], baseStatLevel[4][40]['anomalyProficiency'], baseStatLevel[4][40]['anomalyMastery'], baseStatLevel[4][40]['impact'] = (5576, 613, 444, 94, 93, 93)
	baseStatLevel[4][50]['hp'], baseStatLevel[4][50]['atk'], baseStatLevel[4][50]['def'], baseStatLevel[4][50]['anomalyProficiency'], baseStatLevel[4][50]['anomalyMastery'], baseStatLevel[4][50]['impact'] = (6413, 691, 511, 94, 93, 93)
	baseStatLevel[5][50]['hp'], baseStatLevel[5][50]['atk'], baseStatLevel[5][50]['def'], baseStatLevel[5][50]['anomalyProficiency'], baseStatLevel[5][50]['anomalyMastery'], baseStatLevel[5][50]['impact'] = (6836, 736, 545, 94, 93, 93)
	baseStatLevel[5][60]['hp'], baseStatLevel[5][60]['atk'], baseStatLevel[5][60]['def'], baseStatLevel[5][60]['anomalyProficiency'], baseStatLevel[5][60]['anomalyMastery'], baseStatLevel[5][60]['impact'] = (7673, 813, 612, 94, 93, 93)


	def __init__(self):
		super().__init__()



class Soukaku(Agent):
	name = "Soukaku"
	realName = "Soukaku"
	rank = "A"
	attribute = "Ice"
	specialty = "Support"
	faction = "Section 6"
	attackType = "Slash"
	baseStatLevel = deepcopy(baseStatLevelTemplate)

	baseStatLevel[0][1]['hp'], baseStatLevel[0][1]['atk'], baseStatLevel[0][1]['def'], baseStatLevel[0][1]['anomalyProficiency'], baseStatLevel[0][1]['anomalyMastery'], baseStatLevel[0][1]['impact'] = (645, 96, 48, 93, 96, 86)
	baseStatLevel[0][10]['hp'], baseStatLevel[0][10]['atk'], baseStatLevel[0][10]['def'], baseStatLevel[0][10]['anomalyProficiency'], baseStatLevel[0][10]['anomalyMastery'], baseStatLevel[0][10]['impact'] = (1433, 145, 106, 93, 96, 86)
	baseStatLevel[1][10]['hp'], baseStatLevel[1][10]['atk'], baseStatLevel[1][10]['def'], baseStatLevel[1][10]['anomalyProficiency'], baseStatLevel[1][10]['anomalyMastery'], baseStatLevel[1][10]['impact'] = (1876, 179, 139, 93, 96, 86)
	baseStatLevel[1][20]['hp'], baseStatLevel[1][20]['atk'], baseStatLevel[1][20]['def'], baseStatLevel[1][20]['anomalyProficiency'], baseStatLevel[1][20]['anomalyMastery'], baseStatLevel[1][20]['impact'] = (2751, 234, 204, 93, 96, 86)
	baseStatLevel[2][20]['hp'], baseStatLevel[2][20]['atk'], baseStatLevel[2][20]['def'], baseStatLevel[2][20]['anomalyProficiency'], baseStatLevel[2][20]['anomalyMastery'], baseStatLevel[2][20]['impact'] = (3194, 268, 237, 93, 96, 86)
	baseStatLevel[2][30]['hp'], baseStatLevel[2][30]['atk'], baseStatLevel[2][30]['def'], baseStatLevel[2][30]['anomalyProficiency'], baseStatLevel[2][30]['anomalyMastery'], baseStatLevel[2][30]['impact'] = (4070, 323, 303, 93, 96, 86)
	baseStatLevel[3][30]['hp'], baseStatLevel[3][30]['atk'], baseStatLevel[3][30]['def'], baseStatLevel[3][30]['anomalyProficiency'], baseStatLevel[3][30]['anomalyMastery'], baseStatLevel[3][30]['impact'] = (4513, 358, 336, 93, 96, 86)
	baseStatLevel[3][40]['hp'], baseStatLevel[3][40]['atk'], baseStatLevel[3][40]['def'], baseStatLevel[3][40]['anomalyProficiency'], baseStatLevel[3][40]['anomalyMastery'], baseStatLevel[3][40]['impact'] = (5389, 413, 401, 93, 96, 86)
	baseStatLevel[4][40]['hp'], baseStatLevel[4][40]['atk'], baseStatLevel[4][40]['def'], baseStatLevel[4][40]['anomalyProficiency'], baseStatLevel[4][40]['anomalyMastery'], baseStatLevel[4][40]['impact'] = (5832, 447, 434, 93, 96, 86)
	baseStatLevel[4][50]['hp'], baseStatLevel[4][50]['atk'], baseStatLevel[4][50]['def'], baseStatLevel[4][50]['anomalyProficiency'], baseStatLevel[4][50]['anomalyMastery'], baseStatLevel[4][50]['impact'] = (6708, 501, 499, 93, 96, 86)
	baseStatLevel[5][50]['hp'], baseStatLevel[5][50]['atk'], baseStatLevel[5][50]['def'], baseStatLevel[5][50]['anomalyProficiency'], baseStatLevel[5][50]['anomalyMastery'], baseStatLevel[5][50]['impact'] = (7150, 535, 532, 93, 96, 86)
	baseStatLevel[5][60]['hp'], baseStatLevel[5][60]['atk'], baseStatLevel[5][60]['def'], baseStatLevel[5][60]['anomalyProficiency'], baseStatLevel[5][60]['anomalyMastery'], baseStatLevel[5][60]['impact'] = (8025, 590, 597, 93, 96, 86)

	def __init__(self):
		super().__init__()



class Lycaon(Agent):
	name = "Lycaon"
	realName = "Von Lycaon"
	rank = "S"
	attribute = "Ice"
	specialty = "Stun"
	faction = "Victoria Housekeeping"
	attackType = "Strike"
	baseStatLevel = deepcopy(baseStatLevelTemplate)

	baseStatLevel[0][1]['hp'], baseStatLevel[0][1]['atk'], baseStatLevel[0][1]['def'], baseStatLevel[0][1]['anomalyProficiency'], baseStatLevel[0][1]['anomalyMastery'], baseStatLevel[0][1]['impact'] = (677, 105, 49, 91, 90, 119)
	baseStatLevel[0][10]['hp'], baseStatLevel[0][10]['atk'], baseStatLevel[0][10]['def'], baseStatLevel[0][10]['anomalyProficiency'], baseStatLevel[0][10]['anomalyMastery'], baseStatLevel[0][10]['impact'] = (1503, 160, 108, 91, 90, 119)
	baseStatLevel[1][10]['hp'], baseStatLevel[1][10]['atk'], baseStatLevel[1][10]['def'], baseStatLevel[1][10]['anomalyProficiency'], baseStatLevel[1][10]['anomalyMastery'], baseStatLevel[1][10]['impact'] = (1967, 197, 141, 91, 90, 119)
	baseStatLevel[1][20]['hp'], baseStatLevel[1][20]['atk'], baseStatLevel[1][20]['def'], baseStatLevel[1][20]['anomalyProficiency'], baseStatLevel[1][20]['anomalyMastery'], baseStatLevel[1][20]['impact'] = (2885, 258, 207, 91, 90, 119)
	baseStatLevel[2][20]['hp'], baseStatLevel[2][20]['atk'], baseStatLevel[2][20]['def'], baseStatLevel[2][20]['anomalyProficiency'], baseStatLevel[2][20]['anomalyMastery'], baseStatLevel[2][20]['impact'] = (3350, 296, 241, 91, 90, 119)
	baseStatLevel[2][30]['hp'], baseStatLevel[2][30]['atk'], baseStatLevel[2][30]['def'], baseStatLevel[2][30]['anomalyProficiency'], baseStatLevel[2][30]['anomalyMastery'], baseStatLevel[2][30]['impact'] = (4268, 357, 307, 91, 90, 119)
	baseStatLevel[3][30]['hp'], baseStatLevel[3][30]['atk'], baseStatLevel[3][30]['def'], baseStatLevel[3][30]['anomalyProficiency'], baseStatLevel[3][30]['anomalyMastery'], baseStatLevel[3][30]['impact'] = (4732, 394, 340, 91, 90, 119)
	baseStatLevel[3][40]['hp'], baseStatLevel[3][40]['atk'], baseStatLevel[3][40]['def'], baseStatLevel[3][40]['anomalyProficiency'], baseStatLevel[3][40]['anomalyMastery'], baseStatLevel[3][40]['impact'] = (5650, 456, 407, 91, 90, 119)
	baseStatLevel[4][40]['hp'], baseStatLevel[4][40]['atk'], baseStatLevel[4][40]['def'], baseStatLevel[4][40]['anomalyProficiency'], baseStatLevel[4][40]['anomalyMastery'], baseStatLevel[4][40]['impact'] = (6114, 494, 441, 91, 90, 119)
	baseStatLevel[4][50]['hp'], baseStatLevel[4][50]['atk'], baseStatLevel[4][50]['def'], baseStatLevel[4][50]['anomalyProficiency'], baseStatLevel[4][50]['anomalyMastery'], baseStatLevel[4][50]['impact'] = (7033, 555, 507, 91, 90, 119)
	baseStatLevel[5][50]['hp'], baseStatLevel[5][50]['atk'], baseStatLevel[5][50]['def'], baseStatLevel[5][50]['anomalyProficiency'], baseStatLevel[5][50]['anomalyMastery'], baseStatLevel[5][50]['impact'] = (7498, 592, 540, 91, 90, 119)
	baseStatLevel[5][60]['hp'], baseStatLevel[5][60]['atk'], baseStatLevel[5][60]['def'], baseStatLevel[5][60]['anomalyProficiency'], baseStatLevel[5][60]['anomalyMastery'], baseStatLevel[5][60]['impact'] = (8416, 653, 606, 91, 90, 119)

	def __init__(self):
		super().__init__()



class Yuan(Agent):
	name = "Yuan"
	realName = "Zhu Yuan"
	rank = "S"
	attribute = "Ether"
	specialty = "Attack"
	faction = "Criminal Investigation Special Response Team"
	attackType = "Pierce"
	baseStatLevel = deepcopy(baseStatLevelTemplate)
		
	baseStatLevel[0][1]['hp'], baseStatLevel[0][1]['atk'], baseStatLevel[0][1]['def'], baseStatLevel[0][1]['anomalyProficiency'], baseStatLevel[0][1]['anomalyMastery'], baseStatLevel[0][1]['impact'] = (602, 132, 48, 93, 92, 90)
	baseStatLevel[0][10]['hp'], baseStatLevel[0][10]['atk'], baseStatLevel[0][10]['def'], baseStatLevel[0][10]['anomalyProficiency'], baseStatLevel[0][10]['anomalyMastery'], baseStatLevel[0][10]['impact'] = (1336, 204, 106, 93, 92, 90)
	baseStatLevel[1][10]['hp'], baseStatLevel[1][10]['atk'], baseStatLevel[1][10]['def'], baseStatLevel[1][10]['anomalyProficiency'], baseStatLevel[1][10]['anomalyMastery'], baseStatLevel[1][10]['impact'] = (1749, 251, 139, 93, 92, 90)
	baseStatLevel[1][20]['hp'], baseStatLevel[1][20]['atk'], baseStatLevel[1][20]['def'], baseStatLevel[1][20]['anomalyProficiency'], baseStatLevel[1][20]['anomalyMastery'], baseStatLevel[1][20]['impact'] = (2566, 332, 205, 93, 92, 90)
	baseStatLevel[2][20]['hp'], baseStatLevel[2][20]['atk'], baseStatLevel[2][20]['def'], baseStatLevel[2][20]['anomalyProficiency'], baseStatLevel[2][20]['anomalyMastery'], baseStatLevel[2][20]['impact'] = (2979, 380, 238, 93, 92, 90)
	baseStatLevel[2][30]['hp'], baseStatLevel[2][30]['atk'], baseStatLevel[2][30]['def'], baseStatLevel[2][30]['anomalyProficiency'], baseStatLevel[2][30]['anomalyMastery'], baseStatLevel[2][30]['impact'] = (3795, 461, 304, 93, 92, 90)
	baseStatLevel[3][30]['hp'], baseStatLevel[3][30]['atk'], baseStatLevel[3][30]['def'], baseStatLevel[3][30]['anomalyProficiency'], baseStatLevel[3][30]['anomalyMastery'], baseStatLevel[3][30]['impact'] = (4208, 508, 337, 93, 92, 90)
	baseStatLevel[3][40]['hp'], baseStatLevel[3][40]['atk'], baseStatLevel[3][40]['def'], baseStatLevel[3][40]['anomalyProficiency'], baseStatLevel[3][40]['anomalyMastery'], baseStatLevel[3][40]['impact'] = (5024, 588, 402, 93, 92, 90)
	baseStatLevel[4][40]['hp'], baseStatLevel[4][40]['atk'], baseStatLevel[4][40]['def'], baseStatLevel[4][40]['anomalyProficiency'], baseStatLevel[4][40]['anomalyMastery'], baseStatLevel[4][40]['impact'] = (5436, 635, 436, 93, 92, 90)
	baseStatLevel[4][50]['hp'], baseStatLevel[4][50]['atk'], baseStatLevel[4][50]['def'], baseStatLevel[4][50]['anomalyProficiency'], baseStatLevel[4][50]['anomalyMastery'], baseStatLevel[4][50]['impact'] = (6253, 716, 502, 93, 92, 90)
	baseStatLevel[5][50]['hp'], baseStatLevel[5][50]['atk'], baseStatLevel[5][50]['def'], baseStatLevel[5][50]['anomalyProficiency'], baseStatLevel[5][50]['anomalyMastery'], baseStatLevel[5][50]['impact'] = (6666, 763, 535, 93, 92, 90)
	baseStatLevel[5][60]['hp'], baseStatLevel[5][60]['atk'], baseStatLevel[5][60]['def'], baseStatLevel[5][60]['anomalyProficiency'], baseStatLevel[5][60]['anomalyMastery'], baseStatLevel[5][60]['impact'] = (7482, 844, 600, 93, 92, 90)

	def __init__(self):
		super().__init__()



agents: dict[str, Type[Agent]] = {
	# S rank
	"Rina": Rina,
	"Ellen": Ellen,
	"Grace": Grace,
	"Koleda": Koleda,
	"Nekomata": Nekomata,
	"Qingyi": Qingyi,
	"Soldier11": Soldier11,
	"Lycaon": Lycaon,
	"Yuan": Yuan,

	# A rank
	"Anby": Anby,
	"Anton": Anton,
	"Ben": Ben,
	"Billy": Billy,
	"Corin": Corin,
	"Lucy": Lucy,
	"Nicole": Nicole,
	"Piper": Piper,
	"Soukaku": Soukaku,

}

