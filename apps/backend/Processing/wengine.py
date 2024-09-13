import config

from typing import Literal, Union, Type

from copy import deepcopy

"combat+addition+increase+squad+next+enemy-skill2*type+skil2*type2"



baseStatLevelTemplate: dict[
	Literal['mainStat', 'subStat'], dict[
		Literal[0, 1, 2, 3, 4, 5], dict[
			Literal[0, 10, 20, 30, 40, 50, 60], float
		]
	]
] = {
	'mainStat': {
		0: {
			0: 0,
			10: 0
		},
		1: {
			10: 0,
			20: 0
		},
		2: {
			20: 0,
			30: 0
		},
		3: {
			30: 0,
			40: 0
		},
		4: {
			40: 0,
			50: 0
		},
		5: {
			50: 0,
			60: 0
		},
	},
	'subStat': {
		0: {
			0: 0,
			10: 0
		},
		1: {
			10: 0,
			20: 0
		},
		2: {
			20: 0,
			30: 0
		},
		3: {
			30: 0,
			40: 0
		},
		4: {
			40: 0,
			50: 0
		},
		5: {
			50: 0,
			60: 0
		},
	}
}


class WEngine:
	name: str
	rank: config.RANKS
	specialty: config.SPECIALTY
	modificationLevel: Literal[0, 1, 2, 3, 4, 5]
	level: int 
	upgradeLevel: Literal[1, 2, 3, 4, 5]

	mainStat: str
	subStat: str

	baseStatLevel: dict[
		Literal['mainStat', 'subStat'], dict[
			Literal[0, 1, 2, 3, 4, 5], dict[
				Literal[0, 10, 20, 30, 40, 50, 60], float
			]
		]
	]

	passiveDescription: str
	passiveStats: dict[str, dict[str, list[float] | float | str]]


	def __init__(self):
		self.modificationLevel = 0
		self.level = 0
		self.upgradeLevel = 1


	def fromJson(self, data: dict):
		pass

	def loadBaseStat(self, data):
		self.baseStatLevel = data

	def setLevel(self, value):
		self.level = value

	@classmethod
	def getStat(cls, modification: Literal[0,1,2,3,4,5] = 0, level: int = 0) -> dict[str, tuple[str, float]]:
		levelmin = modification*10
		levelmax = levelmin+10

		mainStatmin = cls.baseStatLevel['mainStat'][modification][levelmin]
		mainStatmax = cls.baseStatLevel['mainStat'][modification][levelmax]

		subStatmin = cls.baseStatLevel['subStat'][modification][levelmin]
		subStatmax = cls.baseStatLevel['subStat'][modification][levelmax]

		mainStat = (mainStatmax-mainStatmin)*(level-levelmin) / 10 + mainStatmin
		subStat = (subStatmax-subStatmin)*(level-levelmin) / 10 + subStatmin

		return {"mainStat": (cls.mainStat, mainStat), "subStat": (cls.subStat, subStat)}

	@classmethod
	def getPassive(cls, upgrade: Literal[1,2,3,4,5] = 1):
		passive = cls.passiveDescription.format(*[passiveStat['value'][upgrade-1] for passiveStat in cls.passiveStats.values()]) # type: ignore

		return {"passive": passive}
		


class DeepSeaVisitor(WEngine):
	name = "Deep Sea Visitor"
	rank = 'S'
	specialty = 'Attack'
	mainStat = 'atk'
	subStat = 'critRate_'

	baseStatLevel = deepcopy(baseStatLevelTemplate)
	baseStatLevel['mainStat'][0][00], baseStatLevel['subStat'][0][0] = 48 , 9.6
	baseStatLevel['mainStat'][0][10], baseStatLevel['subStat'][0][10] = 123, 9.6
	baseStatLevel['mainStat'][1][10], baseStatLevel['subStat'][1][10] = 166, 12.5
	baseStatLevel['mainStat'][1][20], baseStatLevel['subStat'][1][20] = 241, 12.5
	baseStatLevel['mainStat'][2][20], baseStatLevel['subStat'][2][20] = 284, 15.4
	baseStatLevel['mainStat'][2][30], baseStatLevel['subStat'][2][30] = 359, 15.4
	baseStatLevel['mainStat'][3][30], baseStatLevel['subStat'][3][30] = 402, 18.2
	baseStatLevel['mainStat'][3][40], baseStatLevel['subStat'][3][40] = 477, 18.2
	baseStatLevel['mainStat'][4][40], baseStatLevel['subStat'][4][40] = 520, 21.1
	baseStatLevel['mainStat'][4][50], baseStatLevel['subStat'][4][50] = 595, 21.1
	baseStatLevel['mainStat'][5][50], baseStatLevel['subStat'][5][50] = 638, 24.0
	baseStatLevel['mainStat'][5][60], baseStatLevel['subStat'][5][60] = 713, 24.0

	passiveStats = {
		"iceDMG_": {
			"value": [25, 31.5, 38, 44.5, 50]
		},
		"combat-critRate_": {
			"value": [10, 12.5, 15, 17.5, 20],
			"multiple": 1,
			"description": "..."
		}, 
		"combat-critRate_ 2": {
			"value": [10, 12.5, 15, 17.5, 20],
			"multiple": 1,
			"description": "..."
		}, 
	}

	passiveDescription = "<p>Increases <span style=\"color: rgb(140,216,218)\">Ice DMG</span> by <span style=\"color: rgb(237,197,84)\">{0}%</span>. Upon hitting an enemy with a Basic Attack, the equipper's CRIT Rate increases by <span style=\"color: rgb(237,197,84)\">{1}%</span> for 8s. When dealing <span style=\"color: rgb(140,216,218)\">Ice DMG</span> with a Dash Attack, the equipper's CRIT Rate increases by an additional <span style=\"color: rgb(237,197,84)\">{2}%</span> for 15s. The duration of each effect is calculated separately.</p>"
	
	def __init__(self):
		super().__init__()





class FusionCompiler(WEngine):
	name = "Fusion Compiler"
	rank = "S"
	specialty = "Anomaly"
	mainStat = "atk"
	subStat = "pen_"
	baseStatLevel = deepcopy(baseStatLevelTemplate)	
	baseStatLevel['mainStat'][0][0], baseStatLevel['subStat'][0][0] = 46 , 9.6
	baseStatLevel['mainStat'][0][10], baseStatLevel['subStat'][0][10] = 118 , 9.6
	baseStatLevel['mainStat'][1][10], baseStatLevel['subStat'][1][10] = 159 , 12.5
	baseStatLevel['mainStat'][1][20], baseStatLevel['subStat'][1][20] = 231 , 12.5
	baseStatLevel['mainStat'][2][20], baseStatLevel['subStat'][2][20] = 272 , 15.4
	baseStatLevel['mainStat'][2][30], baseStatLevel['subStat'][2][30] = 344 , 15.4
	baseStatLevel['mainStat'][3][30], baseStatLevel['subStat'][3][30] = 385 , 18.2
	baseStatLevel['mainStat'][3][40], baseStatLevel['subStat'][3][40] = 457 , 18.2
	baseStatLevel['mainStat'][4][40], baseStatLevel['subStat'][4][40] = 498 , 21.1
	baseStatLevel['mainStat'][4][50], baseStatLevel['subStat'][4][50] = 570 , 21.1
	baseStatLevel['mainStat'][5][50], baseStatLevel['subStat'][5][50] = 611 , 24.0
	baseStatLevel['mainStat'][5][60], baseStatLevel['subStat'][5][60] = 684 , 24.0

	passiveStats = {
			"atk_": {
				"value": [12, 15, 18, 21, 24]
			},
			"combat-anomalyProficiency": {
				"value": [25, 31, 37, 43, 50],
				"multiple": 3,
				"description": "..."
			},
		}

	passiveDescription = "<p>Increases ATK by <span style=\"color: rgb(237,197,84)\">{0}%</span>. When using a Special Attack or EX Special Attack, the equipper's Anomaly Proficiency is increased by <span style=\"color: rgb(237,197,84)\">{1}</span> for 8, stacking up to 3 times. The duration of each stack is calculated separately.</p>"
	def __init__(self):
		super().__init__()





class HellfireGears(WEngine):
	name = "Hellfire Gears"
	rank = "S"
	specialty = "Stun"
	mainStat = "atk"
	subStat = "impact_"
	baseStatLevel = deepcopy(baseStatLevelTemplate)
	baseStatLevel['mainStat'][0][0], baseStatLevel['subStat'][0][0] = 46 , 7.2
	baseStatLevel['mainStat'][0][10], baseStatLevel['subStat'][0][10] = 118 , 7.2
	baseStatLevel['mainStat'][1][10], baseStatLevel['subStat'][1][10] = 159 , 9.4
	baseStatLevel['mainStat'][1][20], baseStatLevel['subStat'][1][20] = 231 , 9.4
	baseStatLevel['mainStat'][2][20], baseStatLevel['subStat'][2][20] = 272 , 11.5
	baseStatLevel['mainStat'][2][30], baseStatLevel['subStat'][2][30] = 344 , 11.5
	baseStatLevel['mainStat'][3][30], baseStatLevel['subStat'][3][30] = 385 , 13.7
	baseStatLevel['mainStat'][3][40], baseStatLevel['subStat'][3][40] = 457 , 13.7
	baseStatLevel['mainStat'][4][40], baseStatLevel['subStat'][4][40] = 498 , 15.8
	baseStatLevel['mainStat'][4][50], baseStatLevel['subStat'][4][50] = 570 , 15.8
	baseStatLevel['mainStat'][5][50], baseStatLevel['subStat'][5][50] = 611 , 18.0
	baseStatLevel['mainStat'][5][60], baseStatLevel['subStat'][5][60] = 684 , 18.0

	passiveStats = {
			"combat-energyRegen": {
				"value": [0.6, 0.75, 0.9, 1.5, 1.2],
				"multiple": "inf",
				"description": "..."
			},
			"combat-impact_": {
				"value": [10, 12.5, 15, 17.5, 20],
				"multiple": 2,
				"description": "..."
			},
		}


	passiveDescription = "<p>When off-field, the equipper's Energy Regen increases by <span style=\"color: rgb(237,197,84)\">{0}</span> per second. When using an EX Special Attack, the equipper's Impact is increased by <span style=\"color: rgb(237,197,84)\">{1}</span> for 10s, stacking up to 2 times. The duration of each stack is calculated separately.</p>"
	def __init__(self):
		super().__init__()






class IceJadeTeapot(WEngine):
	name = "Ice-Jade Teapot"
	rank = "S"
	specialty = "Stun"
	mainStat = "atk"
	subStat = "impact_"
	baseStatLevel = deepcopy(baseStatLevelTemplate)

	baseStatLevel['mainStat'][0][0], baseStatLevel['subStat'][0][0] = 48 , 7.2
	baseStatLevel['mainStat'][0][10], baseStatLevel['subStat'][0][10] = 123 , 7.2
	baseStatLevel['mainStat'][1][10], baseStatLevel['subStat'][1][10] = 166 , 9.4
	baseStatLevel['mainStat'][1][20], baseStatLevel['subStat'][1][20] = 241 , 9.4
	baseStatLevel['mainStat'][2][20], baseStatLevel['subStat'][2][20] = 284 , 11.5
	baseStatLevel['mainStat'][2][30], baseStatLevel['subStat'][2][30] = 359 , 11.5
	baseStatLevel['mainStat'][3][30], baseStatLevel['subStat'][3][30] = 402 , 13.7
	baseStatLevel['mainStat'][3][40], baseStatLevel['subStat'][3][40] = 477 , 13.7
	baseStatLevel['mainStat'][4][40], baseStatLevel['subStat'][4][40] = 520 , 15.8
	baseStatLevel['mainStat'][4][50], baseStatLevel['subStat'][4][50] = 595 , 15.8
	baseStatLevel['mainStat'][5][50], baseStatLevel['subStat'][5][50] = 638 , 18.0
	baseStatLevel['mainStat'][5][60], baseStatLevel['subStat'][5][60] = 713 , 18.0

	passiveStats = {
			"combat-impact_": {
				"value": [0.7, 0.88, 1.05, 1.22, 1.4],
				"multiple": 30,
				"description": "..."
			},
			"squad-DMG_": {
				"value": [20, 23, 26, 29, 32],
				"multiple": 1,
				"description": "...",
				"stackable": False
			}
		}


	passiveDescription = "<p>When a Basic Attack hits an enemy, gain 1 stack of Tea-riffic. Each stack of Tea-riffic increases the user's Impact by <span style=\"color: rgb(237,197,84)\">{0}%</span>, stacking up to 30 times, and lasting for 8s. The duration of each stack is calculated separately. Upon acquiring Tea-riffic, if the equipper possesses stacks of Tea-riffic greater than or equal to 15, all squad members' DMG is increased by <span style=\"color: rgb(237,197,84)\">{1}%</span> for 10s. Passive effects of the same name do not stack.</p>"
	def __init__(self):
		super().__init__()






