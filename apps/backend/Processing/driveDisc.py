import config
import re
from typing import Literal, Type

availabelMainStats: dict[Literal[1,2,3,4,5,6], list[str]] = {
	1: ['hp'],
	2: ['atk'],
	3: ['def'],
	4: ['hp_', 'atk_', 'def_', 'critRate_', 'critDMG_', 'anomalyProficiency'],
	5: ['hp_', 'atk_', 'def_', 'pen_', 'electricDMG_', 'physicalDMG_', 'fireDMG_', 'iceDMG_', 'etherDMG_'],
	6: ['hp_', 'atk_', 'def_', 'anomalyMastery_', 'energyRegen_', 'impact_']
}

mainStatBase: dict[config.RANKS, dict[str, float]] = {
	'B': {
		'hp': 183,
		'hp_': 2.5,
		'atk': 26,
		'atk_': 2.5,
		'def': 15,
		'def_': 0,
		'critRate_': 2,
		'critDMG_': 4,
		'anomalyProficiency': 0,
		'pen_': 2,
		'electricDMG_': 2.5,
		'physicalDMG_': 2.5,
		'fireDMG_': 2.5,
		'iceDMG_': 2.5,
		'etherDMG_': 2.5,
		'anomalyMastery_': 2.5,
		'energyRegen_': 0,
		'impact_': 1.5,
	},
	'A': {
		'hp': 367,
		'hp_': 5,
		'atk': 53,
		'atk_': 5,
		'def': 31,
		'def_': 0,
		'critRate_': 4,
		'critDMG_': 8,
		'anomalyProficiency': 15,
		'pen_': 4,
		'electricDMG_': 5,
		'physicalDMG_': 5,
		'fireDMG_': 5,
		'iceDMG_': 5,
		'etherDMG_': 5,
		'anomalyMastery_': 5,
		'energyRegen_': 0,
		'impact_': 3,
	},
	'S': {
		'hp': 550,
		'hp_': 7.5,
		'atk': 79,
		'atk_': 7.5,
		'def': 46,
		'def_': 12,
		'critRate_': 6,
		'critDMG_': 12,
		'anomalyProficiency': 23,
		'pen_': 6,
		'electricDMG_': 7.5,
		'physicalDMG_': 7.5,
		'fireDMG_': 7.5,
		'iceDMG_': 7.5,
		'etherDMG_': 7.5,
		'anomalyMastery_': 7.5,
		'energyRegen_': 15,
		'impact_': 4.5,
	}
}

mainStatMax: dict[config.RANKS, dict[str, float]] = {
	'B': {
		'hp': 734,
		'hp_': 10,
		'atk': 104,
		'atk_': 10,
		'def': 60,
		'def_': 16,
		'critRate_': 8,
		'critDMG_': 16,
		'anomalyProficiency': 32,
		'pen_': 8,
		'electricDMG_': 10,
		'physicalDMG_': 10,
		'fireDMG_': 10,
		'iceDMG_': 10,
		'etherDMG_': 10,
		'anomalyMastery_': 10,
		'energyRegen_': 20,
		'impact_': 6,
	},
	'A': {
		'hp': 1468,
		'hp_': 20,
		'atk': 212,
		'atk_': 20,
		'def': 124,
		'def_': 32,
		'critRate_': 16,
		'critDMG_': 32,
		'anomalyProficiency': 60,
		'pen_': 16,
		'electricDMG_': 20,
		'physicalDMG_': 20,
		'fireDMG_': 20,
		'iceDMG_': 20,
		'etherDMG_': 20,
		'anomalyMastery_': 20,
		'energyRegen_': 40,
		'impact_': 12,
	},
	'S': {
		'hp': 2200,
		'hp_': 30,
		'atk': 316,
		'atk_': 30,
		'def': 184,
		'def_': 48,
		'critRate_': 24,
		'critDMG_': 48,
		'anomalyProficiency': 92,
		'pen_': 24,
		'electricDMG_': 30,
		'physicalDMG_': 30,
		'fireDMG_': 30,
		'iceDMG_': 30,
		'etherDMG_': 30,
		'anomalyMastery_': 30,
		'energyRegen_': 60,
		'impact_': 18,
	}
}

