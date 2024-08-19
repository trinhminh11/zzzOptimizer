import json		
import os
from .stat import Stat
from config import *

from models import WEngineModel

dirname = os.path.dirname(__file__)
baseStatFile = dirname + "/wenginetBaseStat.json"

class WEngine:
	name: str
	rank: str
	fightingType: str
	modificationLevel: int = 0
	level: int = 0
	upgradeLevel: int = 1


	mainStat: Stat = Stat()
	subStat: Stat = Stat()

	baseStatLevel: dict = {
		'mainStat': {
			0: {
				0: None,
				10: None
			},
			1: {
				10: None,
				20: None
			},
			2: {
				20: None,
				30: None
			},
			3: {
				30: None,
				40: None
			},
			4: {
				40: None,
				50: None
			},
			5: {
				50: None,
				60: None
			},
		},
		'subStat': {
			0: {
				0: None,
				10: None
			},
			1: {
				10: None,
				20: None
			},
			2: {
				20: None,
				30: None
			},
			3: {
				30: None,
				40: None
			},
			4: {
				40: None,
				50: None
			},
			5: {
				50: None,
				60: None
			},
		}
	}

	def __init__(self, name: str, rank: str, fightingStyle: str, mainStat: Stat, subStat: Stat):
		self.name = name
		if rank not in ['S', 'A', 'B']:
			raise ValueError()
		
		self.rank = rank
		
		if fightingStyle not in ['Attack', 'Stun', 'Anomaly', 'Defense', 'Support']:
			raise ValueError()
		
		self.fightingType = fightingStyle

		self.mainStat = mainStat
		self.subStat = subStat

	def fromJson(self, data: dict):
		pass

	def loadBaseStat(self, data):
		self.baseStatLevel = data

	def setLevel(self, value):
		self.level = value


class DeepSeaVisitor(WEngine):
	def __init__(self):
		super().__init__("Deep Sea Visitor", "S", "Attack", Stat("atk"), Stat("critRate_"))

		self.baseStatLevel['mainStat'][0][00], self.baseStatLevel['subStat'][0][0] = 48 , 9.6
		self.baseStatLevel['mainStat'][0][10], self.baseStatLevel['subStat'][0][10] = 123, 9.6
		self.baseStatLevel['mainStat'][1][10], self.baseStatLevel['subStat'][1][10] = 166, 12.5
		self.baseStatLevel['mainStat'][1][20], self.baseStatLevel['subStat'][1][20] = 241, 12.5
		self.baseStatLevel['mainStat'][2][20], self.baseStatLevel['subStat'][2][20] = 284, 15.4
		self.baseStatLevel['mainStat'][2][30], self.baseStatLevel['subStat'][2][30] = 359, 15.4
		self.baseStatLevel['mainStat'][3][30], self.baseStatLevel['subStat'][3][30] = 402, 18.2
		self.baseStatLevel['mainStat'][3][40], self.baseStatLevel['subStat'][3][40] = 477, 18.2
		self.baseStatLevel['mainStat'][4][40], self.baseStatLevel['subStat'][4][40] = 520, 21.1
		self.baseStatLevel['mainStat'][4][50], self.baseStatLevel['subStat'][4][50] = 595, 21.1
		self.baseStatLevel['mainStat'][4][50], self.baseStatLevel['subStat'][5][50] = 638, 24.0
		self.baseStatLevel['mainStat'][4][60], self.baseStatLevel['subStat'][5][60] = 713, 24.0

	

class FusionCompiler(WEngine):
	def __init__(self):
		super().__init__("Fusion Compiler", "S", "Anomaly", Stat("atk"), Stat("pen_"))
		self.baseStatLevel['mainStat'][0][0], self.baseStatLevel['subStat'][0][0] = 46 , 9.6
		self.baseStatLevel['mainStat'][0][10], self.baseStatLevel['subStat'][0][10] = 118 , 9.6
		self.baseStatLevel['mainStat'][1][10], self.baseStatLevel['subStat'][1][10] = 159 , 12.5
		self.baseStatLevel['mainStat'][1][20], self.baseStatLevel['subStat'][1][20] = 231 , 12.5
		self.baseStatLevel['mainStat'][2][20], self.baseStatLevel['subStat'][2][20] = 272 , 15.4
		self.baseStatLevel['mainStat'][2][30], self.baseStatLevel['subStat'][2][30] = 344 , 15.4
		self.baseStatLevel['mainStat'][3][30], self.baseStatLevel['subStat'][3][30] = 385 , 18.2
		self.baseStatLevel['mainStat'][3][40], self.baseStatLevel['subStat'][3][40] = 457 , 18.2
		self.baseStatLevel['mainStat'][4][40], self.baseStatLevel['subStat'][4][40] = 498 , 21.1
		self.baseStatLevel['mainStat'][4][50], self.baseStatLevel['subStat'][4][50] = 570 , 21.1
		self.baseStatLevel['mainStat'][5][50], self.baseStatLevel['subStat'][5][50] = 611 , 24.0
		self.baseStatLevel['mainStat'][5][60], self.baseStatLevel['subStat'][5][60] = 684 , 24.0


class HellfireGears(WEngine):
	def __init__(self):
		super().__init__("Hellfire Gears", "S", "Stun", Stat("atk"), Stat("impact_"))
		self.baseStatLevel['mainStat'][0][0], self.baseStatLevel['subStat'][0][0] = 46 , 7.2
		self.baseStatLevel['mainStat'][0][10], self.baseStatLevel['subStat'][0][10] = 118 , 7.2
		self.baseStatLevel['mainStat'][1][10], self.baseStatLevel['subStat'][1][10] = 159 , 9.4
		self.baseStatLevel['mainStat'][1][20], self.baseStatLevel['subStat'][1][20] = 231 , 9.4
		self.baseStatLevel['mainStat'][2][20], self.baseStatLevel['subStat'][2][20] = 272 , 11.5
		self.baseStatLevel['mainStat'][2][30], self.baseStatLevel['subStat'][2][30] = 344 , 11.5
		self.baseStatLevel['mainStat'][3][30], self.baseStatLevel['subStat'][3][30] = 385 , 13.7
		self.baseStatLevel['mainStat'][3][40], self.baseStatLevel['subStat'][3][40] = 457 , 13.7
		self.baseStatLevel['mainStat'][4][40], self.baseStatLevel['subStat'][4][40] = 498 , 15.8
		self.baseStatLevel['mainStat'][4][50], self.baseStatLevel['subStat'][4][50] = 570 , 15.8
		self.baseStatLevel['mainStat'][5][50], self.baseStatLevel['subStat'][5][50] = 611 , 18.0
		self.baseStatLevel['mainStat'][5][60], self.baseStatLevel['subStat'][5][60] = 684 , 18.0

		