class RiotSuppressorMarkVI(WEngine):
	name = "Riot Suppressor Mark VI"
	rank = "S"
	specialty = "Attack"
	mainStat = "atk"
	subStat = "critDMG_"
	baseStatLevel = deepcopy(baseStatLevelTemplate)
	baseStatLevel['mainStat'][0][0], baseStatLevel['subStat'][0][0] = 48 , 19.2
	baseStatLevel['mainStat'][0][10], baseStatLevel['subStat'][0][10] = 123 , 19.2
	baseStatLevel['mainStat'][1][10], baseStatLevel['subStat'][1][10] = 166 , 25.0
	baseStatLevel['mainStat'][1][20], baseStatLevel['subStat'][1][20] = 241 , 25.0
	baseStatLevel['mainStat'][2][20], baseStatLevel['subStat'][2][20] = 284 , 30.7
	baseStatLevel['mainStat'][2][30], baseStatLevel['subStat'][2][30] = 359 , 30.7
	baseStatLevel['mainStat'][3][30], baseStatLevel['subStat'][3][30] = 402 , 36.5
	baseStatLevel['mainStat'][3][40], baseStatLevel['subStat'][3][40] = 477 , 36.5
	baseStatLevel['mainStat'][4][40], baseStatLevel['subStat'][4][40] = 520 , 42.2
	baseStatLevel['mainStat'][4][50], baseStatLevel['subStat'][4][50] = 595 , 42.2
	baseStatLevel['mainStat'][5][50], baseStatLevel['subStat'][5][50] = 638 , 48.0
	baseStatLevel['mainStat'][5][60], baseStatLevel['subStat'][5][60] = 713 , 48.0

	passiveStats = {
			"critRate_": {
				"value": [15, 18.8, 22.6, 26.4, 30]
			}, 
			"combat-etherDMG_": {
				"value": [35, 43.5, 52, 60.5, 70],
				"multiple": 1,
				"description": "..."
			}
		}


	passiveDescription = "<p>Increases CRIT Rate by <span style=\"color: rgb(237,197,84)\">{0}%</span>. Launching an EX Special Attack grants the equipper 8 Charge stacks, up to a maximum of 8 stacks. Whenever the equipper's Basic Attack deals <span style=\"color: rgb(217,64,112)\">Ether DMG</span>, consumes a Charge stack and increases the skill's DMG by <span style=\"color: rgb(237,197,84)\">{1}%</span>.</p>"

	def __init__(self):
		super().__init__()




class SteelCushion(WEngine):
	name = "Steel Cushion"
	rank = "S"
	specialty = "Attack"
	mainStat = "atk"
	subStat = "critRate_"
	baseStatLevel = deepcopy(baseStatLevelTemplate)
	baseStatLevel['mainStat'][0][0], baseStatLevel['subStat'][0][0] = 46 , 9.6
	baseStatLevel['mainStat'][0][10], baseStatLevel['subStat'][0][10] = 118 , 9.6
	baseStatLevel['mainStat'][1][10], baseStatLevel['subStat'][1][10] = 159 , 12.5
	baseStatLevel['mainStat'][1][20], baseStatLevel['subStat'][1][20] = 231 , 12.5
	baseStatLevel['mainStat'][2][20], baseStatLevel['subStat'][2][20] = 272 , 15.4
	baseStatLevel['mainStat'][2][30], baseStatLevel['subStat'][2][30] = 344 , 15.4
	baseStatLevel['mainStat'][3][30], baseStatLevel['subStat'][3][30] = 385 , 18.2
	baseStatLevel['mainStat'][3][40], baseStatLevel['subStat'][3][40] = 457 , 18.2
	baseStatLevel['mainStat'][4][40], baseStatLevel['subStat'][4][40] = 498 , 21.1
	baseStatLevel['mainStat'][4][50], baseStatLevel['subStat'][4][50] = 570 , 21.1
	baseStatLevel['mainStat'][5][50], baseStatLevel['subStat'][5][50] = 611 , 24.0
	baseStatLevel['mainStat'][5][60], baseStatLevel['subStat'][5][60] = 684 , 24.0

	passiveStats = {
			"physicalDMG_": {
				"value": [20, 25, 30, 35, 40],
			},
			"combat-DMG_": {
				"value": [25, 31.5, 38, 44, 50],
				"mutiple": 1,
				"description": "..."
			}
		}

	passiveDescription = "<p>Increases <span style=\"color: rgb(192,168,47)\">Physical DMG</span> by <span style=\"color: rgb(237,197,84)\">{0}%s</span>. The equipper's DMG increases by <span style=\"color: rgb(237,197,84)\">{1}</span> when attacking the enemy from behind.</p>"


	def __init__(self):
		super().__init__()




class TheBrimstone(WEngine):
	name = "The Brimstone"
	rank = "S"
	specialty = "Attack"
	mainStat = "atk"
	subStat = "atk_"
	baseStatLevel = deepcopy(baseStatLevelTemplate)
	baseStatLevel['mainStat'][0][0], baseStatLevel['subStat'][0][0] = 46 , 12.0
	baseStatLevel['mainStat'][0][10], baseStatLevel['subStat'][0][10] = 118 , 12.0
	baseStatLevel['mainStat'][1][10], baseStatLevel['subStat'][1][10] = 159 , 15.6
	baseStatLevel['mainStat'][1][20], baseStatLevel['subStat'][1][20] = 231 , 15.6
	baseStatLevel['mainStat'][2][20], baseStatLevel['subStat'][2][20] = 272 , 19.2
	baseStatLevel['mainStat'][2][30], baseStatLevel['subStat'][2][30] = 344 , 19.2
	baseStatLevel['mainStat'][3][30], baseStatLevel['subStat'][3][30] = 385 , 22.8
	baseStatLevel['mainStat'][3][40], baseStatLevel['subStat'][3][40] = 457 , 22.8
	baseStatLevel['mainStat'][4][40], baseStatLevel['subStat'][4][40] = 498 , 26.4
	baseStatLevel['mainStat'][4][50], baseStatLevel['subStat'][4][50] = 570 , 26.4
	baseStatLevel['mainStat'][5][50], baseStatLevel['subStat'][5][50] = 611 , 30.0
	baseStatLevel['mainStat'][5][60], baseStatLevel['subStat'][5][60] = 684 , 30.0

	passiveStats = {
			"combat-atk_": {
				"value": [3.5, 4.4, 5.2, 6, 7],
				"multiple": 8,
				"description": "..."
			}
		}

	passiveDescription = "<p>Upon hitting an enemy with a Basic Attack, Dash Attack, or Dodge Counter, the equipper's ATK increases by <span style=\"color: rgb(237,197,84)\">{0}%</span> for 8s, stacking up to 8 times. This effect can trigger once every 0.5s. The duration of each stack is calculated separately.</p>"


	def __init__(self):
		super().__init__()




class TheRestrained(WEngine):
	name = "The Restrained"
	rank = "S"
	specialty = "Stun"
	mainStat = "atk"
	subStat = "impact_"
	baseStatLevel = deepcopy(baseStatLevelTemplate)
	baseStatLevel['mainStat'][0][0], baseStatLevel['subStat'][0][0] = 46 , 7.2
	baseStatLevel['mainStat'][0][10], baseStatLevel['subStat'][0][10] = 118 , 7.2
	baseStatLevel['mainStat'][1][10], baseStatLevel['subStat'][1][10] = 159 , 9.4
	baseStatLevel['mainStat'][1][20], baseStatLevel['subStat'][1][20] = 231 , 9.4
	baseStatLevel['mainStat'][2][20], baseStatLevel['subStat'][2][20] = 272 , 11.5
	baseStatLevel['mainStat'][2][30], baseStatLevel['subStat'][2][30] = 344 , 11.5
	baseStatLevel['mainStat'][3][30], baseStatLevel['subStat'][3][30] = 385 , 13.7
	baseStatLevel['mainStat'][3][40], baseStatLevel['subStat'][3][40] = 457 , 13.7
	baseStatLevel['mainStat'][4][40], baseStatLevel['subStat'][4][40] = 498 , 15.8
	baseStatLevel['mainStat'][4][50], baseStatLevel['subStat'][4][50] = 570 , 15.8
	baseStatLevel['mainStat'][5][50], baseStatLevel['subStat'][5][50] = 611 , 18.0
	baseStatLevel['mainStat'][5][60], baseStatLevel['subStat'][5][60] = 684 , 18.0

	passiveStats = {
			"combat-basic*daze_+basic*DMG_": {
				"value": [6, 7.5, 9, 10.5, 12],
				"multiple": 5,
				"description": "..."
			}
		}

	passiveDescription = "<p>When an attack hits an enemy, DMG and Daze from Basic Attacks increase by <span style=\"color: rgb(237,197,84)\">{0}%</span> for 8s, stacking up to 5 times. This effect can trigger at most once during each skill. The duration of each stack is calculated separately.</p>"


	def __init__(self):
		super().__init__()




class WeepingCradle(WEngine):
	name = "Weeping Cradle"
	rank = "S"
	specialty = "Support"
	mainStat = "atk"
	subStat = "pen_"
	baseStatLevel = deepcopy(baseStatLevelTemplate)
	baseStatLevel['mainStat'][0][0], baseStatLevel['subStat'][0][0] = 46 , 9.6
	baseStatLevel['mainStat'][0][10], baseStatLevel['subStat'][0][10] = 118 , 9.6
	baseStatLevel['mainStat'][1][10], baseStatLevel['subStat'][1][10] = 159 , 12.5
	baseStatLevel['mainStat'][1][20], baseStatLevel['subStat'][1][20] = 231 , 12.5
	baseStatLevel['mainStat'][2][20], baseStatLevel['subStat'][2][20] = 272 , 15.4
	baseStatLevel['mainStat'][2][30], baseStatLevel['subStat'][2][30] = 344 , 15.4
	baseStatLevel['mainStat'][3][30], baseStatLevel['subStat'][3][30] = 385 , 18.2
	baseStatLevel['mainStat'][3][40], baseStatLevel['subStat'][3][40] = 457 , 18.2
	baseStatLevel['mainStat'][4][40], baseStatLevel['subStat'][4][40] = 498 , 21.1
	baseStatLevel['mainStat'][4][50], baseStatLevel['subStat'][4][50] = 570 , 21.1
	baseStatLevel['mainStat'][5][50], baseStatLevel['subStat'][5][50] = 611 , 24.0
	baseStatLevel['mainStat'][5][60], baseStatLevel['subStat'][5][60] = 684 , 24.0

	passiveStats = {
			"combat-energyRegen": {
				"value": [0.6, 0.75, 0.9, 1.05, 1.2],
				"multiple": 1,
				"description": "..."
			},
			"combat+squad-DMG_": {
				"value": [10, 12.5, 15, 17.5, 20],
				"multiple": 1,
				"description": "...",
				"stackable": False
			},
			"increase_-{combat-energyRegen}-{combat+squad-DMG_}": {
				"value": [1.7, 2, 2.5, 3, 3.3],
				"multiple": 6,
				"description": "..."
			}
		}

	passiveDescription = "<p>While off-field, Energy Regen increases by <span style=\"color: rgb(237,197,84)\">{0}</span> per second. Attacks from the equipper enhance the squad's DMG against a struck target by <span style=\"color: rgb(237,197,84)\">{1}%</span> for 3 seconds. During this period, this effect is further increased by <span style=\"color: rgb(237,197,84)\">{2}%</span> every 0.5s, up to 6 time. Repeated triggers only refresh its duration without refreshing the DMG increase effect. Passive effects of the same name do not stack.</p>"


	def __init__(self):
		super().__init__()




class BashfulDemon(WEngine):	
	name = "Bashful Demon"
	rank = "A"
	specialty = "Support"
	mainStat = "atk"
	subStat = "atk_"
	baseStatLevel = deepcopy(baseStatLevelTemplate)

	baseStatLevel['mainStat'][0][0], baseStatLevel['subStat'][0][0] = 42 , 10.0
	baseStatLevel['mainStat'][0][10], baseStatLevel['subStat'][0][10] = 107 , 10.0
	baseStatLevel['mainStat'][1][10], baseStatLevel['subStat'][1][10] = 145 , 13.0
	baseStatLevel['mainStat'][1][20], baseStatLevel['subStat'][1][20] = 211 , 13.0
	baseStatLevel['mainStat'][2][20], baseStatLevel['subStat'][2][20] = 248 , 16.0
	baseStatLevel['mainStat'][2][30], baseStatLevel['subStat'][2][30] = 314 , 16.0
	baseStatLevel['mainStat'][3][30], baseStatLevel['subStat'][3][30] = 352 , 19.0
	baseStatLevel['mainStat'][3][40], baseStatLevel['subStat'][3][40] = 417 , 19.0
	baseStatLevel['mainStat'][4][40], baseStatLevel['subStat'][4][40] = 455 , 22.0
	baseStatLevel['mainStat'][4][50], baseStatLevel['subStat'][4][50] = 521 , 22.0
	baseStatLevel['mainStat'][5][50], baseStatLevel['subStat'][5][50] = 558 , 25.0
	baseStatLevel['mainStat'][5][60], baseStatLevel['subStat'][5][60] = 624 , 25.0

	passiveStats = {
			"iceDMG_": {
				"value": [15, 17.5, 20, 22, 24]
			},
			"squad-atk_":{
				"value": [2, 2.3, 2.6, 2.9, 3.2],
				"multiple": 4,
				"description": "...",
				"stackable": False
			} 
		}

	passiveDescription = "<p>Increases <span style=\"color: rgb(140,216,218)\">Ice DMG</span> by <span style=\"color: rgb(237,197,84)\">{0}</span>. When launching an EX Special Attack, all squad members' ATK increases by <span style=\"color: rgb(237,197,84)\">{1}%</span> for 12s, stacking up to 4 times. Retriggering refreshes duration. Passive effects of the same name do not stack.</p>"


	def __init__(self):
		super().__init__()