mainStatIncrement: dict[config.RANKS, dict[str, float]] = {
	'B': {stat: (v_max-v_min)/9 for (stat, v_min), (stat, v_max) in zip(mainStatBase['B'].items(), mainStatMax['B'].items())},
	'A': {stat: (v_max-v_min)/12 for (stat, v_min), (stat, v_max) in zip(mainStatBase['A'].items(), mainStatMax['A'].items())},
	'S': {stat: (v_max-v_min)/15 for (stat, v_min), (stat, v_max) in zip(mainStatBase['S'].items(), mainStatMax['S'].items())}
}


initialNoSubStat: dict[config.RANKS, tuple[int, int]] = {
	'B': (1, 2),
	'A': (2, 3),
	'S': (3, 4),
}


subStatIncrement: dict[config.RANKS, dict[str, float]] = {
	'B':{
		'hp': 39,
		'atk': 7,
		'def': 5,
		'hp_': 1,
		'atk_': 1,
		'def_': 1.6,
		'pen': 3,
		'critRate_': 0.8,
		'critDMG_': 1.6,
		'anomalyProficiency': 3
	},
	'A':{
		'hp': 79,
		'atk': 15,
		'def': 10,
		'hp_': 2,
		'atk_': 2,
		'def_': 3.2,
		'pen': 6,
		'critRate_': 1.6,
		'critDMG_': 3.2,
		'anomalyProficiency': 6
	},
	'S':{
		'hp': 112,
		'atk': 19,
		'def': 15,
		'hp_': 3,
		'atk_': 3,
		'def_': 4.8,
		'pen': 9,
		'critRate_': 2.4,
		'critDMG_': 4.8,
		'anomalyProficiency': 9
	}
}

levelCap: dict[config.RANKS, int] = {
	'B': 9,
	'A': 12,
	'S': 15
}

incrementLevel: Literal[3] = 3


def getRangeOfSubStats(rank: config.RANKS, level: int):
	n_increase = level//incrementLevel

	return initialNoSubStat[rank][0] + n_increase, initialNoSubStat[rank][1]+n_increase

class DriveDisc:
	name: str
	passiveDescription2Pieces: str
	passiveDescription4Pieces: str
	passiveStat2Pieces: dict
	passiveStat4Pieces: dict

	pieces: list

	
	@classmethod
	def getPassive(cls, n_pieces: Literal[2, 4]):
		if n_pieces == 2:
			passive = cls.passiveDescription2Pieces.format(*[passiveStat['value'] for passiveStat in cls.passiveStat2Pieces.values()])
		elif n_pieces == 4:
			passive = cls.passiveDescription4Pieces.format(*[passiveStat['value'] for passiveStat in cls.passiveStat4Pieces.values()])
		else:
			raise ValueError("...")
		
		return {"passive": passive}	

	@classmethod
	def getRangeOfSubstat(cls, level):
		pass

class ChaoticMetal(DriveDisc):
	name = 'Chaotic Metal'

	passiveStat2Pieces = {
			"etherDMG_": {
				"value": 10
			}, 
		}

	passiveDescription2Pieces = '<p>Increases <span style=\"color: rgb(217,64,112)\">Ether DMG</span> by <span style=\"color: rgb(237,197,84)\">{0}%</span>.</p>'

	passiveStat4Pieces = {
			'squad-DMG_': {
				'value': 18,
				'mutiply': 1,
				'description': '...',
				'stackable': False
			}
		}

	passiveDescription4Pieces = '<p>Whenever a squad member inflicts <span style=\"color: rgb(217,64,112)\">Corruption</span> on an enemy, that enemy takes <span style=\"color: rgb(237,197,84)\">{0}%</span> more DMG for 12s. Passive effects of the same name do not stack.</p>'

	def __init__(self):
		super().__init__()



