class Stat:
	availableStat = [
		'',
		'hp',
		'hp_',
		'atk',
		'atk_',
		'def',
		'def_',
		'impact',
		'impact_',
		'critRate_',
		'critDMG_',
		'anomalyMastery',
		'anomalyProficiency',
		'pen',
		'pen_',
		'energyRegen',
		'energyRegen_',
		'electricDMG_',
		'physicalDMG_',
		'fireDMG_',
		'iceDMG_',
		'etherDMG_',
	]

	def __init__(self, key: str = "", value: float = 0.0):
		if key not in self.availableStat:
			raise ValueError()
		
		self.key = key
		self.value = value