class BigCylinder(WEngine):
	name = "Big Cylinder"
	rank = "A"
	specialty = "Defense"
	mainStat = "atk"
	subStat = "def_"
	baseStatLevel = deepcopy(baseStatLevelTemplate)
	baseStatLevel['mainStat'][0][0], baseStatLevel['subStat'][0][0] = 42 , 16.0
	baseStatLevel['mainStat'][0][10], baseStatLevel['subStat'][0][10] = 107 , 16.0
	baseStatLevel['mainStat'][1][10], baseStatLevel['subStat'][1][10] = 145 , 20.8
	baseStatLevel['mainStat'][1][20], baseStatLevel['subStat'][1][20] = 211 , 20.8
	baseStatLevel['mainStat'][2][20], baseStatLevel['subStat'][2][20] = 248 , 25.6
	baseStatLevel['mainStat'][2][30], baseStatLevel['subStat'][2][30] = 314 , 25.6
	baseStatLevel['mainStat'][3][30], baseStatLevel['subStat'][3][30] = 352 , 30.4
	baseStatLevel['mainStat'][3][40], baseStatLevel['subStat'][3][40] = 417 , 30.4
	baseStatLevel['mainStat'][4][40], baseStatLevel['subStat'][4][40] = 455 , 35.2
	baseStatLevel['mainStat'][4][50], baseStatLevel['subStat'][4][50] = 521 , 35.2
	baseStatLevel['mainStat'][5][50], baseStatLevel['subStat'][5][50] = 558 , 40.0
	baseStatLevel['mainStat'][5][60], baseStatLevel['subStat'][5][60] = 624 , 40.0

	passiveStats = {
			"...": {
				"value": [7.5, 8.5, 9.5, 10.5, 12]
			},
			"addition-def_": {
				"value": [600, 690, 780, 870, 960],
				"description": "..."
			}
		}
	passiveDescription = "<p>Reduces DMG taken by <span style=\"color: rgb(237,197,84)\">{0}</span>. After being attacked, the next attack to hit an enemy will trigger a critical hit and deal <span style=\"color: rgb(237,197,84)\">{1}%</span> of the equipper's DEF as additional DMG. This effect can be triggered once every 7.5s.</p>"



	def __init__(self):
		super().__init__()




class BunnyBand(WEngine):
	name = "Bunny Band"
	rank = "A"
	specialty = "Defense"
	mainStat = "atk"
	subStat = "def_"
	baseStatLevel = deepcopy(baseStatLevelTemplate)
	baseStatLevel['mainStat'][0][0], baseStatLevel['subStat'][0][0] = 40 , 16.0
	baseStatLevel['mainStat'][0][10], baseStatLevel['subStat'][0][10] = 102 , 16.0
	baseStatLevel['mainStat'][1][10], baseStatLevel['subStat'][1][10] = 138 , 20.8
	baseStatLevel['mainStat'][1][20], baseStatLevel['subStat'][1][20] = 201 , 20.8
	baseStatLevel['mainStat'][2][20], baseStatLevel['subStat'][2][20] = 236 , 25.6
	baseStatLevel['mainStat'][2][30], baseStatLevel['subStat'][2][30] = 299 , 25.6
	baseStatLevel['mainStat'][3][30], baseStatLevel['subStat'][3][30] = 335 , 30.4
	baseStatLevel['mainStat'][3][40], baseStatLevel['subStat'][3][40] = 397 , 30.4
	baseStatLevel['mainStat'][4][40], baseStatLevel['subStat'][4][40] = 433 , 35.2
	baseStatLevel['mainStat'][4][50], baseStatLevel['subStat'][4][50] = 496 , 35.2
	baseStatLevel['mainStat'][5][50], baseStatLevel['subStat'][5][50] = 532 , 40.0
	baseStatLevel['mainStat'][5][60], baseStatLevel['subStat'][5][60] = 594 , 40.0

	passiveStats = {
			"hp_": {
				"value": [8, 9.2, 10.4, 11.6, 12.8]
			},
			"combat-atk_": {
				"value": [10, 11.5, 13, 14.5, 16],
				"multiple": 1
			}
		}

	passiveDescription = "<p>Increases Max HP by <span style=\"color: rgb(237,197,84)\">{0}</span>. Increases the equipper's ATK by <span style=\"color: rgb(237,197,84)\">{1}%</span> when they are shielded.</p>"

	def __init__(self):
		super().__init__()




class CannonRotor(WEngine):
	name = "Cannon Rotor"
	rank = "A"
	specialty = "Attack"
	mainStat = "atk"
	subStat = "critRate_"
	baseStatLevel = deepcopy(baseStatLevelTemplate)
	baseStatLevel['mainStat'][0][0], baseStatLevel['subStat'][0][0] = 40 , 8.0
	baseStatLevel['mainStat'][0][10], baseStatLevel['subStat'][0][10] = 102 , 8.0
	baseStatLevel['mainStat'][1][10], baseStatLevel['subStat'][1][10] = 138 , 10.4
	baseStatLevel['mainStat'][1][20], baseStatLevel['subStat'][1][20] = 201 , 10.4
	baseStatLevel['mainStat'][2][20], baseStatLevel['subStat'][2][20] = 236 , 12.8
	baseStatLevel['mainStat'][2][30], baseStatLevel['subStat'][2][30] = 299 , 12.8
	baseStatLevel['mainStat'][3][30], baseStatLevel['subStat'][3][30] = 335 , 15.2
	baseStatLevel['mainStat'][3][40], baseStatLevel['subStat'][3][40] = 397 , 15.2
	baseStatLevel['mainStat'][4][40], baseStatLevel['subStat'][4][40] = 433 , 17.6
	baseStatLevel['mainStat'][4][50], baseStatLevel['subStat'][4][50] = 496 , 17.6
	baseStatLevel['mainStat'][5][50], baseStatLevel['subStat'][5][50] = 532 , 20.0
	baseStatLevel['mainStat'][5][60], baseStatLevel['subStat'][5][60] = 594 , 20.0

	passiveStats = {
			"atk_": {
				"value": [7.5, 8.6, 9.7, 10.8, 12]
			}, 
			"addition-atk_": {
				"value": [200, 200, 200, 200, 200],
				"description": "..."
			},
			"...":{
				"value": [8, 7.5, 7, 6.5, 6]
			}
		}
	passiveDescription = "<p>Increases ATK by <span style=\"color: rgb(237,197,84)\">{0}</span>. Attacks that land a CRIT on an enemy will inflict an additional <span style=\"color: rgb(237,197,84)\">{1}%</span> of ATK as DMG. This effect can only be triggered once every <span style=\"color: rgb(237,197,84)\">{2}s</span>.</p>"

	def __init__(self):
		super().__init__()




class DemaraBatteryMarkII(WEngine):
	name = "Demara Battery Mark II"
	rank = "A"
	specialty = "Stun"
	mainStat = "atk"
	subStat = "impact_"
	baseStatLevel = deepcopy(baseStatLevelTemplate)

	baseStatLevel['mainStat'][0][0], baseStatLevel['subStat'][0][0] = 42 , 6.0
	baseStatLevel['mainStat'][0][10], baseStatLevel['subStat'][0][10] = 107 , 6.0
	baseStatLevel['mainStat'][1][10], baseStatLevel['subStat'][1][10] = 145 , 7.8
	baseStatLevel['mainStat'][1][20], baseStatLevel['subStat'][1][20] = 211 , 7.8
	baseStatLevel['mainStat'][2][20], baseStatLevel['subStat'][2][20] = 248 , 9.6
	baseStatLevel['mainStat'][2][30], baseStatLevel['subStat'][2][30] = 314 , 9.6
	baseStatLevel['mainStat'][3][30], baseStatLevel['subStat'][3][30] = 352 , 11.4
	baseStatLevel['mainStat'][3][40], baseStatLevel['subStat'][3][40] = 417 , 11.4
	baseStatLevel['mainStat'][4][40], baseStatLevel['subStat'][4][40] = 455 , 13.2
	baseStatLevel['mainStat'][4][50], baseStatLevel['subStat'][4][50] = 521 , 13.2
	baseStatLevel['mainStat'][5][50], baseStatLevel['subStat'][5][50] = 558 , 15.0
	baseStatLevel['mainStat'][5][60], baseStatLevel['subStat'][5][60] = 624 , 15.0

	passiveStats = {
			"electricDMG_": {
				"value": [15, 17.5, 20, 22, 22]
			}, 
			"combat-energyRegen_":{
				"value": [18, 20.5, 23, 25, 27.5],
				"multiple": 1,
				"description": "..."
			}
		}

	passiveDescription = "<p>Increases <span style=\"color: rgb(46,182,255)\">Electric DMG</span> by <span style=\"color: rgb(237,197,84)\">{0}</span>. When the equipper hits an enemy with Dodge Counter or Assist Attack, their Energy Generation Rate increases by <span style=\"color: rgb(237,197,84)\">{1}%</span> for 8s.</p>"

	def __init__(self):
		super().__init__()




class DrillRigRedAxis(WEngine):
	name = "Drill Rig - Red Axis"
	rank = "A"
	specialty = "Attack"
	mainStat = "atk"
	subStat = "energyRegen_"
	baseStatLevel = deepcopy(baseStatLevelTemplate)

	baseStatLevel['mainStat'][0][0], baseStatLevel['subStat'][0][0] = 42 , 20.0
	baseStatLevel['mainStat'][0][10], baseStatLevel['subStat'][0][10] = 107 , 20.0
	baseStatLevel['mainStat'][1][10], baseStatLevel['subStat'][1][10] = 145 , 26.0
	baseStatLevel['mainStat'][1][20], baseStatLevel['subStat'][1][20] = 211 , 26.0
	baseStatLevel['mainStat'][2][20], baseStatLevel['subStat'][2][20] = 248 , 32.0
	baseStatLevel['mainStat'][2][30], baseStatLevel['subStat'][2][30] = 314 , 32.0
	baseStatLevel['mainStat'][3][30], baseStatLevel['subStat'][3][30] = 352 , 38.0
	baseStatLevel['mainStat'][3][40], baseStatLevel['subStat'][3][40] = 417 , 38.0
	baseStatLevel['mainStat'][4][40], baseStatLevel['subStat'][4][40] = 455 , 44.0
	baseStatLevel['mainStat'][4][50], baseStatLevel['subStat'][4][50] = 521 , 44.0
	baseStatLevel['mainStat'][5][50], baseStatLevel['subStat'][5][50] = 558 , 50.0
	baseStatLevel['mainStat'][5][60], baseStatLevel['subStat'][5][60] = 624 , 50.0

	passiveStats = {
			"combat-dash*electricDMG_+basic*electricDMG_":{
				"value": [50, 57.5, 65, 72.5, 80],
				"multiple": 1,
				"description": "..."
			}
		}

	passiveDescription = "<p>When launching an EX Special Attack or Chain Attack, <span style=\"color: rgb(46,182,255)\">Electric DMG</span> from Basic Attacks and Dash Attacks increases by <span style=\"color: rgb(237,197,84)\">{0}%</span> for 10s. This effect can trigger once every 15s.</p>"


	def __init__(self):
		super().__init__()




class ElectroLipGloss(WEngine):
	name = "Electro-Lip Gloss"
	rank = "A"
	specialty = "Anomaly"
	mainStat = "atk"
	subStat = "anomalyProficiency"
	baseStatLevel = deepcopy(baseStatLevelTemplate)

	baseStatLevel['mainStat'][0][0], baseStatLevel['subStat'][0][0] = 40 , 30.0
	baseStatLevel['mainStat'][0][10], baseStatLevel['subStat'][0][10] = 102 , 30.0
	baseStatLevel['mainStat'][1][10], baseStatLevel['subStat'][1][10] = 138 , 39.0
	baseStatLevel['mainStat'][1][20], baseStatLevel['subStat'][1][20] = 201 , 39.0
	baseStatLevel['mainStat'][2][20], baseStatLevel['subStat'][2][20] = 236 , 48.0
	baseStatLevel['mainStat'][2][30], baseStatLevel['subStat'][2][30] = 299 , 48.0
	baseStatLevel['mainStat'][3][30], baseStatLevel['subStat'][3][30] = 335 , 57.0
	baseStatLevel['mainStat'][3][40], baseStatLevel['subStat'][3][40] = 397 , 57.0
	baseStatLevel['mainStat'][4][40], baseStatLevel['subStat'][4][40] = 433 , 66.0
	baseStatLevel['mainStat'][4][50], baseStatLevel['subStat'][4][50] = 496 , 66.0
	baseStatLevel['mainStat'][5][50], baseStatLevel['subStat'][5][50] = 532 , 75.0
	baseStatLevel['mainStat'][5][60], baseStatLevel['subStat'][5][60] = 594 , 75.0

	passiveStats = {
			"combat-atk_": {
				"value": [10, 11.5, 13, 14.5, 16],
				"multiple": 1,
				"description": "..."
			},
			"combat-DMG_": {
				"value": [15, 17.5, 20, 22.5, 25],
				"multiple": 1,
				"description": "..."
			}
		}
		
	passiveDescription = "<p>When there are enemies inflicted with Attribute Anomaly on the field, the equipper's ATK increases by <span style=\"color: rgb(237,197,84)\">{0}%</span> and they deal an additional <span style=\"color: rgb(237,197,84)\">{1}%</span> more DMG to the target.</p>"


	def __init__(self):
		super().__init__()