class FangedMetal(DriveDisc):
	name = 'Fanged Metal'

	passiveStat2Pieces = {
			"physicalDMG_": {
				"value": 10
			}, 
		}

	passiveDescription2Pieces = '<p>Increases <span style=\"color: rgb(192,168,47)\">Physical DMG</span> by <span style=\"color: rgb(237,197,84)\">{0}%</span>.</p>'

	passiveStat4Pieces = {
			'combat-DMG_': {
				'value': 35,
				'mutiply': 1,
				'description': '...'
			}
		}

	passiveDescription4Pieces = '<p>Whenever a squad member inflicts <span style=\"color: rgb(192,168,47)\">Assault</span> on an enemy, the equipper deals <span style=\"color: rgb(237,197,84)\">{0}%</span> additional DMG to the target for 12s.</p>'

	def __init__(self):
		super().__init__()



class FreedomBlues(DriveDisc):
	name = "Freedom Blues"

	passiveStat2Pieces = {
		"anomalyProficiency": {
			"value": 30
		}, 
	}

	passiveDescription2Pieces = '<p>Increases <span style=\"color: rgb(237,197,84)\">Anomaly Proficiency</span> by <span style=\"color: rgb(237,197,84)\">{0}</span>.</p>'

	

	passiveDescription4Pieces = '<p>When an EX Special Attack hits an enemy, reduce the target\'s Anomaly Buildup RES to the equipper\'s Attribute by <span style=\"color: rgb(237,197,84)\">{0}%</span> for 8s. This effect does not stack with others of the same attribute.</p>'

	def __init__(self, equiperAtribute: config.ATTRIBUTES = 'Ice'):
		super().__init__()
		self.equiperAttribute = equiperAtribute

		self.passiveStat4Pieces = {
			f'enemy-{self.equiperAttribute.lower()}AnomalyBuildUpRes_': {
				'value': 35,
				'mutiply': 1,
				'description': '...',
				'stackable': False
			}
		}

	@classmethod
	def getPassive(cls, n_pieces: Literal[2, 4]):
		if n_pieces == 2:
			passive = cls.passiveDescription2Pieces.format(*[passiveStat['value'] for passiveStat in cls.passiveStat2Pieces.values()])
		elif n_pieces == 4:
			passive = cls.passiveDescription4Pieces.format(35)
		else:
			raise ValueError("...")
		
		return {"passive": passive}	


class HormonePunk(DriveDisc):
	name = 'Hormone Punk'

	passiveStat2Pieces = {
			"atk_": {
				"value": 10
			}, 
		}

	passiveDescription2Pieces = '<p>Increases <span style=\"color: rgb(237,197,84)\">ATK</span> by <span style=\"color: rgb(237,197,84)\">{0}%</span>.</p>'

	passiveStat4Pieces = {
			'combat-atk_': {
				'value': 25,
				'mutiply': 1,
				'description': '...'
			}
		}

	passiveDescription4Pieces = '<p>Upon entering or switching into combat, the equipper has their <span style=\"color: rgb(237,197,84)\">ATK</span> increased by <span style=\"color: rgb(237,197,84)\">{0}%</span> for 8s. This effect can be triggered once every 20s.</p>'

	def __init__(self):
		super().__init__()



class InfernoMetal(DriveDisc):
	name = 'Inferno Metal'

	passiveStat2Pieces = {
			"fireDMG_": {
				"value": 10
			}, 
		}

	passiveDescription2Pieces = '<p>Increases <span style=\"color: rgb(255,85,33)\">Fire DMG</span> by <span style=\"color: rgb(237,197,84)\">{0}%</span>.</p>'

	passiveStat4Pieces = {
			'combat-critRate_': {
				'value': 28,
				'mutiply': 1,
				'description': '...'
			}
		}

	passiveDescription4Pieces	= '<p>Upon hitting a <span style=\"color: rgb(255,85,33)\">Burning</span> enemy, the equipper\'s CRIT Rate is increased by <span style=\"color: rgb(237,197,84)\">{0}%</span> for 8s.</p>'

	def __init__(self):
		super().__init__()