class RiotSuppressorMarkVI(WEngine):
	def __init__(self):
		super().__init__("Riot Suppressor Mark VI", "S", "Attack", Stat("atk"), Stat("critDMG_"))
		self.baseStatLevel['mainStat'][0][0], self.baseStatLevel['subStat'][0][0] = 48 , 19.2
		self.baseStatLevel['mainStat'][0][10], self.baseStatLevel['subStat'][0][10] = 123 , 19.2
		self.baseStatLevel['mainStat'][1][10], self.baseStatLevel['subStat'][1][10] = 166 , 25.0
		self.baseStatLevel['mainStat'][1][20], self.baseStatLevel['subStat'][1][20] = 241 , 25.0
		self.baseStatLevel['mainStat'][2][20], self.baseStatLevel['subStat'][2][20] = 284 , 30.7
		self.baseStatLevel['mainStat'][2][30], self.baseStatLevel['subStat'][2][30] = 359 , 30.7
		self.baseStatLevel['mainStat'][3][30], self.baseStatLevel['subStat'][3][30] = 402 , 36.5
		self.baseStatLevel['mainStat'][3][40], self.baseStatLevel['subStat'][3][40] = 477 , 36.5
		self.baseStatLevel['mainStat'][4][40], self.baseStatLevel['subStat'][4][40] = 520 , 42.2
		self.baseStatLevel['mainStat'][4][50], self.baseStatLevel['subStat'][4][50] = 595 , 42.2
		self.baseStatLevel['mainStat'][5][50], self.baseStatLevel['subStat'][5][50] = 638 , 48.0
		self.baseStatLevel['mainStat'][5][60], self.baseStatLevel['subStat'][5][60] = 713 , 48.0


class SteelCushion(WEngine):
	def __init__(self):
		super().__init__("Steel Cushion", "S", "Attack", Stat("atk"), Stat("critRate_"))
		self.baseStatLevel['mainStat'][0][0], self.baseStatLevel['subStat'][0][0] = 46 , 9.6
		self.baseStatLevel['mainStat'][0][10], self.baseStatLevel['subStat'][0][10] = 118 , 9.6
		self.baseStatLevel['mainStat'][1][10], self.baseStatLevel['subStat'][1][10] = 159 , 12.5
		self.baseStatLevel['mainStat'][1][20], self.baseStatLevel['subStat'][1][20] = 231 , 12.5
		self.baseStatLevel['mainStat'][2][20], self.baseStatLevel['subStat'][2][20] = 272 , 15.4
		self.baseStatLevel['mainStat'][2][30], self.baseStatLevel['subStat'][2][30] = 344 , 15.4
		self.baseStatLevel['mainStat'][3][30], self.baseStatLevel['subStat'][3][30] = 385 , 18.2
		self.baseStatLevel['mainStat'][3][40], self.baseStatLevel['subStat'][3][40] = 457 , 18.2
		self.baseStatLevel['mainStat'][4][40], self.baseStatLevel['subStat'][4][40] = 498 , 21.1
		self.baseStatLevel['mainStat'][4][50], self.baseStatLevel['subStat'][4][50] = 570 , 21.1
		self.baseStatLevel['mainStat'][5][50], self.baseStatLevel['subStat'][5][50] = 611 , 24.0
		self.baseStatLevel['mainStat'][5][60], self.baseStatLevel['subStat'][5][60] = 684 , 24.0


class TheBrimstone(WEngine):
	def __init__(self):
		super().__init__("The Brimstone", "S", "Attack", Stat("atk"), Stat("atk_"))
		self.baseStatLevel['mainStat'][0][0], self.baseStatLevel['subStat'][0][0] = 46 , 12.0
		self.baseStatLevel['mainStat'][0][10], self.baseStatLevel['subStat'][0][10] = 118 , 12.0
		self.baseStatLevel['mainStat'][1][10], self.baseStatLevel['subStat'][1][10] = 159 , 15.6
		self.baseStatLevel['mainStat'][1][20], self.baseStatLevel['subStat'][1][20] = 231 , 15.6
		self.baseStatLevel['mainStat'][2][20], self.baseStatLevel['subStat'][2][20] = 272 , 19.2
		self.baseStatLevel['mainStat'][2][30], self.baseStatLevel['subStat'][2][30] = 344 , 19.2
		self.baseStatLevel['mainStat'][3][30], self.baseStatLevel['subStat'][3][30] = 385 , 22.8
		self.baseStatLevel['mainStat'][3][40], self.baseStatLevel['subStat'][3][40] = 457 , 22.8
		self.baseStatLevel['mainStat'][4][40], self.baseStatLevel['subStat'][4][40] = 498 , 26.4
		self.baseStatLevel['mainStat'][4][50], self.baseStatLevel['subStat'][4][50] = 570 , 26.4
		self.baseStatLevel['mainStat'][5][50], self.baseStatLevel['subStat'][5][50] = 611 , 30.0
		self.baseStatLevel['mainStat'][5][60], self.baseStatLevel['subStat'][5][60] = 684 , 30.0


class TheRestrained(WEngine):
	def __init__(self):
		super().__init__("The Restrained", "S", "Stun", Stat("atk"), Stat("impact_"))
		self.baseStatLevel['mainStat'][0][0], self.baseStatLevel['subStat'][0][0] = 46 , 7.2
		self.baseStatLevel['mainStat'][0][10], self.baseStatLevel['subStat'][0][10] = 118 , 7.2
		self.baseStatLevel['mainStat'][1][10], self.baseStatLevel['subStat'][1][10] = 159 , 9.4
		self.baseStatLevel['mainStat'][1][20], self.baseStatLevel['subStat'][1][20] = 231 , 9.4
		self.baseStatLevel['mainStat'][2][20], self.baseStatLevel['subStat'][2][20] = 272 , 11.5
		self.baseStatLevel['mainStat'][2][30], self.baseStatLevel['subStat'][2][30] = 344 , 11.5
		self.baseStatLevel['mainStat'][3][30], self.baseStatLevel['subStat'][3][30] = 385 , 13.7
		self.baseStatLevel['mainStat'][3][40], self.baseStatLevel['subStat'][3][40] = 457 , 13.7
		self.baseStatLevel['mainStat'][4][40], self.baseStatLevel['subStat'][4][40] = 498 , 15.8
		self.baseStatLevel['mainStat'][4][50], self.baseStatLevel['subStat'][4][50] = 570 , 15.8
		self.baseStatLevel['mainStat'][5][50], self.baseStatLevel['subStat'][5][50] = 611 , 18.0
		self.baseStatLevel['mainStat'][5][60], self.baseStatLevel['subStat'][5][60] = 684 , 18.0


class WeepingCradle(WEngine):
	def __init__(self):
		super().__init__("Weeping Cradle", "S", "Support", Stat("atk"), Stat("pen_"))
		self.baseStatLevel['mainStat'][0][0], self.baseStatLevel['subStat'][0][0] = 46 , 9.6
		self.baseStatLevel['mainStat'][0][10], self.baseStatLevel['subStat'][0][10] = 118 , 9.6
		self.baseStatLevel['mainStat'][1][10], self.baseStatLevel['subStat'][1][10] = 159 , 12.5
		self.baseStatLevel['mainStat'][1][20], self.baseStatLevel['subStat'][1][20] = 231 , 12.5
		self.baseStatLevel['mainStat'][2][20], self.baseStatLevel['subStat'][2][20] = 272 , 15.4
		self.baseStatLevel['mainStat'][2][30], self.baseStatLevel['subStat'][2][30] = 344 , 15.4
		self.baseStatLevel['mainStat'][3][30], self.baseStatLevel['subStat'][3][30] = 385 , 18.2
		self.baseStatLevel['mainStat'][3][40], self.baseStatLevel['subStat'][3][40] = 457 , 18.2
		self.baseStatLevel['mainStat'][4][40], self.baseStatLevel['subStat'][4][40] = 498 , 21.1
		self.baseStatLevel['mainStat'][4][50], self.baseStatLevel['subStat'][4][50] = 570 , 21.1
		self.baseStatLevel['mainStat'][5][50], self.baseStatLevel['subStat'][5][50] = 611 , 24.0
		self.baseStatLevel['mainStat'][5][60], self.baseStatLevel['subStat'][5][60] = 684 , 24.0