class GildedBlossom(WEngine):
	name = "Gilded Blossom"
	rank = "A"
	specialty = "Attack"
	mainStat = "atk"
	subStat = "atk_"
	baseStatLevel = deepcopy(baseStatLevelTemplate)

		# Temp remember to fixed
	baseStatLevel['mainStat'][0][0], baseStatLevel['subStat'][0][0] = 42 , 10.0
	baseStatLevel['mainStat'][0][10], baseStatLevel['subStat'][0][10] = 107 , 10.0
	baseStatLevel['mainStat'][1][10], baseStatLevel['subStat'][1][10] = 145 , 13.0
	baseStatLevel['mainStat'][1][20], baseStatLevel['subStat'][1][20] = 211 , 13.0
	baseStatLevel['mainStat'][2][20], baseStatLevel['subStat'][2][20] = 248 , 16.0
	baseStatLevel['mainStat'][2][30], baseStatLevel['subStat'][2][30] = 314 , 16.0
	baseStatLevel['mainStat'][3][30], baseStatLevel['subStat'][3][30] = 352 , 19.0
	baseStatLevel['mainStat'][3][40], baseStatLevel['subStat'][3][40] = 417 , 19.0
	baseStatLevel['mainStat'][4][40], baseStatLevel['subStat'][4][40] = 455 , 22.0
	baseStatLevel['mainStat'][4][50], baseStatLevel['subStat'][4][50] = 521 , 22.0
	baseStatLevel['mainStat'][5][50], baseStatLevel['subStat'][5][50] = 558 , 25.0
	baseStatLevel['mainStat'][5][60], baseStatLevel['subStat'][5][60] = 624 , 25.0

	passiveStats = {
			"atk_": {
				"value": [6, 6.9, 7.8, 8.7, 9.6]
			},
			"EXspecial*DMG_": {
				"value": [15, 17.2, 19.5, 21.8, 24]
			}
		}

	passiveDescription = "ATK increases by <span style=\"color: rgb(237,197,84)\">{0}%</span>, and DMG dealt by EX Special Attacks increases by <span style=\"color: rgb(237,197,84)\">{1}%</span>."

		

	def __init__(self):
		super().__init__()




class Housekeeper(WEngine):
	name = "Housekeeper"
	rank = "A"
	specialty = "Attack"
	mainStat = "atk"
	subStat = "atk_"
	baseStatLevel = deepcopy(baseStatLevelTemplate)
	baseStatLevel['mainStat'][0][0], baseStatLevel['subStat'][0][0] = 42 , 10.0
	baseStatLevel['mainStat'][0][10], baseStatLevel['subStat'][0][10] = 107 , 10.0
	baseStatLevel['mainStat'][1][10], baseStatLevel['subStat'][1][10] = 145 , 13.0
	baseStatLevel['mainStat'][1][20], baseStatLevel['subStat'][1][20] = 211 , 13.0
	baseStatLevel['mainStat'][2][20], baseStatLevel['subStat'][2][20] = 248 , 16.0
	baseStatLevel['mainStat'][2][30], baseStatLevel['subStat'][2][30] = 314 , 16.0
	baseStatLevel['mainStat'][3][30], baseStatLevel['subStat'][3][30] = 352 , 19.0
	baseStatLevel['mainStat'][3][40], baseStatLevel['subStat'][3][40] = 417 , 19.0
	baseStatLevel['mainStat'][4][40], baseStatLevel['subStat'][4][40] = 455 , 22.0
	baseStatLevel['mainStat'][4][50], baseStatLevel['subStat'][4][50] = 521 , 22.0
	baseStatLevel['mainStat'][5][50], baseStatLevel['subStat'][5][50] = 558 , 25.0
	baseStatLevel['mainStat'][5][60], baseStatLevel['subStat'][5][60] = 624 , 25.0

	passiveStats = {
			"combat-energyRegen": {
				"value": [0.45, 0.52, 0.58, 0.65, 0.72],
				"multiple": "inf",
				"description": "..."
			},
			"combat-physicalDMG_": {
				"value": [3, 3.5, 4, 4.4, 4.8],
				"multiple": 15,
				"description": "..."
			}
		}
	passiveDescription = "<p>While off-field, Energy Regen increases by <span style=\"color: rgb(237,197,84)\">{0}</span> per second. When an EX Special Attack hits an enemy, the equipper's <span style=\"color: rgb(192,168,47)\">Physical DMG</span> increases by <span style=\"color: rgb(237,197,84)\">{1}%</span>, stacking up to 15 times and lasting 1s. Retriggering refreshes duration.</p>"



	def __init__(self):
		super().__init__()




class KaboomtheCannon(WEngine):
	name = "Kaboom the Cannon"
	rank = "A"
	specialty = "Support"
	mainStat = "atk"
	subStat = "energyRegen_"
	baseStatLevel = deepcopy(baseStatLevelTemplate)
	baseStatLevel['mainStat'][0][0], baseStatLevel['subStat'][0][0] = 42 , 20.0
	baseStatLevel['mainStat'][0][10], baseStatLevel['subStat'][0][10] = 107 , 20.0
	baseStatLevel['mainStat'][1][10], baseStatLevel['subStat'][1][10] = 145 , 26.0
	baseStatLevel['mainStat'][1][20], baseStatLevel['subStat'][1][20] = 211 , 26.0
	baseStatLevel['mainStat'][2][20], baseStatLevel['subStat'][2][20] = 248 , 32.0
	baseStatLevel['mainStat'][2][30], baseStatLevel['subStat'][2][30] = 314 , 32.0
	baseStatLevel['mainStat'][3][30], baseStatLevel['subStat'][3][30] = 352 , 38.0
	baseStatLevel['mainStat'][3][40], baseStatLevel['subStat'][3][40] = 417 , 38.0
	baseStatLevel['mainStat'][4][40], baseStatLevel['subStat'][4][40] = 455 , 44.0
	baseStatLevel['mainStat'][4][50], baseStatLevel['subStat'][4][50] = 521 , 44.0
	baseStatLevel['mainStat'][5][50], baseStatLevel['subStat'][5][50] = 558 , 50.0
	baseStatLevel['mainStat'][5][60], baseStatLevel['subStat'][5][60] = 624 , 50.0

	passiveStats = {
			"squad-atk_":{
				"value": [2.5, 2.8, 3.2, 3.6, 4],
				"multiple": 4,
				"description": "...",
				"stackable": False
			}
		}
	passiveDescription = "<p>When any friendly unit in the squad attacks and hits an enemy, all friendly units' ATK increases by <span style=\"color: rgb(237,197,84)\">{0}%</span> for 8s, stacking up to 4 times. The duration of each stack is calculated separately, and each friendly unit can provide 1 stack of the buff. Passive effects of the same name do not stack.</p>"



	def __init__(self):
		super().__init__()




class OriginalTransmorpher(WEngine):
	name = "Original Transmorpher"
	rank = "A"
	specialty = "Defense"
	mainStat = "atk"
	subStat = "hp_"
	baseStatLevel = deepcopy(baseStatLevelTemplate)

	baseStatLevel['mainStat'][0][0], baseStatLevel['subStat'][0][0] = 40 , 10.0
	baseStatLevel['mainStat'][0][10], baseStatLevel['subStat'][0][10] = 102 , 10.0
	baseStatLevel['mainStat'][1][10], baseStatLevel['subStat'][1][10] = 138 , 13.0
	baseStatLevel['mainStat'][1][20], baseStatLevel['subStat'][1][20] = 201 , 13.0
	baseStatLevel['mainStat'][2][20], baseStatLevel['subStat'][2][20] = 236 , 16.0
	baseStatLevel['mainStat'][2][30], baseStatLevel['subStat'][2][30] = 299 , 16.0
	baseStatLevel['mainStat'][3][30], baseStatLevel['subStat'][3][30] = 335 , 19.0
	baseStatLevel['mainStat'][3][40], baseStatLevel['subStat'][3][40] = 397 , 19.0
	baseStatLevel['mainStat'][4][40], baseStatLevel['subStat'][4][40] = 433 , 22.0
	baseStatLevel['mainStat'][4][50], baseStatLevel['subStat'][4][50] = 496 , 22.0
	baseStatLevel['mainStat'][5][50], baseStatLevel['subStat'][5][50] = 532 , 25.0
	baseStatLevel['mainStat'][5][60], baseStatLevel['subStat'][5][60] = 594 , 25.0

	passiveStats = {
			"hp_": {
				"value": [8, 9, 10, 11, 12.5]
			}, 
			"combat-impact_": {
				"value": [10, 11.5, 13, 14.5, 16],
				"multiple": 1,
				"description": "..."
			}
		}
	passiveDescription = "<p>Increases Max HP by <span style=\"color: rgb(237,197,84)\">{0}</span>. When attacked, the equipper's Impact is increased by <span style=\"color: rgb(237,197,84)\">{1}%</span> for 12s.</p>"




	def __init__(self):
		super().__init__()




class PreciousFossilizedCore(WEngine):
	name = "Precious Fossilized Core"
	rank = "A"
	specialty = "Stun"
	mainStat = "atk"
	subStat = "impact_"
	baseStatLevel = deepcopy(baseStatLevelTemplate)
	baseStatLevel['mainStat'][0][0], baseStatLevel['subStat'][0][0] = 40 , 6.0
	baseStatLevel['mainStat'][0][10], baseStatLevel['subStat'][0][10] = 102 , 6.0
	baseStatLevel['mainStat'][1][10], baseStatLevel['subStat'][1][10] = 138 , 7.8
	baseStatLevel['mainStat'][1][20], baseStatLevel['subStat'][1][20] = 201 , 7.8
	baseStatLevel['mainStat'][2][20], baseStatLevel['subStat'][2][20] = 236 , 9.6
	baseStatLevel['mainStat'][2][30], baseStatLevel['subStat'][2][30] = 299 , 9.6
	baseStatLevel['mainStat'][3][30], baseStatLevel['subStat'][3][30] = 335 , 11.4
	baseStatLevel['mainStat'][3][40], baseStatLevel['subStat'][3][40] = 397 , 11.4
	baseStatLevel['mainStat'][4][40], baseStatLevel['subStat'][4][40] = 433 , 13.2
	baseStatLevel['mainStat'][4][50], baseStatLevel['subStat'][4][50] = 496 , 13.2
	baseStatLevel['mainStat'][5][50], baseStatLevel['subStat'][5][50] = 532 , 15.0
	baseStatLevel['mainStat'][5][60], baseStatLevel['subStat'][5][60] = 594 , 15.0

	passiveStats = {
			"combat-daze_": {
				"value": [10, 11.5, 13, 14.5, 16], 
				"multiple": 1,
				"description": "..."
			},
			"combat-daze_ 2": {
				"value": [10, 11.5, 13, 14.5, 16],
				"multiple": 1,
				"description": "..."
			}
		}
	passiveDescription = "<p>When the target's HP is no lower than 50%, the equipper inflicts <span style=\"color: rgb(237,197,84)\">{0}%</span> more Daze. When the target's HP is no lower than 75%, this bonus is further enhanced by <span style=\"color: rgb(237,197,84)\">{1}%</span>.</p>"




	def __init__(self):
		super().__init__()




class RainforestGourmet(WEngine):
	name = "Rainforest Gourmet"
	rank = "A"
	specialty = "Anomaly"
	mainStat = "atk"
	subStat = "anomalyProficiency"
	baseStatLevel = deepcopy(baseStatLevelTemplate)

	baseStatLevel['mainStat'][0][0], baseStatLevel['subStat'][0][0] = 40 , 30.0
	baseStatLevel['mainStat'][0][10], baseStatLevel['subStat'][0][10] = 102 , 30.0
	baseStatLevel['mainStat'][1][10], baseStatLevel['subStat'][1][10] = 138 , 39.0
	baseStatLevel['mainStat'][1][20], baseStatLevel['subStat'][1][20] = 201 , 39.0
	baseStatLevel['mainStat'][2][20], baseStatLevel['subStat'][2][20] = 236 , 48.0
	baseStatLevel['mainStat'][2][30], baseStatLevel['subStat'][2][30] = 299 , 48.0
	baseStatLevel['mainStat'][3][30], baseStatLevel['subStat'][3][30] = 335 , 57.0
	baseStatLevel['mainStat'][3][40], baseStatLevel['subStat'][3][40] = 397 , 57.0
	baseStatLevel['mainStat'][4][40], baseStatLevel['subStat'][4][40] = 433 , 66.0
	baseStatLevel['mainStat'][4][50], baseStatLevel['subStat'][4][50] = 496 , 66.0
	baseStatLevel['mainStat'][5][50], baseStatLevel['subStat'][5][50] = 532 , 75.0
	baseStatLevel['mainStat'][5][60], baseStatLevel['subStat'][5][60] = 594 , 75.0

	passiveStats = {
			"combat-atk_": {
				"value": [2.5, 2.8, 3.2, 3.6, 4], 
				"multiple": 10,
				"description": "..."
			}
		}
	passiveDescription = "<p>For every 10 Energy consumed, the equipper gains a buff that increases ATK by <span style=\"color: rgb(237,197,84)\">{0}%</span> for 10s, stacking up to 10 times. The duration of each stack is calculated separately.</p>"



	def __init__(self):
		super().__init__()




