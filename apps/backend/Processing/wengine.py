from .stat import Stat
import config


from typing import Literal


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
	passiveStats: list

	def __init__(self, name: str, rank: str, specialty: str, mainStat: str, subStat: str):
		self.modificationLevel = 0
		self.levl = 0
		self.upgradeLevel = 1

		self.baseStatLevel = {
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
		self.name = name
		self.rank = rank
		
		self.specialty = specialty

		self.mainStat = mainStat
		self.subStat = subStat

		self.passiveDescription = ""
		self.passiveStats = []


	def fromJson(self, data: dict):
		pass

	def loadBaseStat(self, data):
		self.baseStatLevel = data

	def setLevel(self, value):
		self.level = value

	def getStat(self, promotion: Literal[0,1,2,3,4,5] = 0, level: int = 0):
		levelmin = promotion*10
		levelmax = levelmin+10
		mainStatmin = self.baseStatLevel['mainStat'][promotion][levelmin]
		mainStatmax = self.baseStatLevel['mainStat'][promotion][levelmax]

		subStatmin = self.baseStatLevel['subStat'][promotion][levelmin]
		subStatmax = self.baseStatLevel['subStat'][promotion][levelmax]

		mainStat = (mainStatmax-mainStatmin)*(level-levelmin) / 10 + mainStatmin
		subStat = (subStatmax-subStatmin)*(level-levelmin) / 10 + subStatmin

		return {"mainStat": [self.mainStat, mainStat], "subStat": [self.subStat, subStat]}

	def getPassive(self, upgrade: Literal[1,2,3,4,5] = 1):
		passive = self.passiveDescription.format(*[passiveStat[upgrade-1] for passiveStat in self.passiveStats])

		return {"passive": passive}
		


class DeepSeaVisitor(WEngine):
	def __init__(self):
		super().__init__("Deep Sea Visitor", "S", "Attack", "atk", "critRate_")

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

		self.passiveStats = [[25, 31.5, 38, 44.5, 50], [10, 12.5, 15, 17.5, 20], [10, 12.5, 15, 17.5, 20]]

		self.passiveDescription = "<p>Increases <span style=\"color: rgb(140,216,218)\">Ice DMG</span> by <span style=\"color: rgb(237,197,84)\">{0}%</span>. Upon hitting an enemy with a Basic Attack, the equipper's CRIT Rate increases by <span style=\"color: rgb(237,197,84)\">{1}%</span> for 8s. When dealing <span style=\"color: rgb(140,216,218)\">Ice DMG</span> with a Dash Attack, the equipper's CRIT Rate increases by an additional <span style=\"color: rgb(237,197,84)\">{2}%</span> for 15s. The duration of each effect is calculated separately.</p>"
		

class FusionCompiler(WEngine):
	def __init__(self):
		super().__init__("Fusion Compiler", "S", "Anomaly", "atk", "pen_")
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

		self.passiveStats = [[12, 15, 18, 21, 24], [25, 31, 37, 43, 50]]

		self.passiveDescription = "<p>Increases ATK by <span style=\"color: rgb(237,197,84)\">{0}%</span>. When using a Special Attack or EX Special Attack, the equipper's Anomaly Proficiency is increased by <span style=\"color: rgb(237,197,84)\">{1}</span> for 8, stacking up to 3 times. The duration of each stack is calculated separately.</p>"

class HellfireGears(WEngine):
	def __init__(self):
		super().__init__("Hellfire Gears", "S", "Stun", "atk", "impact_")
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

		self.passiveStats = [[0.6, 0.75, 0.9, 1.5, 1.2], [10, 12.5, 15, 17.5, 20]]


		self.passiveDescription = "<p>When off-field, the equipper's Energy Regen increases by <span style=\"color: rgb(237,197,84)\">{0}</span> per second. When using an EX Special Attack, the equipper's Impact is increased by <span style=\"color: rgb(237,197,84)\">{1}</span> for 10s, stacking up to 2 times. The duration of each stack is calculated separately.</p>"

class IceJadeTeapot(WEngine):
	def __init__(self):
		super().__init__("Ice-Jade Teapot", "S", "Stun", "atk", "impact_")

		self.baseStatLevel['mainStat'][0][0], self.baseStatLevel['subStat'][0][0] = 48 , 7.2
		self.baseStatLevel['mainStat'][0][10], self.baseStatLevel['subStat'][0][10] = 123 , 7.2
		self.baseStatLevel['mainStat'][1][10], self.baseStatLevel['subStat'][1][10] = 166 , 9.4
		self.baseStatLevel['mainStat'][1][20], self.baseStatLevel['subStat'][1][20] = 241 , 9.4
		self.baseStatLevel['mainStat'][2][20], self.baseStatLevel['subStat'][2][20] = 284 , 11.5
		self.baseStatLevel['mainStat'][2][30], self.baseStatLevel['subStat'][2][30] = 359 , 11.5
		self.baseStatLevel['mainStat'][3][30], self.baseStatLevel['subStat'][3][30] = 402 , 13.7
		self.baseStatLevel['mainStat'][3][40], self.baseStatLevel['subStat'][3][40] = 477 , 13.7
		self.baseStatLevel['mainStat'][4][40], self.baseStatLevel['subStat'][4][40] = 520 , 15.8
		self.baseStatLevel['mainStat'][4][50], self.baseStatLevel['subStat'][4][50] = 595 , 15.8
		self.baseStatLevel['mainStat'][5][50], self.baseStatLevel['subStat'][5][50] = 638 , 18.0
		self.baseStatLevel['mainStat'][5][60], self.baseStatLevel['subStat'][5][60] = 713 , 18.0

		self.passiveStats = [[0.7, 0.88, 1.05, 1.22, 1.4], [20, 23, 26, 29, 32]]
		self.passiveDescription = "<p>When a Basic Attack hits an enemy, gain 1 stack of Tea-riffic. Each stack of Tea-riffic increases the user's Impact by <span style=\"color: rgb(237,197,84)\">{0}%</span>, stacking up to 30 times, and lasting for 8s. The duration of each stack is calculated separately. Upon acquiring Tea-riffic, if the equipper possesses stacks of Tea-riffic greater than or equal to 15, all squad members' DMG is increased by <span style=\"color: rgb(237,197,84)\">{1}%</span> for 10s. Passive effects of the same name do not stack.</p>"


class RiotSuppressorMarkVI(WEngine):
	def __init__(self):
		super().__init__("Riot Suppressor Mark VI", "S", "Attack", "atk", "critDMG_")
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

		self.passiveStats = [[15, 18.8, 22.6, 26.4, 30], [35, 43.5, 52, 60.5, 70]]


		self.passiveDescription = "<p>Increases CRIT Rate by <span style=\"color: rgb(237,197,84)\">{0}</span>. Launching an EX Special Attack grants the equipper 8 Charge stacks, up to a maximum of 8 stacks. Whenever the equipper's Basic Attack deals Ether DMG, consumes a Charge stack and increases the skill's DMG by <span style=\"color: rgb(237,197,84)\">{1}</span>.</p>"

class SteelCushion(WEngine):
	def __init__(self):
		super().__init__("Steel Cushion", "S", "Attack", "atk", "critRate_")
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

		self.passiveStats = [[20, 25, 30, 35, 40], [25, 31.5, 38, 44, 50]]

		self.passiveDescription = "<p>Increases <span style=\"color: rgb(192,168,47)\">Physical DMG</span> by <span style=\"color: rgb(237,197,84)\">{0}%s</span>. The equipper's DMG increases by <span style=\"color: rgb(237,197,84)\">{1}</span> when attacking the enemy from behind.</p>"


class TheBrimstone(WEngine):
	def __init__(self):
		super().__init__("The Brimstone", "S", "Attack", "atk", "atk_")
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

		self.passiveStats = [[3.5, 4.4, 5.2, 6, 7]]

		self.passiveDescription = "<p>Upon hitting an enemy with a Basic Attack, Dash Attack, or Dodge Counter, the equipper's ATK increases by <span style=\"color: rgb(237,197,84)\">{0}%</span> for 8s, stacking up to 8 times. This effect can trigger once every 0.5s. The duration of each stack is calculated separately.</p>"


class TheRestrained(WEngine):
	def __init__(self):
		super().__init__("The Restrained", "S", "Stun", "atk", "impact_")
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

		self.passiveStats = [[6, 7.5, 9, 10.5, 12]]

		self.passiveDescription = "<p>When an attack hits an enemy, DMG and Daze from Basic Attacks increase by <span style=\"color: rgb(237,197,84)\">{0}%</span> for 8s, stacking up to 5 times. This effect can trigger at most once during each skill. The duration of each stack is calculated separately.</p>"


class WeepingCradle(WEngine):
	def __init__(self):
		super().__init__("Weeping Cradle", "S", "Support", "atk", "pen_")
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

		self.passiveStats = [[0.6, 0.75, 0.9, 1.05, 1.2], [10, 12.5, 15, 17.5, 20], [1.7, 2, 2.5, 3, 3.3], [10.2, 12, 15, 18, 19.8]]


		self.passiveDescription = "<p>While off-field, Energy Regen increases by <span style=\"color: rgb(237,197,84)\">{0}</span> per second. Attacks from the equipper enhance the squad's DMG against a struck target by <span style=\"color: rgb(237,197,84)\">{1}%</span> for 3 seconds. During this period, this effect is further increased by <span style=\"color: rgb(237,197,84)\">{2}%</span> every 0.5s, up to a maximum additional increase of <span style=\"color: rgb(237,197,84)\">{3}</span>. Repeated triggers only refresh its duration without refreshing the DMG increase effect. Passive effects of the same name do not stack.</p>"


class BashfulDemon(WEngine):
	def __init__(self):
		super().__init__("Bashful Demon", "A", "Support", "atk", "atk_")

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

		self.passiveStats = [[15, 17.5, 20, 22, 24], [2, 2.3, 2.6, 2.9, 3.2]]

		self.passiveDescription = "<p>Increases <span style=\"color: rgb(140,216,218)\">Ice DMG</span> by <span style=\"color: rgb(237,197,84)\">{0}</span>. When launching an EX Special Attack, all squad members' ATK increases by <span style=\"color: rgb(237,197,84)\">{1}%</span> for 12s, stacking up to 4 times. Retriggering refreshes duration. Passive effects of the same name do not stack.</p>"


class BigCylinder(WEngine):
	def __init__(self):
		super().__init__("Big Cylinder", "A", "Defense", "atk", "def_")
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

		self.passiveStats = [[7.5, 8.5, 9.5, 10.5, 12], [600, 690, 780, 870, 960]]

		self.passiveDescription = "<p>Reduces DMG taken by <span style=\"color: rgb(237,197,84)\">{0}</span>. After being attacked, the next attack to hit an enemy will trigger a critical hit and deal <span style=\"color: rgb(237,197,84)\">{1}%</span> of the equipper's DEF as additional DMG. This effect can be triggered once every 7.5s.</p>"



class BunnyBand(WEngine):
	def __init__(self):
		super().__init__("Bunny Band", "A", "Defense", "atk", "def_")
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

		self.passiveStats = [[8, 9.2, 10.4, 11.6, 12.8], [10, 11.5, 13, 14.5, 16]]

		self.passiveDescription = "<p>Increases Max HP by <span style=\"color: rgb(237,197,84)\">{0}</span>. Increases the equipper's ATK by <span style=\"color: rgb(237,197,84)\">{1}%</span> when they are shielded.</p>"

class CannonRotor(WEngine):
	def __init__(self):
		super().__init__("Cannon Rotor", "A", "Attack", "atk", "critRate_")
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

		self.passiveStats = [[7.5, 8.6, 9.7, 10.8, 12], [8, 7.5, 7, 6.5, 6]]

		self.passiveDescription = "<p>Increases ATK by <span style=\"color: rgb(237,197,84)\">{0}</span>. Attacks that land a CRIT on an enemy will inflict an additional 200% of ATK as DMG. This effect can only be triggered once every <span style=\"color: rgb(237,197,84)\">{1}s</span>.</p>"

class DemaraBatteryMarkII(WEngine):
	def __init__(self):
		super().__init__("Demara Battery Mark II", "A", "Stun", "atk", "impact_")

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

		self.passiveStats = [[15, 17.5, 20, 22, 22], [18, 20.5, 23, 25, 27.5]]

		self.passiveDescription = "<p>Increases <span style=\"color: rgb(46,182,255)\">Electric DMG</span> by <span style=\"color: rgb(237,197,84)\">{0}</span>. When the equipper hits an enemy with Dodge Counter or Assist Attack, their Energy Generation Rate increases by <span style=\"color: rgb(237,197,84)\">{1}%</span> for 8s.</p>"

class DrillRigRedAxis(WEngine):
	def __init__(self):
		super().__init__("Drill Rig - Red Axis", "A", "Attack", "atk", "energyRegen_")

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

		self.passiveStats = [[50, 57.5, 65, 72.5, 80]]

		self.passiveDescription = "<p>When launching an EX Special Attack or Chain Attack, <span style=\"color: rgb(46,182,255)\">Electric DMG</span> from Basic Attacks and Dash Attacks increases by <span style=\"color: rgb(237,197,84)\">{0}%</span> for 10s. This effect can trigger once every 15s.</p>"


class ElectroLipGloss(WEngine):
	def __init__(self):
		super().__init__("Electro-Lip Gloss", "A", "Anomaly", "atk", "anomalyProficiency")

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

		self.passiveStats = [[10, 11.5, 13, 14.5, 16], [15, 17.5, 20, 22.5, 25]]
		self.passiveDescription = "<p>When there are enemies inflicted with Attribute Anomaly on the field, the equipper's ATK increases by <span style=\"color: rgb(237,197,84)\">{0}%</span> and they deal an additional <span style=\"color: rgb(237,197,84)\">{1}%</span> more DMG to the target.</p>"



class Housekeeper(WEngine):
	def __init__(self):
		super().__init__("Housekeeper", "A", "Attack", "atk", "atk_")
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

		self.passiveStats = [[0.45, 0.52, 0.58, 0.65, 0.72], [3, 3.5, 4, 4.4, 4.8]]
		self.passiveDescription = "<p>While off-field, Energy Regen increases by <span style=\"color: rgb(237,197,84)\">{0}</span> per second. When an EX Special Attack hits an enemy, the equipper's <span style=\"color: rgb(192,168,47)\">Physical DMG</span> increases by <span style=\"color: rgb(237,197,84)\">{1}%</span>, stacking up to 15 times and lasting 1s. Retriggering refreshes duration.</p>"



class KaboomtheCannon(WEngine):
	def __init__(self):
		super().__init__("Kaboom the Cannon", "A", "Support", "atk", "energyRegen_")
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

		self.passiveStats = [[2.5, 2.8, 3.2, 3.6, 4]]
		self.passiveDescription = "<p>When any friendly unit in the squad attacks and hits an enemy, all friendly units' ATK increases by <span style=\"color: rgb(237,197,84)\">{0}%</span> for 8s, stacking up to 4 times. The duration of each stack is calculated separately, and each friendly unit can provide 1 stack of the buff. Passive effects of the same name do not stack.</p>"



class OriginalTransmorpher(WEngine):
	def __init__(self):
		super().__init__("Original Transmorpher", "A", "Defense", "atk", "hp_")

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

		self.passiveStats = [[8, 9, 10, 11, 12.5], [10, 11.5, 13, 14.5, 16]]
		self.passiveDescription = "<p>Increases Max HP by <span style=\"color: rgb(237,197,84)\">{0}</span>. When attacked, the equipper's Impact is increased by <span style=\"color: rgb(237,197,84)\">{1}%</span> for 12s.</p>"




class PreciousFossilizedCore(WEngine):
	def __init__(self):
		super().__init__("Precious Fossilized Core", "A", "Stun", "atk", "impact_")
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

		self.passiveStats = [[10, 11.5, 13, 14.5, 16], [10, 11.5, 13, 14.5, 16]]
		self.passiveDescription = "<p>When the target's HP is no lower than 50%, the equipper inflicts <span style=\"color: rgb(237,197,84)\">{0}%</span> more Daze. When the target's HP is no lower than 75%, this bonus is further enhanced by <span style=\"color: rgb(237,197,84)\">{1}%</span>.</p>"




class RainforestGourmet(WEngine):
	def __init__(self):
		super().__init__("Rainforest Gourmet", "A", "Anomaly", "atk", "anomalyProficiency")

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

		self.passiveStats = [[2.5, 2.8, 3.2, 3.6, 4]]
		self.passiveDescription = "<p>For every 10 Energy consumed, the equipper gains a buff that increases ATK by <span style=\"color: rgb(237,197,84)\">{0}%</span> for 10s, stacking up to 10 times. The duration of each stack is calculated separately.</p>"



class RoaringRide(WEngine):
	def __init__(self):
		super().__init__("Roaring Ride", "A", "Anomaly", "atk", "atk_")

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

		self.passiveStats = [[8, 9.2, 10.4, 11.6, 12.8], [40, 46, 52, 58, 64], [25, 28, 32, 36, 40]]

		self.passiveDescription = "<p>When EX Special Attack hits an enemy, one of three possible effects is randomly triggered for 5 seconds. This effect can trigger once every 0.3s. The same types of effects cannot stack. Repeated triggers reset the duration allowing several effects to be active at once:<ul><li>increases the equipper's ATK by <span style=\"color: rgb(237,197,84)\">{0}%</span>.</li> <li> increases the equipper's Anomaly Proficiency by <span style=\"color: rgb(237,197,84)\">{1}</span>.</li> <li>increases the equipper's Anomaly Buildup Rate by <span style=\"color: rgb(237,197,84)\">{2}%</span>.</li></ul></p>"

class SixShooter(WEngine):
	def __init__(self):
		super().__init__("Six Shooter", "A", "Stun", "atk", "impact_")

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

		self.passiveStats = [[4, 4.6, 5.2, 5.8, 6.4]]
		self.passiveDescription = "<p>The equipper gains a Charge stack every 3s, stacking up to 6 times. When launching an EX Special Attack, consumes all Charge stacks, and each stack increases the Daze inflicted by <span style=\"color: rgb(237,197,84)\">{0}%</span> </p>"



class SliceofTime(WEngine):
	def __init__(self):
		super().__init__("Slice of Time", "A", "Support", "atk", "pen_")

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

		self.passiveStats = [[20, 23, 26, 29, 32], [25, 28.5, 32, 35.5, 40], [30, 34.5, 39, 43.5, 48], [35, 40, 45, 50, 55], [0.7, 0.8, 0.9, 1, 1.1]]
		self.passiveDescription = "<p>Any squad members' Dodge Counter, EX Special Attack, Assist Attack, or Chain Attack respectively generates <span style=\"color: rgb(237,197,84)\">{0}</span> (Dodge) | <span style=\"color: rgb(237,197,84)\">{1}</span> (Special) | <span style=\"color: rgb(237,197,84)\">{2}</span> (Assist) | <span style=\"color: rgb(237,197,84)\">{3}</span> (Chain) more Decibels and generates <span style=\"color: rgb(237,197,84)\">{4}</span> Energy for the equipper. This effect can trigger once every 12s. The cooldown for each type of attack is independent of others. Passive effects of the same name do not stack.</p>"




class SpringEmbrace(WEngine):
	def __init__(self):
		super().__init__("Spring Embrace", "A", "Defense", "atk", "atk_")

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

		self.passiveStats = [[7.5, 8.5, 9.5, 10.5, 12], [10, 11.5, 13, 14.5, 16]]
		self.passiveDescription = "<p>Reduces DMG taken <span style=\"color: rgb(237,197,84)\">{0}</span>. When attacked, the equipper's Energy Generation Rate increased by <span style=\"color: rgb(237,197,84)\">{1}%</span> for 12s. When the equipper switches off-field, this buff will be transferred to the new on-field character with its duration refreshed. Passive effects of the same name do not stack.</p>"



class StarlightEngine(WEngine):
	def __init__(self):
		super().__init__("Starlight Engine", "A", "Attack", "atk", "atk_")

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

		self.passiveStats = [[12, 13.8, 15.6, 17.4, 19.2]]
		self.passiveDescription = "<p>Launching a Dodge Counter or Quick Assist increases the equipper's ATK by <span style=\"color: rgb(237,197,84)\">{0}%</span> for 12s.</p>"



class StarlightEngineReplica(WEngine):
	def __init__(self):
		super().__init__("Starlight Engine Replica", "A", "Attack", "atk", "atk_")

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

		self.passiveStats = [[36, 41, 46.5, 52, 57.5]]
		self.passiveDescription = "<p>Increases the equipper's <span style=\"color: rgb(192,168,47)\">Physical DMG</span> by <span style=\"color: rgb(237,197,84)\">{0}%</span> for 8s upon hitting an enemy at least 6 meters away with a Basic Attack or Dash Attack.</p>"



class SteamOven(WEngine):
	def __init__(self):
		super().__init__("Steam Oven", "A", "Stun", "atk", "energyRegen_")

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

		self.passiveStats = [[2, 2.3, 2.6, 2.9, 3.2]]
		self.passiveDescription = "<p>For every 10 Energy accumulated, the equipper's Impact is increased by <span style=\"color: rgb(237,197,84)\">{0}%</span>  stacking up to 8 times. After Energy is consumed, this bonus remains for 8 more seconds. The duration of each stack is calculated separately.</p>"



class StreetSuperstar(WEngine):
	def __init__(self):
		super().__init__("Street Superstar", "A", "Attack", "atk", "atk_")

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


		self.passiveStats = [[15, 17.2, 19.5, 21.7, 24]]
		self.passiveDescription = "<p>Whenever a squad member launches a Chain Attack, the equipper gains a Charge stack, stacking up to 3 times. Upon activating their own Ultimate, the equipper consumes all Charge stacks, and each stack increases the skill's DMG by <span style=\"color: rgb(237,197,84)\">{0}%</span>.</p>"



class TheVault(WEngine):
	def __init__(self):
		super().__init__("The Vault", "A", "Support", "atk", "energyRegen_")

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

		self.passiveStats = [[15, 17.5, 20, 22, 24], [0.5, 0.58, 0.65, 0.72, 0.8]]
		self.passiveDescription = "<p>Dealing <span style=\"color: rgb(248,66,123)\">Electric DMG</span> using an EX Special Attack, Chain Attack, or Ultimate increases all squad members' DMG against the target by <span style=\"color: rgb(237,197,84)\">{0}%</span> and increases the equipper's Energy Regen by <span style=\"color: rgb(237,197,84)\">{1}</span> per second for 2s. Passive effects of the same name do not stack.</p>"



class UnfetteredGameBall(WEngine):
	def __init__(self):
		super().__init__("Unfettered Game Ball", "A", "Support", "atk", "energyRegen_")

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

		self.passiveStats = [[12, 13.5, 15.5, 17.5, 20]]
		self.passiveDescription = "<p>Whenever the equipper's attack triggers an Attribute Counter effect, all squad members' CRIT Rate against the struck enemy increases by <span style=\"color: rgb(237,197,84)\">{0}%</span> for 12s. The bonuses triggered by the same type of passive effects do not stack.</p>"


class WeepingGemini(WEngine):
	def __init__(self):
		super().__init__("Weeping Gemini", "A", "Anomaly", "atk", "atk_")

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

		self.passiveStats = [[30, 34, 38, 42, 46]]
		self.passiveDescription = "<p>Whenever a squad member inflicts an Attribute Anomaly on an enemy, the equipper gains a buff that increases Anomaly Proficiency by <span style=\"color: rgb(237,197,84)\">{0}</span>, stacking up to 4 times. This effect expires when the target recovers from Stun or is defeated. The duration of each stack is calculated separately.</p>"


class IdentityBase(WEngine):
	def __init__(self):
		super().__init__("[Identity] Base", "B", "Defense", "atk", "def_")

		self.baseStatLevel['mainStat'][0][0], self.baseStatLevel['subStat'][0][0] = 32 , 12.8
		self.baseStatLevel['mainStat'][0][10], self.baseStatLevel['subStat'][0][10] = 82 , 12.8
		self.baseStatLevel['mainStat'][1][10], self.baseStatLevel['subStat'][1][10] = 110 , 16.6
		self.baseStatLevel['mainStat'][1][20], self.baseStatLevel['subStat'][1][20] = 160 , 16.6
		self.baseStatLevel['mainStat'][2][20], self.baseStatLevel['subStat'][2][20] = 189 , 20.5
		self.baseStatLevel['mainStat'][2][30], self.baseStatLevel['subStat'][2][30] = 239 , 20.5
		self.baseStatLevel['mainStat'][3][30], self.baseStatLevel['subStat'][3][30] = 268 , 24.3
		self.baseStatLevel['mainStat'][3][40], self.baseStatLevel['subStat'][3][40] = 318 , 24.3
		self.baseStatLevel['mainStat'][4][40], self.baseStatLevel['subStat'][4][40] = 346 , 28.2
		self.baseStatLevel['mainStat'][4][50], self.baseStatLevel['subStat'][4][50] = 397 , 28.2
		self.baseStatLevel['mainStat'][5][50], self.baseStatLevel['subStat'][5][50] = 425 , 32.0
		self.baseStatLevel['mainStat'][5][60], self.baseStatLevel['subStat'][5][60] = 475 , 32.0

		self.passiveStats = [[20, 23, 26, 29, 32]]
		self.passiveDescription = "<p>When attacked, the equipper's DEF increases by <span style=\"color: rgb(237,197,84)\">{0}%</span> for 8s.</p>"


class IdentityInflection(WEngine):
	def __init__(self):
		super().__init__("[Identity] Inflection", "B", "Defense", "atk", "def_")

		self.baseStatLevel['mainStat'][0][0], self.baseStatLevel['subStat'][0][0] = 32 , 12.8
		self.baseStatLevel['mainStat'][0][10], self.baseStatLevel['subStat'][0][10] = 82 , 12.8
		self.baseStatLevel['mainStat'][1][10], self.baseStatLevel['subStat'][1][10] = 110 , 16.6
		self.baseStatLevel['mainStat'][1][20], self.baseStatLevel['subStat'][1][20] = 160 , 16.6
		self.baseStatLevel['mainStat'][2][20], self.baseStatLevel['subStat'][2][20] = 189 , 20.5
		self.baseStatLevel['mainStat'][2][30], self.baseStatLevel['subStat'][2][30] = 239 , 20.5
		self.baseStatLevel['mainStat'][3][30], self.baseStatLevel['subStat'][3][30] = 268 , 24.3
		self.baseStatLevel['mainStat'][3][40], self.baseStatLevel['subStat'][3][40] = 318 , 24.3
		self.baseStatLevel['mainStat'][4][40], self.baseStatLevel['subStat'][4][40] = 346 , 28.2
		self.baseStatLevel['mainStat'][4][50], self.baseStatLevel['subStat'][4][50] = 397 , 28.2
		self.baseStatLevel['mainStat'][5][50], self.baseStatLevel['subStat'][5][50] = 425 , 32.0
		self.baseStatLevel['mainStat'][5][60], self.baseStatLevel['subStat'][5][60] = 475 , 32.0

		self.passiveStats = [[6, 7, 8, 9, 10]]
		self.passiveDescription = "<p>When attacked, reduces the attacker's DMG by <span style=\"color: rgb(237,197,84)\">{0}%</span> for 12s.</p>"



class LunarDecrescent(WEngine):
	def __init__(self):
		super().__init__("[Lunar] Decrescent", "B", "Attack", "atk", "atk_")

		self.baseStatLevel['mainStat'][0][0], self.baseStatLevel['subStat'][0][0] = 32 , 8.0
		self.baseStatLevel['mainStat'][0][10], self.baseStatLevel['subStat'][0][10] = 82 , 8.0
		self.baseStatLevel['mainStat'][1][10], self.baseStatLevel['subStat'][1][10] = 110 , 10.4
		self.baseStatLevel['mainStat'][1][20], self.baseStatLevel['subStat'][1][20] = 160 , 10.4
		self.baseStatLevel['mainStat'][2][20], self.baseStatLevel['subStat'][2][20] = 189 , 12.8
		self.baseStatLevel['mainStat'][2][30], self.baseStatLevel['subStat'][2][30] = 239 , 12.8
		self.baseStatLevel['mainStat'][3][30], self.baseStatLevel['subStat'][3][30] = 268 , 15.2
		self.baseStatLevel['mainStat'][3][40], self.baseStatLevel['subStat'][3][40] = 318 , 15.2
		self.baseStatLevel['mainStat'][4][40], self.baseStatLevel['subStat'][4][40] = 346 , 17.6
		self.baseStatLevel['mainStat'][4][50], self.baseStatLevel['subStat'][4][50] = 397 , 17.6
		self.baseStatLevel['mainStat'][5][50], self.baseStatLevel['subStat'][5][50] = 425 , 20.0
		self.baseStatLevel['mainStat'][5][60], self.baseStatLevel['subStat'][5][60] = 475 , 20.0

		self.passiveStats = [[15, 17.5, 20, 22.5, 25]]
		self.passiveDescription = "<p>Launching a Chain Attack or Ultimate increases the equipper's DMG by <span style=\"color: rgb(237,197,84)\">{0}%</span> for 6s.</p>"


class LunarNoviluna(WEngine):
	def __init__(self):
		super().__init__("[Lunar] Noviluna", "B", "Attack", "atk", "critRate_")

		self.baseStatLevel['mainStat'][0][0], self.baseStatLevel['subStat'][0][0] = 32 , 6.4
		self.baseStatLevel['mainStat'][0][10], self.baseStatLevel['subStat'][0][10] = 82 , 6.4
		self.baseStatLevel['mainStat'][1][10], self.baseStatLevel['subStat'][1][10] = 110 , 8.3
		self.baseStatLevel['mainStat'][1][20], self.baseStatLevel['subStat'][1][20] = 160 , 8.3
		self.baseStatLevel['mainStat'][2][20], self.baseStatLevel['subStat'][2][20] = 189 , 10.2
		self.baseStatLevel['mainStat'][2][30], self.baseStatLevel['subStat'][2][30] = 239 , 10.2
		self.baseStatLevel['mainStat'][3][30], self.baseStatLevel['subStat'][3][30] = 268 , 12.2
		self.baseStatLevel['mainStat'][3][40], self.baseStatLevel['subStat'][3][40] = 318 , 12.2
		self.baseStatLevel['mainStat'][4][40], self.baseStatLevel['subStat'][4][40] = 346 , 14.1
		self.baseStatLevel['mainStat'][4][50], self.baseStatLevel['subStat'][4][50] = 397 , 14.1
		self.baseStatLevel['mainStat'][5][50], self.baseStatLevel['subStat'][5][50] = 425 , 16.0
		self.baseStatLevel['mainStat'][5][60], self.baseStatLevel['subStat'][5][60] = 475 , 16.0

		self.passiveStats = [[3, 3.5, 4, 4.5, 5]]
		self.passiveDescription = "<p>Launching an EX Special Attack generates <span style=\"color: rgb(237,197,84)\">{0}</span> Energy for the equipper. This effect can trigger once every 12s.</p>"



class LunarPleniluna(WEngine):
	def __init__(self):
		super().__init__("[Lunar] Pleniluna", "B", "Attack", "atk", "atk_")

		self.baseStatLevel['mainStat'][0][0], self.baseStatLevel['subStat'][0][0] = 32 , 8.0
		self.baseStatLevel['mainStat'][0][10], self.baseStatLevel['subStat'][0][10] = 82 , 8.0
		self.baseStatLevel['mainStat'][1][10], self.baseStatLevel['subStat'][1][10] = 110 , 10.4
		self.baseStatLevel['mainStat'][1][20], self.baseStatLevel['subStat'][1][20] = 160 , 10.4
		self.baseStatLevel['mainStat'][2][20], self.baseStatLevel['subStat'][2][20] = 189 , 12.8
		self.baseStatLevel['mainStat'][2][30], self.baseStatLevel['subStat'][2][30] = 239 , 12.8
		self.baseStatLevel['mainStat'][3][30], self.baseStatLevel['subStat'][3][30] = 268 , 15.2
		self.baseStatLevel['mainStat'][3][40], self.baseStatLevel['subStat'][3][40] = 318 , 15.2
		self.baseStatLevel['mainStat'][4][40], self.baseStatLevel['subStat'][4][40] = 346 , 17.6
		self.baseStatLevel['mainStat'][4][50], self.baseStatLevel['subStat'][4][50] = 397 , 17.6
		self.baseStatLevel['mainStat'][5][50], self.baseStatLevel['subStat'][5][50] = 425 , 20.0
		self.baseStatLevel['mainStat'][5][60], self.baseStatLevel['subStat'][5][60] = 475 , 20.0

		self.passiveStats = [[12, 14, 16, 18, 20]]
		self.passiveDescription = "<p>Basic Attack, Dash Attack, and Dodge Counter DMG increase by <span style=\"color: rgb(237,197,84)\">{0}%</span>.</p>"


class MagneticStormAlpha(WEngine):
	def __init__(self):
		super().__init__("[Magnetic Storm] Alpha", "B", "Anomaly", "atk", "atk_")
		
		self.baseStatLevel['mainStat'][0][0], self.baseStatLevel['subStat'][0][0] = 32 , 8.0
		self.baseStatLevel['mainStat'][0][10], self.baseStatLevel['subStat'][0][10] = 82 , 8.0
		self.baseStatLevel['mainStat'][1][10], self.baseStatLevel['subStat'][1][10] = 110 , 10.4
		self.baseStatLevel['mainStat'][1][20], self.baseStatLevel['subStat'][1][20] = 160 , 10.4
		self.baseStatLevel['mainStat'][2][20], self.baseStatLevel['subStat'][2][20] = 189 , 12.8
		self.baseStatLevel['mainStat'][2][30], self.baseStatLevel['subStat'][2][30] = 239 , 12.8
		self.baseStatLevel['mainStat'][3][30], self.baseStatLevel['subStat'][3][30] = 268 , 15.2
		self.baseStatLevel['mainStat'][3][40], self.baseStatLevel['subStat'][3][40] = 318 , 15.2
		self.baseStatLevel['mainStat'][4][40], self.baseStatLevel['subStat'][4][40] = 346 , 17.6
		self.baseStatLevel['mainStat'][4][50], self.baseStatLevel['subStat'][4][50] = 397 , 17.6
		self.baseStatLevel['mainStat'][5][50], self.baseStatLevel['subStat'][5][50] = 425 , 20.0
		self.baseStatLevel['mainStat'][5][60], self.baseStatLevel['subStat'][5][60] = 475 , 20.0


		self.passiveStats = [[25, 28, 32, 36, 40]]
		self.passiveDescription = "<p>Accumulating Anomaly Buildup increases the equipper's Anomaly Mastery by <span style=\"color: rgb(237,197,84)\">{0}</span> for 10s. This effect can trigger once every 20s.</p>"
	


class MagneticStormBravo(WEngine):
	def __init__(self):
		super().__init__("[Magnetic Storm] Bravo", "B", "Anomaly", "atk", "anomalyProficiency")

		self.baseStatLevel['mainStat'][0][0], self.baseStatLevel['subStat'][0][0] = 32 , 24.0
		self.baseStatLevel['mainStat'][0][10], self.baseStatLevel['subStat'][0][10] = 82 , 24.0
		self.baseStatLevel['mainStat'][1][10], self.baseStatLevel['subStat'][1][10] = 110 , 31.2
		self.baseStatLevel['mainStat'][1][20], self.baseStatLevel['subStat'][1][20] = 160 , 31.2
		self.baseStatLevel['mainStat'][2][20], self.baseStatLevel['subStat'][2][20] = 189 , 38.4
		self.baseStatLevel['mainStat'][2][30], self.baseStatLevel['subStat'][2][30] = 239 , 38.4
		self.baseStatLevel['mainStat'][3][30], self.baseStatLevel['subStat'][3][30] = 268 , 45.6
		self.baseStatLevel['mainStat'][3][40], self.baseStatLevel['subStat'][3][40] = 318 , 45.6
		self.baseStatLevel['mainStat'][4][40], self.baseStatLevel['subStat'][4][40] = 346 , 52.8
		self.baseStatLevel['mainStat'][4][50], self.baseStatLevel['subStat'][4][50] = 397 , 52.8
		self.baseStatLevel['mainStat'][5][50], self.baseStatLevel['subStat'][5][50] = 425 , 60.0
		self.baseStatLevel['mainStat'][5][60], self.baseStatLevel['subStat'][5][60] = 475 , 60.0

		self.passiveStats = [[25, 28, 32, 36, 40]]
		self.passiveDescription = "<p>Accumulating Anomaly Buildup increases the equipper's Anomaly Proficiency by <span style=\"color: rgb(237,197,84)\">{0}</span> for 10s. This effect can only be triggered once every 20s.</p>"


class MagneticStormCharlie(WEngine):
	def __init__(self):
		super().__init__("[Magnetic Storm] Charlie", "B", "Anomaly", "atk", "pen_")

		self.baseStatLevel['mainStat'][0][0], self.baseStatLevel['subStat'][0][0] = 32 , 6.4
		self.baseStatLevel['mainStat'][0][10], self.baseStatLevel['subStat'][0][10] = 82 , 6.4
		self.baseStatLevel['mainStat'][1][10], self.baseStatLevel['subStat'][1][10] = 110 , 8.3
		self.baseStatLevel['mainStat'][1][20], self.baseStatLevel['subStat'][1][20] = 160 , 8.3
		self.baseStatLevel['mainStat'][2][20], self.baseStatLevel['subStat'][2][20] = 189 , 10.2
		self.baseStatLevel['mainStat'][2][30], self.baseStatLevel['subStat'][2][30] = 239 , 10.2
		self.baseStatLevel['mainStat'][3][30], self.baseStatLevel['subStat'][3][30] = 268 , 12.2
		self.baseStatLevel['mainStat'][3][40], self.baseStatLevel['subStat'][3][40] = 318 , 12.2
		self.baseStatLevel['mainStat'][4][40], self.baseStatLevel['subStat'][4][40] = 346 , 14.1
		self.baseStatLevel['mainStat'][4][50], self.baseStatLevel['subStat'][4][50] = 397 , 14.1
		self.baseStatLevel['mainStat'][5][50], self.baseStatLevel['subStat'][5][50] = 425 , 16.0
		self.baseStatLevel['mainStat'][5][60], self.baseStatLevel['subStat'][5][60] = 475 , 16.0


		self.passiveStats = [[3.5, 4, 4.5, 5, 5.5]]
		self.passiveDescription = "<p>Whenever a squad member inflicts an Attribute Anomaly on an enemy, the equipper generates <span style=\"color: rgb(237,197,84)\">{0}</span> Energy. This effect can trigger once every 12s.</p>"


class ReverbMarkI(WEngine):
	def __init__(self):
		super().__init__("[Reverb] Mark I", "B", "Support", "atk", "atk_")

		self.baseStatLevel['mainStat'][0][0], self.baseStatLevel['subStat'][0][0] = 32 , 8.0
		self.baseStatLevel['mainStat'][0][10], self.baseStatLevel['subStat'][0][10] = 82 , 8.0
		self.baseStatLevel['mainStat'][1][10], self.baseStatLevel['subStat'][1][10] = 110 , 10.4
		self.baseStatLevel['mainStat'][1][20], self.baseStatLevel['subStat'][1][20] = 160 , 10.4
		self.baseStatLevel['mainStat'][2][20], self.baseStatLevel['subStat'][2][20] = 189 , 12.8
		self.baseStatLevel['mainStat'][2][30], self.baseStatLevel['subStat'][2][30] = 239 , 12.8
		self.baseStatLevel['mainStat'][3][30], self.baseStatLevel['subStat'][3][30] = 268 , 15.2
		self.baseStatLevel['mainStat'][3][40], self.baseStatLevel['subStat'][3][40] = 318 , 15.2
		self.baseStatLevel['mainStat'][4][40], self.baseStatLevel['subStat'][4][40] = 346 , 17.6
		self.baseStatLevel['mainStat'][4][50], self.baseStatLevel['subStat'][4][50] = 397 , 17.6
		self.baseStatLevel['mainStat'][5][50], self.baseStatLevel['subStat'][5][50] = 425 , 20.0
		self.baseStatLevel['mainStat'][5][60], self.baseStatLevel['subStat'][5][60] = 475 , 20.0

		self.passiveStats = [[8, 9, 10, 11, 12]]
		self.passiveDescription = "<p>Launching an EX Special Attack increases all squad members' Impact by <span style=\"color: rgb(237,197,84)\">{0}%</span> for 10s. This effect can trigger once every 20s. Passive effects of the same name do not stack.</p>"



class ReverbMarkII(WEngine):
	def __init__(self):
		super().__init__("[Reverb] Mark II", "B", "Support", "atk", "energyRegen_")

		self.baseStatLevel['mainStat'][0][0], self.baseStatLevel['subStat'][0][0] = 32 , 16.0
		self.baseStatLevel['mainStat'][0][10], self.baseStatLevel['subStat'][0][10] = 82 , 16.0
		self.baseStatLevel['mainStat'][1][10], self.baseStatLevel['subStat'][1][10] = 110 , 20.8
		self.baseStatLevel['mainStat'][1][20], self.baseStatLevel['subStat'][1][20] = 160 , 20.8
		self.baseStatLevel['mainStat'][2][20], self.baseStatLevel['subStat'][2][20] = 189 , 25.6
		self.baseStatLevel['mainStat'][2][30], self.baseStatLevel['subStat'][2][30] = 239 , 25.6
		self.baseStatLevel['mainStat'][3][30], self.baseStatLevel['subStat'][3][30] = 268 , 30.4
		self.baseStatLevel['mainStat'][3][40], self.baseStatLevel['subStat'][3][40] = 318 , 30.4
		self.baseStatLevel['mainStat'][4][40], self.baseStatLevel['subStat'][4][40] = 346 , 35.2
		self.baseStatLevel['mainStat'][4][50], self.baseStatLevel['subStat'][4][50] = 397 , 35.2
		self.baseStatLevel['mainStat'][5][50], self.baseStatLevel['subStat'][5][50] = 425 , 40.0
		self.baseStatLevel['mainStat'][5][60], self.baseStatLevel['subStat'][5][60] = 475 , 40.0

		self.passiveStats = [[10, 12, 13, 15, 16]]
		self.passiveDescription = "<p>Launching an EX Special Attack or Chain Attack increases all squad members' Anomaly Mastery and Anomaly Proficiency by <span style=\"color: rgb(237,197,84)\">{0}</span> for 10s. This effect can trigger once every 20s. Passive effects of the same name do not stack.</p>"



class ReverbMarkIII(WEngine):
	def __init__(self):
		super().__init__("[Reverb] Mark III", "B", "Support", "atk", "hp_")

		self.baseStatLevel['mainStat'][0][0], self.baseStatLevel['subStat'][0][0] = 32 , 8.0
		self.baseStatLevel['mainStat'][0][10], self.baseStatLevel['subStat'][0][10] = 82 , 8.0
		self.baseStatLevel['mainStat'][1][10], self.baseStatLevel['subStat'][1][10] = 110 , 10.4
		self.baseStatLevel['mainStat'][1][20], self.baseStatLevel['subStat'][1][20] = 160 , 10.4
		self.baseStatLevel['mainStat'][2][20], self.baseStatLevel['subStat'][2][20] = 189 , 12.8
		self.baseStatLevel['mainStat'][2][30], self.baseStatLevel['subStat'][2][30] = 239 , 12.8
		self.baseStatLevel['mainStat'][3][30], self.baseStatLevel['subStat'][3][30] = 268 , 15.2
		self.baseStatLevel['mainStat'][3][40], self.baseStatLevel['subStat'][3][40] = 318 , 15.2
		self.baseStatLevel['mainStat'][4][40], self.baseStatLevel['subStat'][4][40] = 346 , 17.6
		self.baseStatLevel['mainStat'][4][50], self.baseStatLevel['subStat'][4][50] = 397 , 17.6
		self.baseStatLevel['mainStat'][5][50], self.baseStatLevel['subStat'][5][50] = 425 , 20.0
		self.baseStatLevel['mainStat'][5][60], self.baseStatLevel['subStat'][5][60] = 475 , 20.0

		self.passiveStats = [[8, 9, 10, 11, 12]]
		self.passiveDescription = "<p>Launching a Chain Attack or Ultimate increases all squad members' ATK by <span style=\"color: rgb(237,197,84)\">{0}%</span> for 10s. This effect can trigger once every 20s. Passive effects of the same name do not stack.</p>"



class VortexArrow(WEngine):
	def __init__(self):
		super().__init__("[Vortex] Arrow", "B", "Stun", "atk", "impact_")

		self.baseStatLevel['mainStat'][0][0], self.baseStatLevel['subStat'][0][0] = 32 , 4.8
		self.baseStatLevel['mainStat'][0][10], self.baseStatLevel['subStat'][0][10] = 82 , 4.8
		self.baseStatLevel['mainStat'][1][10], self.baseStatLevel['subStat'][1][10] = 110 , 6.2
		self.baseStatLevel['mainStat'][1][20], self.baseStatLevel['subStat'][1][20] = 160 , 6.2
		self.baseStatLevel['mainStat'][2][20], self.baseStatLevel['subStat'][2][20] = 189 , 7.7
		self.baseStatLevel['mainStat'][2][30], self.baseStatLevel['subStat'][2][30] = 239 , 7.7
		self.baseStatLevel['mainStat'][3][30], self.baseStatLevel['subStat'][3][30] = 268 , 9.1
		self.baseStatLevel['mainStat'][3][40], self.baseStatLevel['subStat'][3][40] = 318 , 9.1
		self.baseStatLevel['mainStat'][4][40], self.baseStatLevel['subStat'][4][40] = 346 , 10.6
		self.baseStatLevel['mainStat'][4][50], self.baseStatLevel['subStat'][4][50] = 397 , 10.6
		self.baseStatLevel['mainStat'][5][50], self.baseStatLevel['subStat'][5][50] = 425 , 12.0
		self.baseStatLevel['mainStat'][5][60], self.baseStatLevel['subStat'][5][60] = 475 , 12.0

		self.passiveStats = [[8, 9, 10, 11, 12]]
		self.passiveDescription = "<p>The equipper's attacks inflict <span style=\"color: rgb(237,197,84)\">{0}%</span> more Daze on their main target.</p>"


class VortexHatchet(WEngine):
	def __init__(self):
		super().__init__("[Vortex] Hatchet", "B", "Stun", "atk", "energyRegen_")

		self.baseStatLevel['mainStat'][0][0], self.baseStatLevel['subStat'][0][0] = 32 , 16.0
		self.baseStatLevel['mainStat'][0][10], self.baseStatLevel['subStat'][0][10] = 82 , 16.0
		self.baseStatLevel['mainStat'][1][10], self.baseStatLevel['subStat'][1][10] = 110 , 20.8
		self.baseStatLevel['mainStat'][1][20], self.baseStatLevel['subStat'][1][20] = 160 , 20.8
		self.baseStatLevel['mainStat'][2][20], self.baseStatLevel['subStat'][2][20] = 189 , 25.6
		self.baseStatLevel['mainStat'][2][30], self.baseStatLevel['subStat'][2][30] = 239 , 25.6
		self.baseStatLevel['mainStat'][3][30], self.baseStatLevel['subStat'][3][30] = 268 , 30.4
		self.baseStatLevel['mainStat'][3][40], self.baseStatLevel['subStat'][3][40] = 318 , 30.4
		self.baseStatLevel['mainStat'][4][40], self.baseStatLevel['subStat'][4][40] = 346 , 35.2
		self.baseStatLevel['mainStat'][4][50], self.baseStatLevel['subStat'][4][50] = 397 , 35.2
		self.baseStatLevel['mainStat'][5][50], self.baseStatLevel['subStat'][5][50] = 425 , 40.0
		self.baseStatLevel['mainStat'][5][60], self.baseStatLevel['subStat'][5][60] = 475 , 40.0

		self.passiveStats = [[9, 10, 11, 12, 13]]
		self.passiveDescription = "<p>Upon entering combat or switching in, the equipper's Impact increases by <span style=\"color: rgb(237,197,84)\">{0}%</span> for 10s. This effect can trigger once every 20s.</p>"



class VortexRevolver(WEngine):
	def __init__(self):
		super().__init__("[Vortex] Revolver", "B", "Stun", "atk", "atk_")

		self.baseStatLevel['mainStat'][0][0], self.baseStatLevel['subStat'][0][0] = 32 , 8.0
		self.baseStatLevel['mainStat'][0][10], self.baseStatLevel['subStat'][0][10] = 82 , 8.0
		self.baseStatLevel['mainStat'][1][10], self.baseStatLevel['subStat'][1][10] = 110 , 10.4
		self.baseStatLevel['mainStat'][1][20], self.baseStatLevel['subStat'][1][20] = 160 , 10.4
		self.baseStatLevel['mainStat'][2][20], self.baseStatLevel['subStat'][2][20] = 189 , 12.8
		self.baseStatLevel['mainStat'][2][30], self.baseStatLevel['subStat'][2][30] = 239 , 12.8
		self.baseStatLevel['mainStat'][3][30], self.baseStatLevel['subStat'][3][30] = 268 , 15.2
		self.baseStatLevel['mainStat'][3][40], self.baseStatLevel['subStat'][3][40] = 318 , 15.2
		self.baseStatLevel['mainStat'][4][40], self.baseStatLevel['subStat'][4][40] = 346 , 17.6
		self.baseStatLevel['mainStat'][4][50], self.baseStatLevel['subStat'][4][50] = 397 , 17.6
		self.baseStatLevel['mainStat'][5][50], self.baseStatLevel['subStat'][5][50] = 425 , 20.0
		self.baseStatLevel['mainStat'][5][60], self.baseStatLevel['subStat'][5][60] = 475 , 20.0

		self.passiveStats = [[10, 11.5, 13, 14.5, 16]]
		self.passiveDescription = "<p>EX Special Attacks inflict <span style=\"color: rgb(237,197,84)\">{0}%</span> more Daze.</p>"

wengines: dict[str, WEngine] = {
	# S rank
	"Deep Sea Visitor": DeepSeaVisitor(),
	"Fusion Compiler": FusionCompiler(),
	"Hellfire Gears": HellfireGears(),
	"Ice-Jade Teapot": IceJadeTeapot(),
	"Riot Suppressor Mark VI": RiotSuppressorMarkVI(),
	"Steel Cushion": SteelCushion(),
	"The Brimstone": TheBrimstone(),
	"The Restrained": TheRestrained(),
	"Weeping Cradle": WeepingCradle(),


	# A rank
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

	# B rank
	"[Identity] Base": IdentityBase(),
	"[Identity] Inflection": IdentityInflection(),
	"[Lunar] Decrescent": LunarDecrescent(),
	"[Lunar] Noviluna": LunarNoviluna(),
	"[Lunar] Pleniluna": LunarPleniluna(),
	"[Magnetic Storm] Alpha": MagneticStormAlpha(),
	"[Magnetic Storm] Bravo": MagneticStormBravo(),
	"[Magnetic Storm] Charlie": MagneticStormCharlie(),
	"[Reverb] Mark I": ReverbMarkI(),
	"[Reverb] Mark II": ReverbMarkII(),
	"[Reverb] Mark III": ReverbMarkIII(),
	"[Vortex] Arrow": VortexArrow(),
	"[Vortex] Hatchet": VortexHatchet(),
	"[Vortex] Revolver": VortexRevolver(),

}