class BashfulDemon(WEngine):
	def __init__(self):
		super().__init__("Bashful Demon", "A", "Support", Stat("atk"), Stat("atk_"))

		self.baseStatLevel['mainStat'][0][0], self.baseStatLevel['subStat'][0][0] = 42 , 10.0
		self.baseStatLevel['mainStat'][0][10], self.baseStatLevel['subStat'][0][10] = 107 , 10.0
		self.baseStatLevel['mainStat'][1][10], self.baseStatLevel['subStat'][1][10] = 145 , 13.0
		self.baseStatLevel['mainStat'][1][20], self.baseStatLevel['subStat'][1][20] = 211 , 13.0
		self.baseStatLevel['mainStat'][2][20], self.baseStatLevel['subStat'][2][20] = 248 , 16.0
		self.baseStatLevel['mainStat'][2][30], self.baseStatLevel['subStat'][2][30] = 314 , 16.0
		self.baseStatLevel['mainStat'][3][30], self.baseStatLevel['subStat'][3][30] = 352 , 19.0
		self.baseStatLevel['mainStat'][3][40], self.baseStatLevel['subStat'][3][40] = 417 , 19.0
		self.baseStatLevel['mainStat'][4][40], self.baseStatLevel['subStat'][4][40] = 455 , 22.0
		self.baseStatLevel['mainStat'][4][50], self.baseStatLevel['subStat'][4][50] = 521 , 22.0
		self.baseStatLevel['mainStat'][5][50], self.baseStatLevel['subStat'][5][50] = 558 , 25.0
		self.baseStatLevel['mainStat'][5][60], self.baseStatLevel['subStat'][5][60] = 624 , 25.0



class BigCylinder(WEngine):
	def __init__(self):
		super().__init__("Big Cylinder", "A", "Defense", Stat("atk"), Stat("def_"))
		self.baseStatLevel['mainStat'][0][0], self.baseStatLevel['subStat'][0][0] = 42 , 16.0
		self.baseStatLevel['mainStat'][0][10], self.baseStatLevel['subStat'][0][10] = 107 , 16.0
		self.baseStatLevel['mainStat'][1][10], self.baseStatLevel['subStat'][1][10] = 145 , 20.8
		self.baseStatLevel['mainStat'][1][20], self.baseStatLevel['subStat'][1][20] = 211 , 20.8
		self.baseStatLevel['mainStat'][2][20], self.baseStatLevel['subStat'][2][20] = 248 , 25.6
		self.baseStatLevel['mainStat'][2][30], self.baseStatLevel['subStat'][2][30] = 314 , 25.6
		self.baseStatLevel['mainStat'][3][30], self.baseStatLevel['subStat'][3][30] = 352 , 30.4
		self.baseStatLevel['mainStat'][3][40], self.baseStatLevel['subStat'][3][40] = 417 , 30.4
		self.baseStatLevel['mainStat'][4][40], self.baseStatLevel['subStat'][4][40] = 455 , 35.2
		self.baseStatLevel['mainStat'][4][50], self.baseStatLevel['subStat'][4][50] = 521 , 35.2
		self.baseStatLevel['mainStat'][5][50], self.baseStatLevel['subStat'][5][50] = 558 , 40.0
		self.baseStatLevel['mainStat'][5][60], self.baseStatLevel['subStat'][5][60] = 624 , 40.0



class BunnyBand(WEngine):
	def __init__(self):
		super().__init__("Bunny Band", "A", "Defense", Stat("atk"), Stat("def_"))
		self.baseStatLevel['mainStat'][0][0], self.baseStatLevel['subStat'][0][0] = 40 , 16.0
		self.baseStatLevel['mainStat'][0][10], self.baseStatLevel['subStat'][0][10] = 102 , 16.0
		self.baseStatLevel['mainStat'][1][10], self.baseStatLevel['subStat'][1][10] = 138 , 20.8
		self.baseStatLevel['mainStat'][1][20], self.baseStatLevel['subStat'][1][20] = 201 , 20.8
		self.baseStatLevel['mainStat'][2][20], self.baseStatLevel['subStat'][2][20] = 236 , 25.6
		self.baseStatLevel['mainStat'][2][30], self.baseStatLevel['subStat'][2][30] = 299 , 25.6
		self.baseStatLevel['mainStat'][3][30], self.baseStatLevel['subStat'][3][30] = 335 , 30.4
		self.baseStatLevel['mainStat'][3][40], self.baseStatLevel['subStat'][3][40] = 397 , 30.4
		self.baseStatLevel['mainStat'][4][40], self.baseStatLevel['subStat'][4][40] = 433 , 35.2
		self.baseStatLevel['mainStat'][4][50], self.baseStatLevel['subStat'][4][50] = 496 , 35.2
		self.baseStatLevel['mainStat'][5][50], self.baseStatLevel['subStat'][5][50] = 532 , 40.0
		self.baseStatLevel['mainStat'][5][60], self.baseStatLevel['subStat'][5][60] = 594 , 40.0


class CannonRotor(WEngine):
	def __init__(self):
		super().__init__("Cannon Rotor", "A", "Attack", Stat("atk"), Stat("critRate_"))
		self.baseStatLevel['mainStat'][0][0], self.baseStatLevel['subStat'][0][0] = 40 , 8.0
		self.baseStatLevel['mainStat'][0][10], self.baseStatLevel['subStat'][0][10] = 102 , 8.0
		self.baseStatLevel['mainStat'][1][10], self.baseStatLevel['subStat'][1][10] = 138 , 10.4
		self.baseStatLevel['mainStat'][1][20], self.baseStatLevel['subStat'][1][20] = 201 , 10.4
		self.baseStatLevel['mainStat'][2][20], self.baseStatLevel['subStat'][2][20] = 236 , 12.8
		self.baseStatLevel['mainStat'][2][30], self.baseStatLevel['subStat'][2][30] = 299 , 12.8
		self.baseStatLevel['mainStat'][3][30], self.baseStatLevel['subStat'][3][30] = 335 , 15.2
		self.baseStatLevel['mainStat'][3][40], self.baseStatLevel['subStat'][3][40] = 397 , 15.2
		self.baseStatLevel['mainStat'][4][40], self.baseStatLevel['subStat'][4][40] = 433 , 17.6
		self.baseStatLevel['mainStat'][4][50], self.baseStatLevel['subStat'][4][50] = 496 , 17.6
		self.baseStatLevel['mainStat'][5][50], self.baseStatLevel['subStat'][5][50] = 532 , 20.0
		self.baseStatLevel['mainStat'][5][60], self.baseStatLevel['subStat'][5][60] = 594 , 20.0