class RoaringRide(WEngine):
	name = "Roaring Ride"
	rank = "A"
	specialty = "Anomaly"
	mainStat = "atk"
	subStat = "atk_"
	baseStatLevel = deepcopy(baseStatLevelTemplate)

	baseStatLevel['mainStat'][0][0], baseStatLevel['subStat'][0][0] = 42 , 10.0
	baseStatLevel['mainStat'][0][10], baseStatLevel['subStat'][0][10] = 107 , 10.0
	baseStatLevel['mainStat'][1][10], baseStatLevel['subStat'][1][10] = 145 , 13.0
	baseStatLevel['mainStat'][1][20], baseStatLevel['subStat'][1][20] = 211 , 13.0
	baseStatLevel['mainStat'][2][20], baseStatLevel['subStat'][2][20] = 248 , 16.0
	baseStatLevel['mainStat'][2][30], baseStatLevel['subStat'][2][30] = 314 , 16.0
	baseStatLevel['mainStat'][3][30], baseStatLevel['subStat'][3][30] = 352 , 19.0
	baseStatLevel['mainStat'][3][40], baseStatLevel['subStat'][3][40] = 417 , 19.0
	baseStatLevel['mainStat'][4][40], baseStatLevel['subStat'][4][40] = 455 , 22.0
	baseStatLevel['mainStat'][4][50], baseStatLevel['subStat'][4][50] = 521 , 22.0
	baseStatLevel['mainStat'][5][50], baseStatLevel['subStat'][5][50] = 558 , 25.0
	baseStatLevel['mainStat'][5][60], baseStatLevel['subStat'][5][60] = 624 , 25.0

	passiveStats = {
			"combat-atk_": {
				"value": [8, 9.2, 10.4, 11.6, 12.8], 
				"multiple": 1,
				"description": "..."
			},
			"combat-anomalyProficiency": {
				"value": [40, 46, 52, 58, 64],
				"multiple": 1,
				"description": "..."
			},
			"combat-anomalyBuildUp_": {
				"value": [25, 28, 32, 36, 40],
				"multiple": 1,
				"description": "..."
			}
		}

	passiveDescription = "<p>When EX Special Attack hits an enemy, one of three possible effects is randomly triggered for 5 seconds. This effect can trigger once every 0.3s. The same types of effects cannot stack. Repeated triggers reset the duration allowing several effects to be active at once:<ul><li>increases the equipper's ATK by <span style=\"color: rgb(237,197,84)\">{0}%</span>.</li> <li> increases the equipper's Anomaly Proficiency by <span style=\"color: rgb(237,197,84)\">{1}</span>.</li> <li>increases the equipper's Anomaly Buildup Rate by <span style=\"color: rgb(237,197,84)\">{2}%</span>.</li></ul></p>"

	def __init__(self):
		super().__init__()




class SixShooter(WEngine):
	name = "Six Shooter"
	rank = "A"
	specialty = "Stun"
	mainStat = "atk"
	subStat = "impact_"
	baseStatLevel = deepcopy(baseStatLevelTemplate)

	baseStatLevel['mainStat'][0][0], baseStatLevel['subStat'][0][0] = 40 , 6.0
	baseStatLevel['mainStat'][0][10], baseStatLevel['subStat'][0][10] = 102 , 6.0
	baseStatLevel['mainStat'][1][10], baseStatLevel['subStat'][1][10] = 138 , 7.8
	baseStatLevel['mainStat'][1][20], baseStatLevel['subStat'][1][20] = 201 , 7.8
	baseStatLevel['mainStat'][2][20], baseStatLevel['subStat'][2][20] = 236 , 9.6
	baseStatLevel['mainStat'][2][30], baseStatLevel['subStat'][2][30] = 299 , 9.6
	baseStatLevel['mainStat'][3][30], baseStatLevel['subStat'][3][30] = 335 , 11.4
	baseStatLevel['mainStat'][3][40], baseStatLevel['subStat'][3][40] = 397 , 11.4
	baseStatLevel['mainStat'][4][40], baseStatLevel['subStat'][4][40] = 433 , 13.2
	baseStatLevel['mainStat'][4][50], baseStatLevel['subStat'][4][50] = 496 , 13.2
	baseStatLevel['mainStat'][5][50], baseStatLevel['subStat'][5][50] = 532 , 15.0
	baseStatLevel['mainStat'][5][60], baseStatLevel['subStat'][5][60] = 594 , 15.0

	passiveStats = {
			"combat-EXspecial*daze_": {
				"value": [4, 4.6, 5.2, 5.8, 6.4],
				"multiple": 6, 
				"description": "..."
			}
		}

	passiveDescription = "<p>The equipper gains a Charge stack every 3s, stacking up to 6 times. When launching an EX Special Attack, consumes all Charge stacks, and each stack increases the Daze inflicted by <span style=\"color: rgb(237,197,84)\">{0}%</span> </p>"



	def __init__(self):
		super().__init__()




class SliceofTime(WEngine):
	name = "Slice of Time"
	rank = "A"
	specialty = "Support"
	mainStat = "atk"
	subStat = "pen_"
	baseStatLevel = deepcopy(baseStatLevelTemplate)

		# this motherfucker is fucking wrong

	baseStatLevel['mainStat'][0][0], baseStatLevel['subStat'][0][0] = 40 , 10.0
	baseStatLevel['mainStat'][0][10], baseStatLevel['subStat'][0][10] = 102 , 10.0
	baseStatLevel['mainStat'][1][10], baseStatLevel['subStat'][1][10] = 138 , 13.0
	baseStatLevel['mainStat'][1][20], baseStatLevel['subStat'][1][20] = 201 , 13.0
	baseStatLevel['mainStat'][2][20], baseStatLevel['subStat'][2][20] = 236 , 16.0
	baseStatLevel['mainStat'][2][30], baseStatLevel['subStat'][2][30] = 299 , 16.0
	baseStatLevel['mainStat'][3][30], baseStatLevel['subStat'][3][30] = 335 , 19.0
	baseStatLevel['mainStat'][3][40], baseStatLevel['subStat'][3][40] = 397 , 19.0
	baseStatLevel['mainStat'][4][40], baseStatLevel['subStat'][4][40] = 433 , 22.0
	baseStatLevel['mainStat'][4][50], baseStatLevel['subStat'][4][50] = 496 , 22.0
	baseStatLevel['mainStat'][5][50], baseStatLevel['subStat'][5][50] = 532 , 25.0
	baseStatLevel['mainStat'][5][60], baseStatLevel['subStat'][5][60] = 594 , 25.0

	passiveStats = {
			"...": {
				"value": [20, 23, 26, 29, 32]
			},
			 "... 2": {
				"value": [25, 28.5, 32, 35.5, 40]
			},
			 "... 3": {
				"value": [30, 34.5, 39, 43.5, 48]
			},
			"... 4": {
				"value": [35, 40, 45, 50, 55]
			},
			"... 5": {
				"value": [0.7, 0.8, 0.9, 1, 1.1]
			}
		}
	passiveDescription = "<p>Any squad members' Dodge Counter, EX Special Attack, Assist Attack, or Chain Attack respectively generates <span style=\"color: rgb(237,197,84)\">{0}</span> (Dodge) | <span style=\"color: rgb(237,197,84)\">{1}</span> (Special) | <span style=\"color: rgb(237,197,84)\">{2}</span> (Assist) | <span style=\"color: rgb(237,197,84)\">{3}</span> (Chain) more Decibels and generates <span style=\"color: rgb(237,197,84)\">{4}</span> Energy for the equipper. This effect can trigger once every 12s. The cooldown for each type of attack is independent of others. Passive effects of the same name do not stack.</p>"




	def __init__(self):
		super().__init__()




class SpringEmbrace(WEngine):
	name = "Spring Embrace"
	rank = "A"
	specialty = "Defense"
	mainStat = "atk"
	subStat = "atk_"
	baseStatLevel = deepcopy(baseStatLevelTemplate)

	baseStatLevel['mainStat'][0][0], baseStatLevel['subStat'][0][0] = 40 , 10.0
	baseStatLevel['mainStat'][0][10], baseStatLevel['subStat'][0][10] = 102 , 10.0
	baseStatLevel['mainStat'][1][10], baseStatLevel['subStat'][1][10] = 138 , 13.0
	baseStatLevel['mainStat'][1][20], baseStatLevel['subStat'][1][20] = 201 , 13.0
	baseStatLevel['mainStat'][2][20], baseStatLevel['subStat'][2][20] = 236 , 16.0
	baseStatLevel['mainStat'][2][30], baseStatLevel['subStat'][2][30] = 299 , 16.0
	baseStatLevel['mainStat'][3][30], baseStatLevel['subStat'][3][30] = 335 , 19.0
	baseStatLevel['mainStat'][3][40], baseStatLevel['subStat'][3][40] = 397 , 19.0
	baseStatLevel['mainStat'][4][40], baseStatLevel['subStat'][4][40] = 433 , 22.0
	baseStatLevel['mainStat'][4][50], baseStatLevel['subStat'][4][50] = 496 , 22.0
	baseStatLevel['mainStat'][5][50], baseStatLevel['subStat'][5][50] = 532 , 25.0
	baseStatLevel['mainStat'][5][60], baseStatLevel['subStat'][5][60] = 594 , 25.0

	passiveStats = {
			"...": {
				"value": [7.5, 8.5, 9.5, 10.5, 12]
			},
			"combat-energyRegen_": {
				"value": [10, 11.5, 13, 14.5, 16],
				"multiple": 1,
				"descriptipn": "..."
			},
			"next-energyRegen_": {
				"value": [10, 11.5, 13, 14.5, 16],
				"multiple": 1,
				"description": "...",
				"stackable": False
			}
		}

	passiveDescription = "<p>Reduces DMG taken <span style=\"color: rgb(237,197,84)\">{0}</span>. When attacked, the equipper's Energy Generation Rate increased by <span style=\"color: rgb(237,197,84)\">{1}%</span> for 12s. When the equipper switches off-field, this buff will be transferred to the new on-field character with its duration refreshed. Passive effects of the same name do not stack.</p>"



	def __init__(self):
		super().__init__()




class StarlightEngine(WEngine):
	name = "Starlight Engine"
	rank = "A"
	specialty = "Attack"
	mainStat = "atk"
	subStat = "atk_"
	baseStatLevel = deepcopy(baseStatLevelTemplate)

	baseStatLevel['mainStat'][0][0], baseStatLevel['subStat'][0][0] = 40 , 10.0
	baseStatLevel['mainStat'][0][10], baseStatLevel['subStat'][0][10] = 102 , 10.0
	baseStatLevel['mainStat'][1][10], baseStatLevel['subStat'][1][10] = 138 , 13.0
	baseStatLevel['mainStat'][1][20], baseStatLevel['subStat'][1][20] = 201 , 13.0
	baseStatLevel['mainStat'][2][20], baseStatLevel['subStat'][2][20] = 236 , 16.0
	baseStatLevel['mainStat'][2][30], baseStatLevel['subStat'][2][30] = 299 , 16.0
	baseStatLevel['mainStat'][3][30], baseStatLevel['subStat'][3][30] = 335 , 19.0
	baseStatLevel['mainStat'][3][40], baseStatLevel['subStat'][3][40] = 397 , 19.0
	baseStatLevel['mainStat'][4][40], baseStatLevel['subStat'][4][40] = 433 , 22.0
	baseStatLevel['mainStat'][4][50], baseStatLevel['subStat'][4][50] = 496 , 22.0
	baseStatLevel['mainStat'][5][50], baseStatLevel['subStat'][5][50] = 532 , 25.0
	baseStatLevel['mainStat'][5][60], baseStatLevel['subStat'][5][60] = 594 , 25.0

	passiveStats = {
			"combat-atk_": {
				"value": [12, 13.8, 15.6, 17.4, 19.2],
				"multiple": 1,
				"description": "...",
			}
		}

	passiveDescription = "<p>Launching a Dodge Counter or Quick Assist increases the equipper's ATK by <span style=\"color: rgb(237,197,84)\">{0}%</span> for 12s.</p>"



	def __init__(self):
		super().__init__()




class StarlightEngineReplica(WEngine):
	name = "Starlight Engine Replica"
	rank = "A"
	specialty = "Attack"
	mainStat = "atk"
	subStat = "atk_"
	baseStatLevel = deepcopy(baseStatLevelTemplate)

	baseStatLevel['mainStat'][0][0], baseStatLevel['subStat'][0][0] = 42 , 10.0
	baseStatLevel['mainStat'][0][10], baseStatLevel['subStat'][0][10] = 107 , 10.0
	baseStatLevel['mainStat'][1][10], baseStatLevel['subStat'][1][10] = 145 , 13.0
	baseStatLevel['mainStat'][1][20], baseStatLevel['subStat'][1][20] = 211 , 13.0
	baseStatLevel['mainStat'][2][20], baseStatLevel['subStat'][2][20] = 248 , 16.0
	baseStatLevel['mainStat'][2][30], baseStatLevel['subStat'][2][30] = 314 , 16.0
	baseStatLevel['mainStat'][3][30], baseStatLevel['subStat'][3][30] = 352 , 19.0
	baseStatLevel['mainStat'][3][40], baseStatLevel['subStat'][3][40] = 417 , 19.0
	baseStatLevel['mainStat'][4][40], baseStatLevel['subStat'][4][40] = 455 , 22.0
	baseStatLevel['mainStat'][4][50], baseStatLevel['subStat'][4][50] = 521 , 22.0
	baseStatLevel['mainStat'][5][50], baseStatLevel['subStat'][5][50] = 558 , 25.0
	baseStatLevel['mainStat'][5][60], baseStatLevel['subStat'][5][60] = 624 , 25.0

	passiveStats = {
			"combat-physicalDMG_": {
				"value": [36, 41, 46.5, 52, 57.5],
				"multiple": 1,
				"description": "...",
			}
		}

	passiveDescription = "<p>Increases the equipper's <span style=\"color: rgb(192,168,47)\">Physical DMG</span> by <span style=\"color: rgb(237,197,84)\">{0}%</span> for 8s upon hitting an enemy at least 6 meters away with a Basic Attack or Dash Attack.</p>"



	def __init__(self):
		super().__init__()