class PolarMetal(DriveDisc):
	name = 'Polar Metal'

	passiveStat2Pieces = {
			"iceDMG_": {
				"value": 10
			}, 
		}

	passiveDescription2Pieces = '<p>Increases <span style=\"color: rgb(140,216,218)\">Ice DMG</span> by <span style=\"color: rgb(237,197,84)\">{0}%</span>.</p>'

	passiveStat4Pieces = {
			'combat-basic*DMG_+dash*DMG_': {
				'value': 28,
				'mutiply': 1,
				'description': '...'
			},
			'combat-basic*DMG_+dash*DMG_ 2': {
				'value': 28,
				'mutiply': 1,
				'description': '...'
			}
		}

	passiveDescription4Pieces = '<p>Basic Attack and Dash Attack DMG increases by <span style=\"color: rgb(237,197,84)\">{0}%</span>. Whenever a squad member <span style=\"color: rgb(140,216,218)\">Freezes</span> or <span style=\"color: rgb(140,216,218)\">Shatters</span> an enemy, the buff further increases by <span style=\"color: rgb(237,197,84)\">{1}%</span> for 12s.</p>'

	def __init__(self):
		super().__init__()



class PufferElectro(DriveDisc):
	name = 'Puffer Electro'

	passiveStat2Pieces = {
			"pen_": {
				"value": 8
			}, 
		}

	passiveDescription2Pieces = '<p>Increases <span style=\"color: rgb(237,197,84)\">PEN Ratio</span> by <span style=\"color: rgb(237,197,84)\">{0}%</span>.</p>'

	passiveStat4Pieces = {
			'ultimate*DMG_': {
				'value': 20,
			},
			'combat-atk_': {
				'value': 15,
				'mutiply': 1,
				'description': '...'
			}
		}

	passiveDescription4Pieces = '<p><span style=\"color: rgb(237,197,84)\">Ultimate DMG</span> increases by <span style=\"color: rgb(237,197,84)\">{0}%</span>. Launching an Ultimate increases the equipper\'s <span style=\"color: rgb(237,197,84)\">ATK</span> by <span style=\"color: rgb(237,197,84)\">{1}%</span> for 12s.</p>'

	def __init__(self):
		super().__init__()



class ShockstarDisco(DriveDisc):
	name = 'Shockstar Disco'

	passiveStat2Pieces = {
			"impact_": {
				"value": 6
			}, 
		}

	passiveDescription2Pieces = '<p>Increases <span style=\"color: rgb(237,197,84)\">Impact</span> by <span style=\"color: rgb(237,197,84)\">{0}%</span>.</p>'

	passiveStat4Pieces = {
			'basic*daze_+dash*daze_+dodge*daze_+special*daze_+EXspecial*daze_': {
				'value': 15,
			}
		}

	passiveDescription4Pieces = '<p>Basic Attacks, Dash Attacks, Dodge Counter, Special Attacks, and EX Special Attacks inflict <span style=\"color: rgb(237,197,84)\">{0}%</span> more Daze upon the main target.</p>'

	def __init__(self):
		super().__init__()



class SoulRock(DriveDisc):
	name = 'Soul Rock'

	passiveStat2Pieces = {
			"def_": {
				"value": 16
			}, 
		}

	passiveDescription2Pieces = '<p>Increases <span style=\"color: rgb(237,197,84)\">DEF</span> by <span style=\"color: rgb(237,197,84)\">{0}%</span>.</p>'

	passiveStat4Pieces = {
			'combat-DMGRes_': {
				'value': 40,
			}
		}

	passiveDescription4Pieces = '<p>Upon receiving an enemy attack and losing HP, the equipper takes <span style=\"color: rgb(237,197,84)\">{0}%</span> less DMG for 2.5s. This effect can trigger once every 15s.</p>'

	def __init__(self):
		super().__init__()