class DemaraBatteryMarkII(WEngine):
	def __init__(self):
		super().__init__("Demara Battery Mark II", "A", "Stun", Stat("atk"), Stat("impact_"))

		self.baseStatLevel['mainStat'][0][0], self.baseStatLevel['subStat'][0][0] = 42 , 6.0
		self.baseStatLevel['mainStat'][0][10], self.baseStatLevel['subStat'][0][10] = 107 , 6.0
		self.baseStatLevel['mainStat'][1][10], self.baseStatLevel['subStat'][1][10] = 145 , 7.8
		self.baseStatLevel['mainStat'][1][20], self.baseStatLevel['subStat'][1][20] = 211 , 7.8
		self.baseStatLevel['mainStat'][2][20], self.baseStatLevel['subStat'][2][20] = 248 , 9.6
		self.baseStatLevel['mainStat'][2][30], self.baseStatLevel['subStat'][2][30] = 314 , 9.6
		self.baseStatLevel['mainStat'][3][30], self.baseStatLevel['subStat'][3][30] = 352 , 11.4
		self.baseStatLevel['mainStat'][3][40], self.baseStatLevel['subStat'][3][40] = 417 , 11.4
		self.baseStatLevel['mainStat'][4][40], self.baseStatLevel['subStat'][4][40] = 455 , 13.2
		self.baseStatLevel['mainStat'][4][50], self.baseStatLevel['subStat'][4][50] = 521 , 13.2
		self.baseStatLevel['mainStat'][5][50], self.baseStatLevel['subStat'][5][50] = 558 , 15.0
		self.baseStatLevel['mainStat'][5][60], self.baseStatLevel['subStat'][5][60] = 624 , 15.0


class DrillRigRedAxis(WEngine):
	def __init__(self):
		super().__init__("Drill Rig - Red Axis", "A", "Attack", Stat("atk"), Stat("energyRegen_"))

		self.baseStatLevel['mainStat'][0][0], self.baseStatLevel['subStat'][0][0] = 42 , 20.0
		self.baseStatLevel['mainStat'][0][10], self.baseStatLevel['subStat'][0][10] = 107 , 20.0
		self.baseStatLevel['mainStat'][1][10], self.baseStatLevel['subStat'][1][10] = 145 , 26.0
		self.baseStatLevel['mainStat'][1][20], self.baseStatLevel['subStat'][1][20] = 211 , 26.0
		self.baseStatLevel['mainStat'][2][20], self.baseStatLevel['subStat'][2][20] = 248 , 32.0
		self.baseStatLevel['mainStat'][2][30], self.baseStatLevel['subStat'][2][30] = 314 , 32.0
		self.baseStatLevel['mainStat'][3][30], self.baseStatLevel['subStat'][3][30] = 352 , 38.0
		self.baseStatLevel['mainStat'][3][40], self.baseStatLevel['subStat'][3][40] = 417 , 38.0
		self.baseStatLevel['mainStat'][4][40], self.baseStatLevel['subStat'][4][40] = 455 , 44.0
		self.baseStatLevel['mainStat'][4][50], self.baseStatLevel['subStat'][4][50] = 521 , 44.0
		self.baseStatLevel['mainStat'][5][50], self.baseStatLevel['subStat'][5][50] = 558 , 50.0
		self.baseStatLevel['mainStat'][5][60], self.baseStatLevel['subStat'][5][60] = 624 , 50.0


class ElectroLipGloss(WEngine):
	def __init__(self):
		super().__init__("Electro-Lip Gloss", "A", "Anomaly", Stat("atk"), Stat("anomalyProficiency"))

		self.baseStatLevel['mainStat'][0][0], self.baseStatLevel['subStat'][0][0] = 40 , 30.0
		self.baseStatLevel['mainStat'][0][10], self.baseStatLevel['subStat'][0][10] = 102 , 30.0
		self.baseStatLevel['mainStat'][1][10], self.baseStatLevel['subStat'][1][10] = 138 , 39.0
		self.baseStatLevel['mainStat'][1][20], self.baseStatLevel['subStat'][1][20] = 201 , 39.0
		self.baseStatLevel['mainStat'][2][20], self.baseStatLevel['subStat'][2][20] = 236 , 48.0
		self.baseStatLevel['mainStat'][2][30], self.baseStatLevel['subStat'][2][30] = 299 , 48.0
		self.baseStatLevel['mainStat'][3][30], self.baseStatLevel['subStat'][3][30] = 335 , 57.0
		self.baseStatLevel['mainStat'][3][40], self.baseStatLevel['subStat'][3][40] = 397 , 57.0
		self.baseStatLevel['mainStat'][4][40], self.baseStatLevel['subStat'][4][40] = 433 , 66.0
		self.baseStatLevel['mainStat'][4][50], self.baseStatLevel['subStat'][4][50] = 496 , 66.0
		self.baseStatLevel['mainStat'][5][50], self.baseStatLevel['subStat'][5][50] = 532 , 75.0
		self.baseStatLevel['mainStat'][5][60], self.baseStatLevel['subStat'][5][60] = 594 , 75.0


class Housekeeper(WEngine):
	def __init__(self):
		super().__init__("Housekeeper", "A", "Attack", Stat("atk"), Stat("atk_"))
		self.baseStatLevel['mainStat'][0][0], self.baseStatLevel['subStat'][0][0] = 42 , 10.0
		self.baseStatLevel['mainStat'][0][10], self.baseStatLevel['subStat'][0][10] = 107 , 10.0
		self.baseStatLevel['mainStat'][1][10], self.baseStatLevel['subStat'][1][10] = 145 , 13.0
		self.baseStatLevel['mainStat'][1][20], self.baseStatLevel['subStat'][1][20] = 211 , 13.0
		self.baseStatLevel['mainStat'][2][20], self.baseStatLevel['subStat'][2][20] = 248 , 16.0
		self.baseStatLevel['mainStat'][2][30], self.baseStatLevel['subStat'][2][30] = 314 , 16.0
		self.baseStatLevel['mainStat'][3][30], self.baseStatLevel['subStat'][3][30] = 352 , 19.0
		self.baseStatLevel['mainStat'][3][40], self.baseStatLevel['subStat'][3][40] = 417 , 19.0
		self.baseStatLevel['mainStat'][4][40], self.baseStatLevel['subStat'][4][40] = 455 , 22.0
		self.baseStatLevel['mainStat'][4][50], self.baseStatLevel['subStat'][4][50] = 521 , 22.0
		self.baseStatLevel['mainStat'][5][50], self.baseStatLevel['subStat'][5][50] = 558 , 25.0
		self.baseStatLevel['mainStat'][5][60], self.baseStatLevel['subStat'][5][60] = 624 , 25.0