class SteamOven(WEngine):
	name = "Steam Oven"
	rank = "A"
	specialty = "Stun"
	mainStat = "atk"
	subStat = "energyRegen_"
	baseStatLevel = deepcopy(baseStatLevelTemplate)

	baseStatLevel['mainStat'][0][0], baseStatLevel['subStat'][0][0] = 40 , 20.0
	baseStatLevel['mainStat'][0][10], baseStatLevel['subStat'][0][10] = 102 , 20.0
	baseStatLevel['mainStat'][1][10], baseStatLevel['subStat'][1][10] = 138 , 26.0
	baseStatLevel['mainStat'][1][20], baseStatLevel['subStat'][1][20] = 201 , 26.0
	baseStatLevel['mainStat'][2][20], baseStatLevel['subStat'][2][20] = 236 , 32.0
	baseStatLevel['mainStat'][2][30], baseStatLevel['subStat'][2][30] = 299 , 32.0
	baseStatLevel['mainStat'][3][30], baseStatLevel['subStat'][3][30] = 335 , 38.0
	baseStatLevel['mainStat'][3][40], baseStatLevel['subStat'][3][40] = 397 , 38.0
	baseStatLevel['mainStat'][4][40], baseStatLevel['subStat'][4][40] = 433 , 44.0
	baseStatLevel['mainStat'][4][50], baseStatLevel['subStat'][4][50] = 496 , 44.0
	baseStatLevel['mainStat'][5][50], baseStatLevel['subStat'][5][50] = 532 , 50.0
	baseStatLevel['mainStat'][5][60], baseStatLevel['subStat'][5][60] = 594 , 50.0

	passiveStats = {
			"combat-impact_": {
				"value": [2, 2.3, 2.6, 2.9, 3.2],
				"multiple": 8,
				"description": "...",
			}
		}

	passiveDescription = "<p>For every 10 Energy accumulated, the equipper's Impact is increased by <span style=\"color: rgb(237,197,84)\">{0}%</span>  stacking up to 8 times. After Energy is consumed, this bonus remains for 8 more seconds. The duration of each stack is calculated separately.</p>"



	def __init__(self):
		super().__init__()




class StreetSuperstar(WEngine):
	name = "Street Superstar"
	rank = "A"
	specialty = "Attack"
	mainStat = "atk"
	subStat = "atk_"
	baseStatLevel = deepcopy(baseStatLevelTemplate)

	baseStatLevel['mainStat'][0][0], baseStatLevel['subStat'][0][0] = 40 , 10.0
	baseStatLevel['mainStat'][0][10], baseStatLevel['subStat'][0][10] = 102 , 10.0
	baseStatLevel['mainStat'][1][10], baseStatLevel['subStat'][1][10] = 138 , 13.0
	baseStatLevel['mainStat'][1][20], baseStatLevel['subStat'][1][20] = 201 , 13.0
	baseStatLevel['mainStat'][2][20], baseStatLevel['subStat'][2][20] = 236 , 16.0
	baseStatLevel['mainStat'][2][30], baseStatLevel['subStat'][2][30] = 299 , 16.0
	baseStatLevel['mainStat'][3][30], baseStatLevel['subStat'][3][30] = 335 , 19.0
	baseStatLevel['mainStat'][3][40], baseStatLevel['subStat'][3][40] = 397 , 19.0
	baseStatLevel['mainStat'][4][40], baseStatLevel['subStat'][4][40] = 433 , 22.0
	baseStatLevel['mainStat'][4][50], baseStatLevel['subStat'][4][50] = 496 , 22.0
	baseStatLevel['mainStat'][5][50], baseStatLevel['subStat'][5][50] = 532 , 25.0
	baseStatLevel['mainStat'][5][60], baseStatLevel['subStat'][5][60] = 594 , 25.0


	passiveStats = {
			"combat-ultimate*DMG_": {
				"value": [15, 17.2, 19.5, 21.7, 24],
				"multiple": 3,
				"description": "...",
			}
		}

	passiveDescription = "<p>Whenever a squad member launches a Chain Attack, the equipper gains a Charge stack, stacking up to 3 times. Upon activating their own Ultimate, the equipper consumes all Charge stacks, and each stack increases the skill's DMG by <span style=\"color: rgb(237,197,84)\">{0}%</span>.</p>"



	def __init__(self):
		super().__init__()




class TheVault(WEngine):
	name = "The Vault"
	rank = "A"
	specialty = "Support"
	mainStat = "atk"
	subStat = "energyRegen_"
	baseStatLevel = deepcopy(baseStatLevelTemplate)

	baseStatLevel['mainStat'][0][0], baseStatLevel['subStat'][0][0] = 42 , 20.0
	baseStatLevel['mainStat'][0][10], baseStatLevel['subStat'][0][10] = 107 , 20.0
	baseStatLevel['mainStat'][1][10], baseStatLevel['subStat'][1][10] = 145 , 26.0
	baseStatLevel['mainStat'][1][20], baseStatLevel['subStat'][1][20] = 211 , 26.0
	baseStatLevel['mainStat'][2][20], baseStatLevel['subStat'][2][20] = 248 , 32.0
	baseStatLevel['mainStat'][2][30], baseStatLevel['subStat'][2][30] = 314 , 32.0
	baseStatLevel['mainStat'][3][30], baseStatLevel['subStat'][3][30] = 352 , 38.0
	baseStatLevel['mainStat'][3][40], baseStatLevel['subStat'][3][40] = 417 , 38.0
	baseStatLevel['mainStat'][4][40], baseStatLevel['subStat'][4][40] = 455 , 44.0
	baseStatLevel['mainStat'][4][50], baseStatLevel['subStat'][4][50] = 521 , 44.0
	baseStatLevel['mainStat'][5][50], baseStatLevel['subStat'][5][50] = 558 , 50.0
	baseStatLevel['mainStat'][5][60], baseStatLevel['subStat'][5][60] = 624 , 50.0

	passiveStats = {
			"squad-DMG_": {
				"value": [15, 17.5, 20, 22, 24],
				"multiple": 1,
				"description": "...",
				"stackable": False
			},
			"combat-energyRegen": {
				"value": [0.5, 0.58, 0.65, 0.72, 0.8],
				"multiple": 2,
				"description": "...",
			}
		}
	passiveDescription = "<p>Dealing <span style=\"color: rgb(248,66,123)\">Electric DMG</span> using an EX Special Attack, Chain Attack, or Ultimate increases all squad members' DMG against the target by <span style=\"color: rgb(237,197,84)\">{0}%</span> and increases the equipper's Energy Regen by <span style=\"color: rgb(237,197,84)\">{1}</span> per second for 2s. Passive effects of the same name do not stack.</p>"



	def __init__(self):
		super().__init__()




class UnfetteredGameBall(WEngine):
	name = "Unfettered Game Ball"
	rank = "A"
	specialty = "Support"
	mainStat = "atk"
	subStat = "energyRegen_"
	baseStatLevel = deepcopy(baseStatLevelTemplate)

	baseStatLevel['mainStat'][0][0], baseStatLevel['subStat'][0][0] = 40 , 20.0
	baseStatLevel['mainStat'][0][10], baseStatLevel['subStat'][0][10] = 102 , 20.0
	baseStatLevel['mainStat'][1][10], baseStatLevel['subStat'][1][10] = 138 , 26.0
	baseStatLevel['mainStat'][1][20], baseStatLevel['subStat'][1][20] = 201 , 26.0
	baseStatLevel['mainStat'][2][20], baseStatLevel['subStat'][2][20] = 236 , 32.0
	baseStatLevel['mainStat'][2][30], baseStatLevel['subStat'][2][30] = 299 , 32.0
	baseStatLevel['mainStat'][3][30], baseStatLevel['subStat'][3][30] = 335 , 38.0
	baseStatLevel['mainStat'][3][40], baseStatLevel['subStat'][3][40] = 397 , 38.0
	baseStatLevel['mainStat'][4][40], baseStatLevel['subStat'][4][40] = 433 , 44.0
	baseStatLevel['mainStat'][4][50], baseStatLevel['subStat'][4][50] = 496 , 44.0
	baseStatLevel['mainStat'][5][50], baseStatLevel['subStat'][5][50] = 532 , 50.0
	baseStatLevel['mainStat'][5][60], baseStatLevel['subStat'][5][60] = 594 , 50.0

	passiveStats = {
			"squad-critRate_": {
				"value": [12, 13.5, 15.5, 17.5, 20],
				"multiple": 1
			}
		}

	passiveDescription = "<p>Whenever the equipper's attack triggers an Attribute Counter effect, all squad members' CRIT Rate against the struck enemy increases by <span style=\"color: rgb(237,197,84)\">{0}%</span> for 12s. The bonuses triggered by the same type of passive effects do not stack.</p>"


	def __init__(self):
		super().__init__()




class WeepingGemini(WEngine):
	name = "Weeping Gemini"
	rank = "A"
	specialty = "Anomaly"
	mainStat = "atk"
	subStat = "atk_"
	baseStatLevel = deepcopy(baseStatLevelTemplate)

	baseStatLevel['mainStat'][0][0], baseStatLevel['subStat'][0][0] = 40 , 10.0
	baseStatLevel['mainStat'][0][10], baseStatLevel['subStat'][0][10] = 102 , 10.0
	baseStatLevel['mainStat'][1][10], baseStatLevel['subStat'][1][10] = 138 , 13.0
	baseStatLevel['mainStat'][1][20], baseStatLevel['subStat'][1][20] = 201 , 13.0
	baseStatLevel['mainStat'][2][20], baseStatLevel['subStat'][2][20] = 236 , 16.0
	baseStatLevel['mainStat'][2][30], baseStatLevel['subStat'][2][30] = 299 , 16.0
	baseStatLevel['mainStat'][3][30], baseStatLevel['subStat'][3][30] = 335 , 19.0
	baseStatLevel['mainStat'][3][40], baseStatLevel['subStat'][3][40] = 397 , 19.0
	baseStatLevel['mainStat'][4][40], baseStatLevel['subStat'][4][40] = 433 , 22.0
	baseStatLevel['mainStat'][4][50], baseStatLevel['subStat'][4][50] = 496 , 22.0
	baseStatLevel['mainStat'][5][50], baseStatLevel['subStat'][5][50] = 532 , 25.0
	baseStatLevel['mainStat'][5][60], baseStatLevel['subStat'][5][60] = 594 , 25.0

	passiveStats = {
			"combat-anomalyProficiency": {
				"value": [30, 34, 38, 42, 46],
				"multiple": 4
			}
		}

	passiveDescription = "<p>Whenever a squad member inflicts an Attribute Anomaly on an enemy, the equipper gains a buff that increases Anomaly Proficiency by <span style=\"color: rgb(237,197,84)\">{0}</span>, stacking up to 4 times. This effect expires when the target recovers from Stun or is defeated. The duration of each stack is calculated separately.</p>"


	def __init__(self):
		super().__init__()




class IdentityBase(WEngine):
	name = "[Identity] Base"
	rank = "B"
	specialty = "Defense"
	mainStat = "atk"
	subStat = "def_"
	baseStatLevel = deepcopy(baseStatLevelTemplate)

	baseStatLevel['mainStat'][0][0], baseStatLevel['subStat'][0][0] = 32 , 12.8
	baseStatLevel['mainStat'][0][10], baseStatLevel['subStat'][0][10] = 82 , 12.8
	baseStatLevel['mainStat'][1][10], baseStatLevel['subStat'][1][10] = 110 , 16.6
	baseStatLevel['mainStat'][1][20], baseStatLevel['subStat'][1][20] = 160 , 16.6
	baseStatLevel['mainStat'][2][20], baseStatLevel['subStat'][2][20] = 189 , 20.5
	baseStatLevel['mainStat'][2][30], baseStatLevel['subStat'][2][30] = 239 , 20.5
	baseStatLevel['mainStat'][3][30], baseStatLevel['subStat'][3][30] = 268 , 24.3
	baseStatLevel['mainStat'][3][40], baseStatLevel['subStat'][3][40] = 318 , 24.3
	baseStatLevel['mainStat'][4][40], baseStatLevel['subStat'][4][40] = 346 , 28.2
	baseStatLevel['mainStat'][4][50], baseStatLevel['subStat'][4][50] = 397 , 28.2
	baseStatLevel['mainStat'][5][50], baseStatLevel['subStat'][5][50] = 425 , 32.0
	baseStatLevel['mainStat'][5][60], baseStatLevel['subStat'][5][60] = 475 , 32.0

	passiveStats = {
			"combat-def_": {
				"value": [20, 23, 26, 29, 32],
				"multiple": 1,
				"description": "..."
			}
		}

	passiveDescription = "<p>When attacked, the equipper's DEF increases by <span style=\"color: rgb(237,197,84)\">{0}%</span> for 8s.</p>"


	def __init__(self):
		super().__init__()




class IdentityInflection(WEngine):
	name = "[Identity] Inflection"
	rank = "B"
	specialty = "Defense"
	mainStat = "atk"
	subStat = "def_"
	baseStatLevel = deepcopy(baseStatLevelTemplate)

	baseStatLevel['mainStat'][0][0], baseStatLevel['subStat'][0][0] = 32 , 12.8
	baseStatLevel['mainStat'][0][10], baseStatLevel['subStat'][0][10] = 82 , 12.8
	baseStatLevel['mainStat'][1][10], baseStatLevel['subStat'][1][10] = 110 , 16.6
	baseStatLevel['mainStat'][1][20], baseStatLevel['subStat'][1][20] = 160 , 16.6
	baseStatLevel['mainStat'][2][20], baseStatLevel['subStat'][2][20] = 189 , 20.5
	baseStatLevel['mainStat'][2][30], baseStatLevel['subStat'][2][30] = 239 , 20.5
	baseStatLevel['mainStat'][3][30], baseStatLevel['subStat'][3][30] = 268 , 24.3
	baseStatLevel['mainStat'][3][40], baseStatLevel['subStat'][3][40] = 318 , 24.3
	baseStatLevel['mainStat'][4][40], baseStatLevel['subStat'][4][40] = 346 , 28.2
	baseStatLevel['mainStat'][4][50], baseStatLevel['subStat'][4][50] = 397 , 28.2
	baseStatLevel['mainStat'][5][50], baseStatLevel['subStat'][5][50] = 425 , 32.0
	baseStatLevel['mainStat'][5][60], baseStatLevel['subStat'][5][60] = 475 , 32.0

	passiveStats = {
			"...": {
				"value": [6, 7, 8, 9, 10]
			}
		}
	passiveDescription = "<p>When attacked, reduces the attacker's DMG by <span style=\"color: rgb(237,197,84)\">{0}%</span> for 12s.</p>"



	def __init__(self):
		super().__init__()