class SwingJazz(DriveDisc):
	name = 'Swing Jazz'

	passiveStat2Pieces = {
			"energyRegen_": {
				"value": 20
			}, 
		}

	passiveDescription2Pieces = '<p>Increases <span style=\"color: rgb(237,197,84)\">Energy Regen</span> by <span style=\"color: rgb(237,197,84)\">{0}%</span>.</p>'

	passiveStat4Pieces = {
			'squad-DMG_': {
				'value': 15,
				'multiply': 1,
				'description': '...',
				'stackable': False
			}
		}

	passiveDescription4Pieces = '<p>Launching a Chain Attack or Ultimate increases all squad members\' DMG by <span style=\"color: rgb(237,197,84)\">{0}%</span> for 12s. Passive effects of the same name do not stack.</p>'
		

	def __init__(self):
		super().__init__()



class ThunderMetal(DriveDisc):
	name = 'Thunder Metal'

	passiveStat2Pieces = {
			"electricDMG_": {
				"value": 10
			}, 
		}

	passiveDescription2Pieces = '<p>Increases <span style=\"color: rgb(46,182,255)\">Electric DMG</span> by <span style=\"color: rgb(237,197,84)\">{0}%</span>.</p>'

	passiveStat4Pieces = {
			'combat-atk_': {
				'value': 27,
				'multiply': 1,
				'description': '...',
			}
		}

	passiveDescription4Pieces = '<p>As long as an enemy in combat is Shocked, the equipper\'s <span style=\"color: rgb(237,197,84)\">ATK</span> is increased by <span style=\"color: rgb(237,197,84)\">{0}%</span>.</p>'

	def __init__(self):
		super().__init__()



class WoodpeckerElectro(DriveDisc):
	name = 'Woodpecker Electro'

	passiveStat2Pieces = {
			"critRate_": {
				"value": 8
			}, 
		}

	passiveDescription2Pieces = '<p>Increases <span style=\"color: rgb(237,197,84)\">Crit Rate</span> by <span style=\"color: rgb(237,197,84)\">{0}%</span>.</p>'

	passiveStat4Pieces = {
			'combat-atk_': {
				'value': 9,
				'multiply': 3,
				'description': '...',
			}
		}

	passiveDescription4Pieces = '<p>Triggering a critical hit with a Basic Attack, Dodge Counter, or EX Special Attack increases the equipper\'s <span style=\"color: rgb(237,197,84)\">ATK</span> by <span style=\"color: rgb(237,197,84)\">{0}%</span> for 6s. The buff duration for different skills are calculated seperately.</p>'

	def __init__(self):
		super().__init__()





class DriveDiscSlot:
	name: str
	rank: config.RANKS
	partition: Literal[1,2,3,4,5,6]
	def __init__(self, name: str, rank: config.RANKS, partition: Literal[1,2,3,4,5,6]):
		self.name = name
		self.rank = rank
		self.partition = partition

		self.levelCap = levelCap[self.rank]

		self.availabelMainStats = availabelMainStats[self.partition]

		self.mainStat: dict[str, float] = {}
		self.subStats: dict[str, float] = {}

	def setMainStat(self, level: int, mainStat: str):
		if level < 0 or level > self.levelCap:
			raise ValueError(f"level of {self.rank} Rank Drive Disc must be between 0 to {self.levelCap}, get {level}")

		if mainStat not in self.availabelMainStats:
			raise ValueError(f'Main Stat of partition {self.partition} must be one of the following: {self.availabelMainStats}, get {mainStat}')
		
		mainStatValue = mainStatBase[self.rank][mainStat] + level*mainStatIncrement[self.rank][mainStat]

		self.mainStat = {mainStat: mainStatValue}

		return mainStatValue

	def setStats(self, level: int, mainStat, substat):
		pass

drivediscs: dict[str, Type[DriveDisc]] = {
	'Chaotic Metal': ChaoticMetal,
	'Fanged Metal': FangedMetal,
	'Freedom Blues': FreedomBlues,
	'Hormone Punk': HormonePunk,
	'Inferno Metal': InfernoMetal,
	'Polar Metal': PolarMetal,
	'Puffer Electro': PufferElectro,
	'Shockstar Disco': ShockstarDisco,
	'Soul Rock': SoulRock,
	'Swing Jazz': SwingJazz,
	'Thunder Metal': ThunderMetal,
	'Woodpecker Electro': WoodpeckerElectro,
}