class KaboomtheCannon(WEngine):
	def __init__(self):
		super().__init__("Kaboom the Cannon", "A", "Support", Stat("atk"), Stat("energyRegen_"))
		self.baseStatLevel['mainStat'][0][0], self.baseStatLevel['subStat'][0][0] = 42 , 20.0
		self.baseStatLevel['mainStat'][0][10], self.baseStatLevel['subStat'][0][10] = 107 , 20.0
		self.baseStatLevel['mainStat'][1][10], self.baseStatLevel['subStat'][1][10] = 145 , 26.0
		self.baseStatLevel['mainStat'][1][20], self.baseStatLevel['subStat'][1][20] = 211 , 26.0
		self.baseStatLevel['mainStat'][2][20], self.baseStatLevel['subStat'][2][20] = 248 , 32.0
		self.baseStatLevel['mainStat'][2][30], self.baseStatLevel['subStat'][2][30] = 314 , 32.0
		self.baseStatLevel['mainStat'][3][30], self.baseStatLevel['subStat'][3][30] = 352 , 38.0
		self.baseStatLevel['mainStat'][3][40], self.baseStatLevel['subStat'][3][40] = 417 , 38.0
		self.baseStatLevel['mainStat'][4][40], self.baseStatLevel['subStat'][4][40] = 455 , 44.0
		self.baseStatLevel['mainStat'][4][50], self.baseStatLevel['subStat'][4][50] = 521 , 44.0
		self.baseStatLevel['mainStat'][5][50], self.baseStatLevel['subStat'][5][50] = 558 , 50.0
		self.baseStatLevel['mainStat'][5][60], self.baseStatLevel['subStat'][5][60] = 624 , 50.0


class OriginalTransmorpher(WEngine):
	def __init__(self):
		super().__init__("Original Transmorpher", "A", "Defense", Stat("atk"), Stat("hp_"))

		self.baseStatLevel['mainStat'][0][0], self.baseStatLevel['subStat'][0][0] = 40 , 10.0
		self.baseStatLevel['mainStat'][0][10], self.baseStatLevel['subStat'][0][10] = 102 , 10.0
		self.baseStatLevel['mainStat'][1][10], self.baseStatLevel['subStat'][1][10] = 138 , 13.0
		self.baseStatLevel['mainStat'][1][20], self.baseStatLevel['subStat'][1][20] = 201 , 13.0
		self.baseStatLevel['mainStat'][2][20], self.baseStatLevel['subStat'][2][20] = 236 , 16.0
		self.baseStatLevel['mainStat'][2][30], self.baseStatLevel['subStat'][2][30] = 299 , 16.0
		self.baseStatLevel['mainStat'][3][30], self.baseStatLevel['subStat'][3][30] = 335 , 19.0
		self.baseStatLevel['mainStat'][3][40], self.baseStatLevel['subStat'][3][40] = 397 , 19.0
		self.baseStatLevel['mainStat'][4][40], self.baseStatLevel['subStat'][4][40] = 433 , 22.0
		self.baseStatLevel['mainStat'][4][50], self.baseStatLevel['subStat'][4][50] = 496 , 22.0
		self.baseStatLevel['mainStat'][5][50], self.baseStatLevel['subStat'][5][50] = 532 , 25.0
		self.baseStatLevel['mainStat'][5][60], self.baseStatLevel['subStat'][5][60] = 594 , 25.0


class PreciousFossilizedCore(WEngine):
	def __init__(self):
		super().__init__("Precious Fossilized Core", "A", "Stun", Stat("atk"), Stat("impact_"))
		self.baseStatLevel['mainStat'][0][0], self.baseStatLevel['subStat'][0][0] = 40 , 6.0
		self.baseStatLevel['mainStat'][0][10], self.baseStatLevel['subStat'][0][10] = 102 , 6.0
		self.baseStatLevel['mainStat'][1][10], self.baseStatLevel['subStat'][1][10] = 138 , 7.8
		self.baseStatLevel['mainStat'][1][20], self.baseStatLevel['subStat'][1][20] = 201 , 7.8
		self.baseStatLevel['mainStat'][2][20], self.baseStatLevel['subStat'][2][20] = 236 , 9.6
		self.baseStatLevel['mainStat'][2][30], self.baseStatLevel['subStat'][2][30] = 299 , 9.6
		self.baseStatLevel['mainStat'][3][30], self.baseStatLevel['subStat'][3][30] = 335 , 11.4
		self.baseStatLevel['mainStat'][3][40], self.baseStatLevel['subStat'][3][40] = 397 , 11.4
		self.baseStatLevel['mainStat'][4][40], self.baseStatLevel['subStat'][4][40] = 433 , 13.2
		self.baseStatLevel['mainStat'][4][50], self.baseStatLevel['subStat'][4][50] = 496 , 13.2
		self.baseStatLevel['mainStat'][5][50], self.baseStatLevel['subStat'][5][50] = 532 , 15.0
		self.baseStatLevel['mainStat'][5][60], self.baseStatLevel['subStat'][5][60] = 594 , 15.0


class RainforestGourmet(WEngine):
	def __init__(self):
		super().__init__("Rainforest Gourmet", "A", "Anomaly", Stat("atk"), Stat("anomalyProficiency"))

		self.baseStatLevel['mainStat'][0][0], self.baseStatLevel['subStat'][0][0] = 40 , 30.0
		self.baseStatLevel['mainStat'][0][10], self.baseStatLevel['subStat'][0][10] = 102 , 30.0
		self.baseStatLevel['mainStat'][1][10], self.baseStatLevel['subStat'][1][10] = 138 , 39.0
		self.baseStatLevel['mainStat'][1][20], self.baseStatLevel['subStat'][1][20] = 201 , 39.0
		self.baseStatLevel['mainStat'][2][20], self.baseStatLevel['subStat'][2][20] = 236 , 48.0
		self.baseStatLevel['mainStat'][2][30], self.baseStatLevel['subStat'][2][30] = 299 , 48.0
		self.baseStatLevel['mainStat'][3][30], self.baseStatLevel['subStat'][3][30] = 335 , 57.0
		self.baseStatLevel['mainStat'][3][40], self.baseStatLevel['subStat'][3][40] = 397 , 57.0
		self.baseStatLevel['mainStat'][4][40], self.baseStatLevel['subStat'][4][40] = 433 , 66.0
		self.baseStatLevel['mainStat'][4][50], self.baseStatLevel['subStat'][4][50] = 496 , 66.0
		self.baseStatLevel['mainStat'][5][50], self.baseStatLevel['subStat'][5][50] = 532 , 75.0
		self.baseStatLevel['mainStat'][5][60], self.baseStatLevel['subStat'][5][60] = 594 , 75.0


class RoaringRide(WEngine):
	def __init__(self):
		super().__init__("Roaring Ride", "A", "Anomaly", Stat("atk"), Stat("atk_"))

		self.baseStatLevel['mainStat'][0][0], self.baseStatLevel['subStat'][0][0] = 42 , 10.0
		self.baseStatLevel['mainStat'][0][10], self.baseStatLevel['subStat'][0][10] = 107 , 10.0
		self.baseStatLevel['mainStat'][1][10], self.baseStatLevel['subStat'][1][10] = 145 , 13.0
		self.baseStatLevel['mainStat'][1][20], self.baseStatLevel['subStat'][1][20] = 211 , 13.0
		self.baseStatLevel['mainStat'][2][20], self.baseStatLevel['subStat'][2][20] = 248 , 16.0
		self.baseStatLevel['mainStat'][2][30], self.baseStatLevel['subStat'][2][30] = 314 , 16.0
		self.baseStatLevel['mainStat'][3][30], self.baseStatLevel['subStat'][3][30] = 352 , 19.0
		self.baseStatLevel['mainStat'][3][40], self.baseStatLevel['subStat'][3][40] = 417 , 19.0
		self.baseStatLevel['mainStat'][4][40], self.baseStatLevel['subStat'][4][40] = 455 , 22.0
		self.baseStatLevel['mainStat'][4][50], self.baseStatLevel['subStat'][4][50] = 521 , 22.0
		self.baseStatLevel['mainStat'][5][50], self.baseStatLevel['subStat'][5][50] = 558 , 25.0
		self.baseStatLevel['mainStat'][5][60], self.baseStatLevel['subStat'][5][60] = 624 , 25.0