class LunarDecrescent(WEngine):
	name = "[Lunar] Decrescent"
	rank = "B"
	specialty = "Attack"
	mainStat = "atk"
	subStat = "atk_"
	baseStatLevel = deepcopy(baseStatLevelTemplate)

	baseStatLevel['mainStat'][0][0], baseStatLevel['subStat'][0][0] = 32 , 8.0
	baseStatLevel['mainStat'][0][10], baseStatLevel['subStat'][0][10] = 82 , 8.0
	baseStatLevel['mainStat'][1][10], baseStatLevel['subStat'][1][10] = 110 , 10.4
	baseStatLevel['mainStat'][1][20], baseStatLevel['subStat'][1][20] = 160 , 10.4
	baseStatLevel['mainStat'][2][20], baseStatLevel['subStat'][2][20] = 189 , 12.8
	baseStatLevel['mainStat'][2][30], baseStatLevel['subStat'][2][30] = 239 , 12.8
	baseStatLevel['mainStat'][3][30], baseStatLevel['subStat'][3][30] = 268 , 15.2
	baseStatLevel['mainStat'][3][40], baseStatLevel['subStat'][3][40] = 318 , 15.2
	baseStatLevel['mainStat'][4][40], baseStatLevel['subStat'][4][40] = 346 , 17.6
	baseStatLevel['mainStat'][4][50], baseStatLevel['subStat'][4][50] = 397 , 17.6
	baseStatLevel['mainStat'][5][50], baseStatLevel['subStat'][5][50] = 425 , 20.0
	baseStatLevel['mainStat'][5][60], baseStatLevel['subStat'][5][60] = 475 , 20.0

	passiveStats = {
			"combat_DMG_": {
				"value": [15, 17.5, 20, 22.5, 25],
				"multiple": 1,
				"description": ".."
			}
		}
	passiveDescription = "<p>Launching a Chain Attack or Ultimate increases the equipper's DMG by <span style=\"color: rgb(237,197,84)\">{0}%</span> for 6s.</p>"


	def __init__(self):
		super().__init__()




class LunarNoviluna(WEngine):
	name = "[Lunar] Noviluna"
	rank = "B"
	specialty = "Attack"
	mainStat = "atk"
	subStat = "critRate_"
	baseStatLevel = deepcopy(baseStatLevelTemplate)

	baseStatLevel['mainStat'][0][0], baseStatLevel['subStat'][0][0] = 32 , 6.4
	baseStatLevel['mainStat'][0][10], baseStatLevel['subStat'][0][10] = 82 , 6.4
	baseStatLevel['mainStat'][1][10], baseStatLevel['subStat'][1][10] = 110 , 8.3
	baseStatLevel['mainStat'][1][20], baseStatLevel['subStat'][1][20] = 160 , 8.3
	baseStatLevel['mainStat'][2][20], baseStatLevel['subStat'][2][20] = 189 , 10.2
	baseStatLevel['mainStat'][2][30], baseStatLevel['subStat'][2][30] = 239 , 10.2
	baseStatLevel['mainStat'][3][30], baseStatLevel['subStat'][3][30] = 268 , 12.2
	baseStatLevel['mainStat'][3][40], baseStatLevel['subStat'][3][40] = 318 , 12.2
	baseStatLevel['mainStat'][4][40], baseStatLevel['subStat'][4][40] = 346 , 14.1
	baseStatLevel['mainStat'][4][50], baseStatLevel['subStat'][4][50] = 397 , 14.1
	baseStatLevel['mainStat'][5][50], baseStatLevel['subStat'][5][50] = 425 , 16.0
	baseStatLevel['mainStat'][5][60], baseStatLevel['subStat'][5][60] = 475 , 16.0

	passiveStats = {
			"...": {
				"value": [3, 3.5, 4, 4.5, 5]
			}
		}

	passiveDescription = "<p>Launching an EX Special Attack generates <span style=\"color: rgb(237,197,84)\">{0}</span> Energy for the equipper. This effect can trigger once every 12s.</p>"



	def __init__(self):
		super().__init__()




class LunarPleniluna(WEngine):
	name = "[Lunar] Pleniluna"
	rank = "B"
	specialty = "Attack"
	mainStat = "atk"
	subStat = "atk_"
	baseStatLevel = deepcopy(baseStatLevelTemplate)

	baseStatLevel['mainStat'][0][0], baseStatLevel['subStat'][0][0] = 32 , 8.0
	baseStatLevel['mainStat'][0][10], baseStatLevel['subStat'][0][10] = 82 , 8.0
	baseStatLevel['mainStat'][1][10], baseStatLevel['subStat'][1][10] = 110 , 10.4
	baseStatLevel['mainStat'][1][20], baseStatLevel['subStat'][1][20] = 160 , 10.4
	baseStatLevel['mainStat'][2][20], baseStatLevel['subStat'][2][20] = 189 , 12.8
	baseStatLevel['mainStat'][2][30], baseStatLevel['subStat'][2][30] = 239 , 12.8
	baseStatLevel['mainStat'][3][30], baseStatLevel['subStat'][3][30] = 268 , 15.2
	baseStatLevel['mainStat'][3][40], baseStatLevel['subStat'][3][40] = 318 , 15.2
	baseStatLevel['mainStat'][4][40], baseStatLevel['subStat'][4][40] = 346 , 17.6
	baseStatLevel['mainStat'][4][50], baseStatLevel['subStat'][4][50] = 397 , 17.6
	baseStatLevel['mainStat'][5][50], baseStatLevel['subStat'][5][50] = 425 , 20.0
	baseStatLevel['mainStat'][5][60], baseStatLevel['subStat'][5][60] = 475 , 20.0

	passiveStats = {
			"basic*DMG_+dash*DMG_+dodgeCounterDMG_": {
				"value": [12, 14, 16, 18, 20]
			}
		}

	passiveDescription = "<p>Basic Attack, Dash Attack, and Dodge Counter DMG increase by <span style=\"color: rgb(237,197,84)\">{0}%</span>.</p>"


	def __init__(self):
		super().__init__()




class MagneticStormAlpha(WEngine):
	name = "[Magnetic Storm] Alpha"
	rank = "B"
	specialty = "Anomaly"
	mainStat = "atk"
	subStat = "atk_"
	baseStatLevel = deepcopy(baseStatLevelTemplate)
		
	baseStatLevel['mainStat'][0][0], baseStatLevel['subStat'][0][0] = 32 , 8.0
	baseStatLevel['mainStat'][0][10], baseStatLevel['subStat'][0][10] = 82 , 8.0
	baseStatLevel['mainStat'][1][10], baseStatLevel['subStat'][1][10] = 110 , 10.4
	baseStatLevel['mainStat'][1][20], baseStatLevel['subStat'][1][20] = 160 , 10.4
	baseStatLevel['mainStat'][2][20], baseStatLevel['subStat'][2][20] = 189 , 12.8
	baseStatLevel['mainStat'][2][30], baseStatLevel['subStat'][2][30] = 239 , 12.8
	baseStatLevel['mainStat'][3][30], baseStatLevel['subStat'][3][30] = 268 , 15.2
	baseStatLevel['mainStat'][3][40], baseStatLevel['subStat'][3][40] = 318 , 15.2
	baseStatLevel['mainStat'][4][40], baseStatLevel['subStat'][4][40] = 346 , 17.6
	baseStatLevel['mainStat'][4][50], baseStatLevel['subStat'][4][50] = 397 , 17.6
	baseStatLevel['mainStat'][5][50], baseStatLevel['subStat'][5][50] = 425 , 20.0
	baseStatLevel['mainStat'][5][60], baseStatLevel['subStat'][5][60] = 475 , 20.0


	passiveStats = {
			"combat-anomalyMastery": {
				"value": [25, 28, 32, 36, 40],
				"multiple": 1,
				"description": ".."
			}
		}
	passiveDescription = "<p>Accumulating Anomaly Buildup increases the equipper's Anomaly Mastery by <span style=\"color: rgb(237,197,84)\">{0}</span> for 10s. This effect can trigger once every 20s.</p>"
	


	def __init__(self):
		super().__init__()


class MagneticStormBravo(WEngine):
	name = "[Magnetic Storm] Bravo"
	rank = "B"
	specialty = "Anomaly"
	mainStat = "atk"
	subStat = "anomalyProficiency"
	baseStatLevel = deepcopy(baseStatLevelTemplate)

	baseStatLevel['mainStat'][0][0], baseStatLevel['subStat'][0][0] = 32 , 24.0
	baseStatLevel['mainStat'][0][10], baseStatLevel['subStat'][0][10] = 82 , 24.0
	baseStatLevel['mainStat'][1][10], baseStatLevel['subStat'][1][10] = 110 , 31.2
	baseStatLevel['mainStat'][1][20], baseStatLevel['subStat'][1][20] = 160 , 31.2
	baseStatLevel['mainStat'][2][20], baseStatLevel['subStat'][2][20] = 189 , 38.4
	baseStatLevel['mainStat'][2][30], baseStatLevel['subStat'][2][30] = 239 , 38.4
	baseStatLevel['mainStat'][3][30], baseStatLevel['subStat'][3][30] = 268 , 45.6
	baseStatLevel['mainStat'][3][40], baseStatLevel['subStat'][3][40] = 318 , 45.6
	baseStatLevel['mainStat'][4][40], baseStatLevel['subStat'][4][40] = 346 , 52.8
	baseStatLevel['mainStat'][4][50], baseStatLevel['subStat'][4][50] = 397 , 52.8
	baseStatLevel['mainStat'][5][50], baseStatLevel['subStat'][5][50] = 425 , 60.0
	baseStatLevel['mainStat'][5][60], baseStatLevel['subStat'][5][60] = 475 , 60.0

	passiveStats = {
			"combat-anomalyProficiency": {
				"value": [25, 28, 32, 36, 40],
				"multiple": 1,
				"description": ".."
			}
		}
	passiveDescription = "<p>Accumulating Anomaly Buildup increases the equipper's Anomaly Proficiency by <span style=\"color: rgb(237,197,84)\">{0}</span> for 10s. This effect can only be triggered once every 20s.</p>"


	def __init__(self):
		super().__init__()


class MagneticStormCharlie(WEngine):
	name = "[Magnetic Storm] Charlie"
	rank = "B"
	specialty = "Anomaly"
	mainStat = "atk"
	subStat = "pen_"
	baseStatLevel = deepcopy(baseStatLevelTemplate)

	baseStatLevel['mainStat'][0][0], baseStatLevel['subStat'][0][0] = 32 , 6.4
	baseStatLevel['mainStat'][0][10], baseStatLevel['subStat'][0][10] = 82 , 6.4
	baseStatLevel['mainStat'][1][10], baseStatLevel['subStat'][1][10] = 110 , 8.3
	baseStatLevel['mainStat'][1][20], baseStatLevel['subStat'][1][20] = 160 , 8.3
	baseStatLevel['mainStat'][2][20], baseStatLevel['subStat'][2][20] = 189 , 10.2
	baseStatLevel['mainStat'][2][30], baseStatLevel['subStat'][2][30] = 239 , 10.2
	baseStatLevel['mainStat'][3][30], baseStatLevel['subStat'][3][30] = 268 , 12.2
	baseStatLevel['mainStat'][3][40], baseStatLevel['subStat'][3][40] = 318 , 12.2
	baseStatLevel['mainStat'][4][40], baseStatLevel['subStat'][4][40] = 346 , 14.1
	baseStatLevel['mainStat'][4][50], baseStatLevel['subStat'][4][50] = 397 , 14.1
	baseStatLevel['mainStat'][5][50], baseStatLevel['subStat'][5][50] = 425 , 16.0
	baseStatLevel['mainStat'][5][60], baseStatLevel['subStat'][5][60] = 475 , 16.0

	passiveStats = {
			"...": {
				"value": [3.5, 4, 4.5, 5, 5.5]
			}
		}

	passiveDescription = "<p>Whenever a squad member inflicts an Attribute Anomaly on an enemy, the equipper generates <span style=\"color: rgb(237,197,84)\">{0}</span> Energy. This effect can trigger once every 12s.</p>"


	def __init__(self):
		super().__init__()


class ReverbMarkI(WEngine):
	name = "[Reverb] Mark I"
	rank = "B"
	specialty = "Support"
	mainStat = "atk"
	subStat = "atk_"
	baseStatLevel = deepcopy(baseStatLevelTemplate)

	baseStatLevel['mainStat'][0][0], baseStatLevel['subStat'][0][0] = 32 , 8.0
	baseStatLevel['mainStat'][0][10], baseStatLevel['subStat'][0][10] = 82 , 8.0
	baseStatLevel['mainStat'][1][10], baseStatLevel['subStat'][1][10] = 110 , 10.4
	baseStatLevel['mainStat'][1][20], baseStatLevel['subStat'][1][20] = 160 , 10.4
	baseStatLevel['mainStat'][2][20], baseStatLevel['subStat'][2][20] = 189 , 12.8
	baseStatLevel['mainStat'][2][30], baseStatLevel['subStat'][2][30] = 239 , 12.8
	baseStatLevel['mainStat'][3][30], baseStatLevel['subStat'][3][30] = 268 , 15.2
	baseStatLevel['mainStat'][3][40], baseStatLevel['subStat'][3][40] = 318 , 15.2
	baseStatLevel['mainStat'][4][40], baseStatLevel['subStat'][4][40] = 346 , 17.6
	baseStatLevel['mainStat'][4][50], baseStatLevel['subStat'][4][50] = 397 , 17.6
	baseStatLevel['mainStat'][5][50], baseStatLevel['subStat'][5][50] = 425 , 20.0
	baseStatLevel['mainStat'][5][60], baseStatLevel['subStat'][5][60] = 475 , 20.0

	passiveStats = {
			"squad-impact_": {
				"value": [8, 9, 10, 11, 12],
				"multiple": 1,
				"description": "...",
				"stackable": False
			}
		}

	passiveDescription = "<p>Launching an EX Special Attack increases all squad members' Impact by <span style=\"color: rgb(237,197,84)\">{0}%</span> for 10s. This effect can trigger once every 20s. Passive effects of the same name do not stack.</p>"



	def __init__(self):
		super().__init__()


class ReverbMarkII(WEngine):
	name = "[Reverb] Mark II"
	rank = "B"
	specialty = "Support"
	mainStat = "atk"
	subStat = "energyRegen_"
	baseStatLevel = deepcopy(baseStatLevelTemplate)

	baseStatLevel['mainStat'][0][0], baseStatLevel['subStat'][0][0] = 32 , 16.0
	baseStatLevel['mainStat'][0][10], baseStatLevel['subStat'][0][10] = 82 , 16.0
	baseStatLevel['mainStat'][1][10], baseStatLevel['subStat'][1][10] = 110 , 20.8
	baseStatLevel['mainStat'][1][20], baseStatLevel['subStat'][1][20] = 160 , 20.8
	baseStatLevel['mainStat'][2][20], baseStatLevel['subStat'][2][20] = 189 , 25.6
	baseStatLevel['mainStat'][2][30], baseStatLevel['subStat'][2][30] = 239 , 25.6
	baseStatLevel['mainStat'][3][30], baseStatLevel['subStat'][3][30] = 268 , 30.4
	baseStatLevel['mainStat'][3][40], baseStatLevel['subStat'][3][40] = 318 , 30.4
	baseStatLevel['mainStat'][4][40], baseStatLevel['subStat'][4][40] = 346 , 35.2
	baseStatLevel['mainStat'][4][50], baseStatLevel['subStat'][4][50] = 397 , 35.2
	baseStatLevel['mainStat'][5][50], baseStatLevel['subStat'][5][50] = 425 , 40.0
	baseStatLevel['mainStat'][5][60], baseStatLevel['subStat'][5][60] = 475 , 40.0

	passiveStats = {
			"squad-anomalyMastery+anomalyProficiency": {
				"value": [10, 12, 13, 15, 16],
				"multiple": 1,
				"description": "...",
				"stackable": False
			}
		}

	passiveDescription = "<p>Launching an EX Special Attack or Chain Attack increases all squad members' Anomaly Mastery and Anomaly Proficiency by <span style=\"color: rgb(237,197,84)\">{0}</span> for 10s. This effect can trigger once every 20s. Passive effects of the same name do not stack.</p>"


	def __init__(self):
		super().__init__()


class ReverbMarkIII(WEngine):
	name = "[Reverb] Mark III"
	rank = "B"
	specialty = "Support"
	mainStat = "atk"
	subStat = "hp_"
	baseStatLevel = deepcopy(baseStatLevelTemplate)

	baseStatLevel['mainStat'][0][0], baseStatLevel['subStat'][0][0] = 32 , 8.0
	baseStatLevel['mainStat'][0][10], baseStatLevel['subStat'][0][10] = 82 , 8.0
	baseStatLevel['mainStat'][1][10], baseStatLevel['subStat'][1][10] = 110 , 10.4
	baseStatLevel['mainStat'][1][20], baseStatLevel['subStat'][1][20] = 160 , 10.4
	baseStatLevel['mainStat'][2][20], baseStatLevel['subStat'][2][20] = 189 , 12.8
	baseStatLevel['mainStat'][2][30], baseStatLevel['subStat'][2][30] = 239 , 12.8
	baseStatLevel['mainStat'][3][30], baseStatLevel['subStat'][3][30] = 268 , 15.2
	baseStatLevel['mainStat'][3][40], baseStatLevel['subStat'][3][40] = 318 , 15.2
	baseStatLevel['mainStat'][4][40], baseStatLevel['subStat'][4][40] = 346 , 17.6
	baseStatLevel['mainStat'][4][50], baseStatLevel['subStat'][4][50] = 397 , 17.6
	baseStatLevel['mainStat'][5][50], baseStatLevel['subStat'][5][50] = 425 , 20.0
	baseStatLevel['mainStat'][5][60], baseStatLevel['subStat'][5][60] = 475 , 20.0

	passiveStats = {
			"squad-atk_": {
				"value": [8, 9, 10, 11, 12],
				"multiple": 1,
				"description": "..."
			}
		}

	passiveDescription = "<p>Launching a Chain Attack or Ultimate increases all squad members' ATK by <span style=\"color: rgb(237,197,84)\">{0}%</span> for 10s. This effect can trigger once every 20s. Passive effects of the same name do not stack.</p>"

	def __init__(self):
		super().__init__()



class VortexArrow(WEngine):
	name = "[Vortex] Arrow"
	rank = "B"
	specialty = "Stun"
	mainStat = "atk"
	subStat = "impact_"
	baseStatLevel = deepcopy(baseStatLevelTemplate)

	baseStatLevel['mainStat'][0][0], baseStatLevel['subStat'][0][0] = 32 , 4.8
	baseStatLevel['mainStat'][0][10], baseStatLevel['subStat'][0][10] = 82 , 4.8
	baseStatLevel['mainStat'][1][10], baseStatLevel['subStat'][1][10] = 110 , 6.2
	baseStatLevel['mainStat'][1][20], baseStatLevel['subStat'][1][20] = 160 , 6.2
	baseStatLevel['mainStat'][2][20], baseStatLevel['subStat'][2][20] = 189 , 7.7
	baseStatLevel['mainStat'][2][30], baseStatLevel['subStat'][2][30] = 239 , 7.7
	baseStatLevel['mainStat'][3][30], baseStatLevel['subStat'][3][30] = 268 , 9.1
	baseStatLevel['mainStat'][3][40], baseStatLevel['subStat'][3][40] = 318 , 9.1
	baseStatLevel['mainStat'][4][40], baseStatLevel['subStat'][4][40] = 346 , 10.6
	baseStatLevel['mainStat'][4][50], baseStatLevel['subStat'][4][50] = 397 , 10.6
	baseStatLevel['mainStat'][5][50], baseStatLevel['subStat'][5][50] = 425 , 12.0
	baseStatLevel['mainStat'][5][60], baseStatLevel['subStat'][5][60] = 475 , 12.0

	passiveStats = {
			"combat-daze_": {
				"value": [8, 9, 10, 11, 12],
				"multiple": 1,
				"description": "..."
			}
		}
	passiveDescription = "<p>The equipper's attacks inflict <span style=\"color: rgb(237,197,84)\">{0}%</span> more Daze on their main target.</p>"

	def __init__(self):
		super().__init__()



class VortexHatchet(WEngine):
	name = "[Vortex] Hatchet"
	rank = "B"
	specialty = "Stun"
	mainStat = "atk"
	subStat = "energyRegen_"
	baseStatLevel = deepcopy(baseStatLevelTemplate)

	baseStatLevel['mainStat'][0][0], baseStatLevel['subStat'][0][0] = 32 , 16.0
	baseStatLevel['mainStat'][0][10], baseStatLevel['subStat'][0][10] = 82 , 16.0
	baseStatLevel['mainStat'][1][10], baseStatLevel['subStat'][1][10] = 110 , 20.8
	baseStatLevel['mainStat'][1][20], baseStatLevel['subStat'][1][20] = 160 , 20.8
	baseStatLevel['mainStat'][2][20], baseStatLevel['subStat'][2][20] = 189 , 25.6
	baseStatLevel['mainStat'][2][30], baseStatLevel['subStat'][2][30] = 239 , 25.6
	baseStatLevel['mainStat'][3][30], baseStatLevel['subStat'][3][30] = 268 , 30.4
	baseStatLevel['mainStat'][3][40], baseStatLevel['subStat'][3][40] = 318 , 30.4
	baseStatLevel['mainStat'][4][40], baseStatLevel['subStat'][4][40] = 346 , 35.2
	baseStatLevel['mainStat'][4][50], baseStatLevel['subStat'][4][50] = 397 , 35.2
	baseStatLevel['mainStat'][5][50], baseStatLevel['subStat'][5][50] = 425 , 40.0
	baseStatLevel['mainStat'][5][60], baseStatLevel['subStat'][5][60] = 475 , 40.0

	passiveStats = {
			"squad-atk_": {
				"value": [9, 10, 11, 12, 13],
				"multiple": 1,
				"description": "...",
				"stackable": False
			}
		}

	passiveDescription = "<p>Upon entering combat or switching in, the equipper's Impact increases by <span style=\"color: rgb(237,197,84)\">{0}%</span> for 10s. This effect can trigger once every 20s.</p>"

	def __init__(self):
		super().__init__()


class VortexRevolver(WEngine):
	name = "[Vortex] Revolver"
	rank = "B"
	specialty = "Stun"
	mainStat = "atk"
	subStat = "atk_"
	baseStatLevel = deepcopy(baseStatLevelTemplate)

	baseStatLevel['mainStat'][0][0], baseStatLevel['subStat'][0][0] = 32 , 8.0
	baseStatLevel['mainStat'][0][10], baseStatLevel['subStat'][0][10] = 82 , 8.0
	baseStatLevel['mainStat'][1][10], baseStatLevel['subStat'][1][10] = 110 , 10.4
	baseStatLevel['mainStat'][1][20], baseStatLevel['subStat'][1][20] = 160 , 10.4
	baseStatLevel['mainStat'][2][20], baseStatLevel['subStat'][2][20] = 189 , 12.8
	baseStatLevel['mainStat'][2][30], baseStatLevel['subStat'][2][30] = 239 , 12.8
	baseStatLevel['mainStat'][3][30], baseStatLevel['subStat'][3][30] = 268 , 15.2
	baseStatLevel['mainStat'][3][40], baseStatLevel['subStat'][3][40] = 318 , 15.2
	baseStatLevel['mainStat'][4][40], baseStatLevel['subStat'][4][40] = 346 , 17.6
	baseStatLevel['mainStat'][4][50], baseStatLevel['subStat'][4][50] = 397 , 17.6
	baseStatLevel['mainStat'][5][50], baseStatLevel['subStat'][5][50] = 425 , 20.0
	baseStatLevel['mainStat'][5][60], baseStatLevel['subStat'][5][60] = 475 , 20.0

	passiveStats = {
			"EXspecial*daze_": {
				"value": [10, 11.5, 13, 14.5, 16],
			}
		}

	passiveDescription = "<p>EX Special Attacks inflict <span style=\"color: rgb(237,197,84)\">{0}%</span> more Daze.</p>"
	def __init__(self):
		super().__init__()


wengines: dict[str, Type[WEngine]] = {
	# S rank
	"Deep Sea Visitor": DeepSeaVisitor,
	"Fusion Compiler": FusionCompiler,
	"Hellfire Gears": HellfireGears,
	"Ice-Jade Teapot": IceJadeTeapot,
	"Riot Suppressor Mark VI": RiotSuppressorMarkVI,
	"Steel Cushion": SteelCushion,
	"The Brimstone": TheBrimstone,
	"The Restrained": TheRestrained,
	"Weeping Cradle": WeepingCradle,


	# A rank
	"Bashful Demon": BashfulDemon,
	"Big Cylinder": BigCylinder,
	"Bunny Band": BunnyBand,
	"Cannon Rotor": CannonRotor,
	"Demara Battery Mark II": DemaraBatteryMarkII,
	"Drill Rig - Red Axis": DrillRigRedAxis,
	"Electro-Lip Gloss": ElectroLipGloss,
	"Gilded Blossom": GildedBlossom,
	"Housekeeper": Housekeeper,
	"Kaboom the Cannon": KaboomtheCannon,
	"Original Transmorpher": OriginalTransmorpher,
	"Precious Fossilized Core": PreciousFossilizedCore,
	"Rainforest Gourmet": RainforestGourmet,
	"Roaring Ride": RoaringRide,
	"Six Shooter": SixShooter,
	"Slice of Time": SliceofTime,
	"Spring Embrace": SpringEmbrace,
	"Starlight Engine": StarlightEngine,
	"Starlight Engine Replica": StarlightEngineReplica,
	"Steam Oven": SteamOven,
	"Street Superstar": StreetSuperstar,
	"The Vault": TheVault,
	"Unfettered Game Ball": UnfetteredGameBall,
	"Weeping Gemini": WeepingGemini,

	# B rank
	"[Identity] Base": IdentityBase,
	"[Identity] Inflection": IdentityInflection,
	"[Lunar] Decrescent": LunarDecrescent,
	"[Lunar] Noviluna": LunarNoviluna,
	"[Lunar] Pleniluna": LunarPleniluna,
	"[Magnetic Storm] Alpha": MagneticStormAlpha,
	"[Magnetic Storm] Bravo": MagneticStormBravo,
	"[Magnetic Storm] Charlie": MagneticStormCharlie,
	"[Reverb] Mark I": ReverbMarkI,
	"[Reverb] Mark II": ReverbMarkII,
	"[Reverb] Mark III": ReverbMarkIII,
	"[Vortex] Arrow": VortexArrow,
	"[Vortex] Hatchet": VortexHatchet,
	"[Vortex] Revolver": VortexRevolver,
}