class SixShooter(WEngine):
	def __init__(self):
		super().__init__("Six Shooter", "A", "Stun", Stat("atk"), Stat("impact_"))

		self.baseStatLevel['mainStat'][0][0], self.baseStatLevel['subStat'][0][0] = 40 , 6.0
		self.baseStatLevel['mainStat'][0][10], self.baseStatLevel['subStat'][0][10] = 102 , 6.0
		self.baseStatLevel['mainStat'][1][10], self.baseStatLevel['subStat'][1][10] = 138 , 7.8
		self.baseStatLevel['mainStat'][1][20], self.baseStatLevel['subStat'][1][20] = 201 , 7.8
		self.baseStatLevel['mainStat'][2][20], self.baseStatLevel['subStat'][2][20] = 236 , 9.6
		self.baseStatLevel['mainStat'][2][30], self.baseStatLevel['subStat'][2][30] = 299 , 9.6
		self.baseStatLevel['mainStat'][3][30], self.baseStatLevel['subStat'][3][30] = 335 , 11.4
		self.baseStatLevel['mainStat'][3][40], self.baseStatLevel['subStat'][3][40] = 397 , 11.4
		self.baseStatLevel['mainStat'][4][40], self.baseStatLevel['subStat'][4][40] = 433 , 13.2
		self.baseStatLevel['mainStat'][4][50], self.baseStatLevel['subStat'][4][50] = 496 , 13.2
		self.baseStatLevel['mainStat'][5][50], self.baseStatLevel['subStat'][5][50] = 532 , 15.0
		self.baseStatLevel['mainStat'][5][60], self.baseStatLevel['subStat'][5][60] = 594 , 15.0


class SliceofTime(WEngine):
	def __init__(self):
		super().__init__("Slice of Time", "A", "Support", Stat("atk"), Stat("pen_"))

		# this motherfucker is fucking wrong

		self.baseStatLevel['mainStat'][0][0], self.baseStatLevel['subStat'][0][0] = 40 , 10.0
		self.baseStatLevel['mainStat'][0][10], self.baseStatLevel['subStat'][0][10] = 102 , 10.0
		self.baseStatLevel['mainStat'][1][10], self.baseStatLevel['subStat'][1][10] = 138 , 13.0
		self.baseStatLevel['mainStat'][1][20], self.baseStatLevel['subStat'][1][20] = 201 , 13.0
		self.baseStatLevel['mainStat'][2][20], self.baseStatLevel['subStat'][2][20] = 236 , 16.0
		self.baseStatLevel['mainStat'][2][30], self.baseStatLevel['subStat'][2][30] = 299 , 16.0
		self.baseStatLevel['mainStat'][3][30], self.baseStatLevel['subStat'][3][30] = 335 , 19.0
		self.baseStatLevel['mainStat'][3][40], self.baseStatLevel['subStat'][3][40] = 397 , 19.0
		self.baseStatLevel['mainStat'][4][40], self.baseStatLevel['subStat'][4][40] = 433 , 22.0
		self.baseStatLevel['mainStat'][4][50], self.baseStatLevel['subStat'][4][50] = 496 , 22.0
		self.baseStatLevel['mainStat'][5][50], self.baseStatLevel['subStat'][5][50] = 532 , 25.0
		self.baseStatLevel['mainStat'][5][60], self.baseStatLevel['subStat'][5][60] = 594 , 25.0


class SpringEmbrace(WEngine):
	def __init__(self):
		super().__init__("Spring Embrace", "A", "Defense", Stat("atk"), Stat("atk_"))

		self.baseStatLevel['mainStat'][0][0], self.baseStatLevel['subStat'][0][0] = 40 , 10.0
		self.baseStatLevel['mainStat'][0][10], self.baseStatLevel['subStat'][0][10] = 102 , 10.0
		self.baseStatLevel['mainStat'][1][10], self.baseStatLevel['subStat'][1][10] = 138 , 13.0
		self.baseStatLevel['mainStat'][1][20], self.baseStatLevel['subStat'][1][20] = 201 , 13.0
		self.baseStatLevel['mainStat'][2][20], self.baseStatLevel['subStat'][2][20] = 236 , 16.0
		self.baseStatLevel['mainStat'][2][30], self.baseStatLevel['subStat'][2][30] = 299 , 16.0
		self.baseStatLevel['mainStat'][3][30], self.baseStatLevel['subStat'][3][30] = 335 , 19.0
		self.baseStatLevel['mainStat'][3][40], self.baseStatLevel['subStat'][3][40] = 397 , 19.0
		self.baseStatLevel['mainStat'][4][40], self.baseStatLevel['subStat'][4][40] = 433 , 22.0
		self.baseStatLevel['mainStat'][4][50], self.baseStatLevel['subStat'][4][50] = 496 , 22.0
		self.baseStatLevel['mainStat'][5][50], self.baseStatLevel['subStat'][5][50] = 532 , 25.0
		self.baseStatLevel['mainStat'][5][60], self.baseStatLevel['subStat'][5][60] = 594 , 25.0


class StarlightEngine(WEngine):
	def __init__(self):
		super().__init__("Starlight Engine", "A", "Attack", Stat("atk"), Stat("atk_"))

		self.baseStatLevel['mainStat'][0][0], self.baseStatLevel['subStat'][0][0] = 40 , 10.0
		self.baseStatLevel['mainStat'][0][10], self.baseStatLevel['subStat'][0][10] = 102 , 10.0
		self.baseStatLevel['mainStat'][1][10], self.baseStatLevel['subStat'][1][10] = 138 , 13.0
		self.baseStatLevel['mainStat'][1][20], self.baseStatLevel['subStat'][1][20] = 201 , 13.0
		self.baseStatLevel['mainStat'][2][20], self.baseStatLevel['subStat'][2][20] = 236 , 16.0
		self.baseStatLevel['mainStat'][2][30], self.baseStatLevel['subStat'][2][30] = 299 , 16.0
		self.baseStatLevel['mainStat'][3][30], self.baseStatLevel['subStat'][3][30] = 335 , 19.0
		self.baseStatLevel['mainStat'][3][40], self.baseStatLevel['subStat'][3][40] = 397 , 19.0
		self.baseStatLevel['mainStat'][4][40], self.baseStatLevel['subStat'][4][40] = 433 , 22.0
		self.baseStatLevel['mainStat'][4][50], self.baseStatLevel['subStat'][4][50] = 496 , 22.0
		self.baseStatLevel['mainStat'][5][50], self.baseStatLevel['subStat'][5][50] = 532 , 25.0
		self.baseStatLevel['mainStat'][5][60], self.baseStatLevel['subStat'][5][60] = 594 , 25.0


class StarlightEngineReplica(WEngine):
	def __init__(self):
		super().__init__("Starlight Engine Replica", "A", "Attack", Stat("atk"), Stat("atk_"))

		self.baseStatLevel['mainStat'][0][0], self.baseStatLevel['subStat'][0][0] = 42 , 10.0
		self.baseStatLevel['mainStat'][0][10], self.baseStatLevel['subStat'][0][10] = 107 , 10.0
		self.baseStatLevel['mainStat'][1][10], self.baseStatLevel['subStat'][1][10] = 145 , 13.0
		self.baseStatLevel['mainStat'][1][20], self.baseStatLevel['subStat'][1][20] = 211 , 13.0
		self.baseStatLevel['mainStat'][2][20], self.baseStatLevel['subStat'][2][20] = 248 , 16.0
		self.baseStatLevel['mainStat'][2][30], self.baseStatLevel['subStat'][2][30] = 314 , 16.0
		self.baseStatLevel['mainStat'][3][30], self.baseStatLevel['subStat'][3][30] = 352 , 19.0
		self.baseStatLevel['mainStat'][3][40], self.baseStatLevel['subStat'][3][40] = 417 , 19.0
		self.baseStatLevel['mainStat'][4][40], self.baseStatLevel['subStat'][4][40] = 455 , 22.0
		self.baseStatLevel['mainStat'][4][50], self.baseStatLevel['subStat'][4][50] = 521 , 22.0
		self.baseStatLevel['mainStat'][5][50], self.baseStatLevel['subStat'][5][50] = 558 , 25.0
		self.baseStatLevel['mainStat'][5][60], self.baseStatLevel['subStat'][5][60] = 624 , 25.0


class SteamOven(WEngine):
	def __init__(self):
		super().__init__("Steam Oven", "A", "Stun", Stat("atk"), Stat("energyRegen_"))

		self.baseStatLevel['mainStat'][0][0], self.baseStatLevel['subStat'][0][0] = 40 , 20.0
		self.baseStatLevel['mainStat'][0][10], self.baseStatLevel['subStat'][0][10] = 102 , 20.0
		self.baseStatLevel['mainStat'][1][10], self.baseStatLevel['subStat'][1][10] = 138 , 26.0
		self.baseStatLevel['mainStat'][1][20], self.baseStatLevel['subStat'][1][20] = 201 , 26.0
		self.baseStatLevel['mainStat'][2][20], self.baseStatLevel['subStat'][2][20] = 236 , 32.0
		self.baseStatLevel['mainStat'][2][30], self.baseStatLevel['subStat'][2][30] = 299 , 32.0
		self.baseStatLevel['mainStat'][3][30], self.baseStatLevel['subStat'][3][30] = 335 , 38.0
		self.baseStatLevel['mainStat'][3][40], self.baseStatLevel['subStat'][3][40] = 397 , 38.0
		self.baseStatLevel['mainStat'][4][40], self.baseStatLevel['subStat'][4][40] = 433 , 44.0
		self.baseStatLevel['mainStat'][4][50], self.baseStatLevel['subStat'][4][50] = 496 , 44.0
		self.baseStatLevel['mainStat'][5][50], self.baseStatLevel['subStat'][5][50] = 532 , 50.0
		self.baseStatLevel['mainStat'][5][60], self.baseStatLevel['subStat'][5][60] = 594 , 50.0


class StreetSuperstar(WEngine):
	def __init__(self):
		super().__init__("Street Superstar", "A", "Attack", Stat("atk"), Stat("atk_"))

		self.baseStatLevel['mainStat'][0][0], self.baseStatLevel['subStat'][0][0] = 40 , 10.0
		self.baseStatLevel['mainStat'][0][10], self.baseStatLevel['subStat'][0][10] = 102 , 10.0
		self.baseStatLevel['mainStat'][1][10], self.baseStatLevel['subStat'][1][10] = 138 , 13.0
		self.baseStatLevel['mainStat'][1][20], self.baseStatLevel['subStat'][1][20] = 201 , 13.0
		self.baseStatLevel['mainStat'][2][20], self.baseStatLevel['subStat'][2][20] = 236 , 16.0
		self.baseStatLevel['mainStat'][2][30], self.baseStatLevel['subStat'][2][30] = 299 , 16.0
		self.baseStatLevel['mainStat'][3][30], self.baseStatLevel['subStat'][3][30] = 335 , 19.0
		self.baseStatLevel['mainStat'][3][40], self.baseStatLevel['subStat'][3][40] = 397 , 19.0
		self.baseStatLevel['mainStat'][4][40], self.baseStatLevel['subStat'][4][40] = 433 , 22.0
		self.baseStatLevel['mainStat'][4][50], self.baseStatLevel['subStat'][4][50] = 496 , 22.0
		self.baseStatLevel['mainStat'][5][50], self.baseStatLevel['subStat'][5][50] = 532 , 25.0
		self.baseStatLevel['mainStat'][5][60], self.baseStatLevel['subStat'][5][60] = 594 , 25.0


class TheVault(WEngine):
	def __init__(self):
		super().__init__("The Vault", "A", "Support", Stat("atk"), Stat("energyRegen_"))

		self.baseStatLevel['mainStat'][0][0], self.baseStatLevel['subStat'][0][0] = 42 , 20.0
		self.baseStatLevel['mainStat'][0][10], self.baseStatLevel['subStat'][0][10] = 107 , 20.0
		self.baseStatLevel['mainStat'][1][10], self.baseStatLevel['subStat'][1][10] = 145 , 26.0
		self.baseStatLevel['mainStat'][1][20], self.baseStatLevel['subStat'][1][20] = 211 , 26.0
		self.baseStatLevel['mainStat'][2][20], self.baseStatLevel['subStat'][2][20] = 248 , 32.0
		self.baseStatLevel['mainStat'][2][30], self.baseStatLevel['subStat'][2][30] = 314 , 32.0
		self.baseStatLevel['mainStat'][3][30], self.baseStatLevel['subStat'][3][30] = 352 , 38.0
		self.baseStatLevel['mainStat'][3][40], self.baseStatLevel['subStat'][3][40] = 417 , 38.0
		self.baseStatLevel['mainStat'][4][40], self.baseStatLevel['subStat'][4][40] = 455 , 44.0
		self.baseStatLevel['mainStat'][4][50], self.baseStatLevel['subStat'][4][50] = 521 , 44.0
		self.baseStatLevel['mainStat'][5][50], self.baseStatLevel['subStat'][5][50] = 558 , 50.0
		self.baseStatLevel['mainStat'][5][60], self.baseStatLevel['subStat'][5][60] = 624 , 50.0


class UnfetteredGameBall(WEngine):
	def __init__(self):
		super().__init__("Unfettered Game Ball", "A", "Support", Stat("atk"), Stat("energyRegen_"))

		self.baseStatLevel['mainStat'][0][0], self.baseStatLevel['subStat'][0][0] = 40 , 20.0
		self.baseStatLevel['mainStat'][0][10], self.baseStatLevel['subStat'][0][10] = 102 , 20.0
		self.baseStatLevel['mainStat'][1][10], self.baseStatLevel['subStat'][1][10] = 138 , 26.0
		self.baseStatLevel['mainStat'][1][20], self.baseStatLevel['subStat'][1][20] = 201 , 26.0
		self.baseStatLevel['mainStat'][2][20], self.baseStatLevel['subStat'][2][20] = 236 , 32.0
		self.baseStatLevel['mainStat'][2][30], self.baseStatLevel['subStat'][2][30] = 299 , 32.0
		self.baseStatLevel['mainStat'][3][30], self.baseStatLevel['subStat'][3][30] = 335 , 38.0
		self.baseStatLevel['mainStat'][3][40], self.baseStatLevel['subStat'][3][40] = 397 , 38.0
		self.baseStatLevel['mainStat'][4][40], self.baseStatLevel['subStat'][4][40] = 433 , 44.0
		self.baseStatLevel['mainStat'][4][50], self.baseStatLevel['subStat'][4][50] = 496 , 44.0
		self.baseStatLevel['mainStat'][5][50], self.baseStatLevel['subStat'][5][50] = 532 , 50.0
		self.baseStatLevel['mainStat'][5][60], self.baseStatLevel['subStat'][5][60] = 594 , 50.0


class WeepingGemini(WEngine):
	def __init__(self):
		super().__init__("Weeping Gemini", "A", "Anomaly", Stat("atk"), Stat("atk_"))

		self.baseStatLevel['mainStat'][0][0], self.baseStatLevel['subStat'][0][0] = 40 , 10.0
		self.baseStatLevel['mainStat'][0][10], self.baseStatLevel['subStat'][0][10] = 102 , 10.0
		self.baseStatLevel['mainStat'][1][10], self.baseStatLevel['subStat'][1][10] = 138 , 13.0
		self.baseStatLevel['mainStat'][1][20], self.baseStatLevel['subStat'][1][20] = 201 , 13.0
		self.baseStatLevel['mainStat'][2][20], self.baseStatLevel['subStat'][2][20] = 236 , 16.0
		self.baseStatLevel['mainStat'][2][30], self.baseStatLevel['subStat'][2][30] = 299 , 16.0
		self.baseStatLevel['mainStat'][3][30], self.baseStatLevel['subStat'][3][30] = 335 , 19.0
		self.baseStatLevel['mainStat'][3][40], self.baseStatLevel['subStat'][3][40] = 397 , 19.0
		self.baseStatLevel['mainStat'][4][40], self.baseStatLevel['subStat'][4][40] = 433 , 22.0
		self.baseStatLevel['mainStat'][4][50], self.baseStatLevel['subStat'][4][50] = 496 , 22.0
		self.baseStatLevel['mainStat'][5][50], self.baseStatLevel['subStat'][5][50] = 532 , 25.0
		self.baseStatLevel['mainStat'][5][60], self.baseStatLevel['subStat'][5][60] = 594 , 25.0


class IdentityBase(WEngine):
	def __init__(self):
		super().__init__("Identity] Base", "B", "Defense", Stat("atk"), Stat("def_"))

class IdentityInflection(WEngine):
	def __init__(self):
		super().__init__("[Identity] Inflection", "B", "Defense", Stat("atk"), Stat("def_"))

class LunarDecrescent(WEngine):
	def __init__(self):
		super().__init__("[Lunar] Decrescent", "B", "Attack", Stat("atk"), Stat("atk_"))

class LunarNoviluna(WEngine):
	def __init__(self):
		super().__init__("[Lunar] Noviluna", "B", "Attack", Stat("atk"), Stat("criteRate_"))

class LunarPleniluna(WEngine):
	def __init__(self):
		super().__init__("[Lunar] Pleniluna", "B", "Attack", Stat("atk"), Stat("atk_"))

class MagneticStormAlpha(WEngine):
	def __init__(self):
		super().__init__("[Magnetic Storm] Alpha", "B", "Anomaly", Stat("atk"), Stat("atk_"))

class MagneticStormBravo(WEngine):
	def __init__(self):
		super().__init__("[Magnetic Storm] Bravo", "B", "Anomaly", Stat("atk"), Stat("anomalyProficiency"))

class MagneticStormCharlie(WEngine):
	def __init__(self):
		super().__init__("[Magnetic Storm] Charlie", "B", "Anomaly", Stat("atk"), Stat("pen_"))

class ReverbMarkI(WEngine):
	def __init__(self):
		super().__init__("[Reverb] Mark I", "B", "Support", Stat("atk"), Stat("atk_"))

class ReverbMarkII(WEngine):
	def __init__(self):
		super().__init__("[Reverb] Mark II", "B", "Support", Stat("atk"), Stat("energyRegen_"))

class ReverbMarkIII(WEngine):
	def __init__(self):
		super().__init__("[Reverb] Mark III", "B", "Support", Stat("atk"), Stat("hp_"))

class VortexArrow(WEngine):
	def __init__(self):
		super().__init__("[Vortex] Arrow", "B", "Stun", Stat("atk"), Stat("impact_"))

class VortexHatchet(WEngine):
	def __init__(self):
		super().__init__("[Vortex] Hatchet", "B", "Stun", Stat("atk"), Stat("energyRegen_"))

class VortexRevolver(WEngine):
	def __init__(self):
		super().__init__("[Vortex] Revolver", "B", "Stun", Stat("atk"), Stat("atk_"))


wengineObjects: dict[str, WEngine] = {
	"Deep Sea Visitor": DeepSeaVisitor(),
	"Fusion Compiler": FusionCompiler(),
	"Hellfire Gears": HellfireGears(),
	"Riot Suppressor Mark VI": RiotSuppressorMarkVI(),
	"Steel Cushion": SteelCushion(),
	"The Brimstone": TheBrimstone(),
	"The Restrained": TheRestrained(),
	"Weeping Cradle": WeepingCradle(),
	"Bashful Demon": BashfulDemon(),
	"Big Cylinder": BigCylinder(),
	"Bunny Band": BunnyBand(),
	"Cannon Rotor": CannonRotor(),
	"Demara Battery Mark II": DemaraBatteryMarkII(),
	"Drill Rig - Red Axis": DrillRigRedAxis(),
	"Electro-Lip Gloss": ElectroLipGloss(),
	"Housekeeper": Housekeeper(),
	"Kaboom the Cannon": KaboomtheCannon(),
	"Original Transmorpher": OriginalTransmorpher(),
	"Precious Fossilized Core": PreciousFossilizedCore(),
	"Rainforest Gourmet": RainforestGourmet(),
	"Roaring Ride": RoaringRide(),
	"Six Shooter": SixShooter(),
	"Slice of Time": SliceofTime(),
	"Spring Embrace": SpringEmbrace(),
	"Starlight Engine": StarlightEngine(),
	"Starlight Engine Replica": StarlightEngineReplica(),
	"Steam Oven": SteamOven(),
	"Street Superstar": StreetSuperstar(),
	"The Vault": TheVault(),
	"Unfettered Game Ball": UnfetteredGameBall(),
	"Weeping Gemini": WeepingGemini(),
}


def load_wengine():
	wengines: list[WEngineModel] = []

	for wengine in wengineObjects.values():
		wengines.append(WEngineModel(
			name = wengine.name,
			rank = wengine.rank,
			mainStat= wengine.mainStat.key,
			subStat=wengine.subStat.key,
			nameIcon=f'{BASE_DIR}/{MEDIA_DIR}/wengines/{wengine.name.replace(" ", "_")}.png',
			rankIcon = f'{BASE_DIR}/{MEDIA_DIR}/rank/{wengine.rank}.png',
		))


	return wengines