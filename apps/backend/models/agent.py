from pydantic import BaseModel, Json
from typing import Literal, Any, Optional
from config import *

# Create your models here.
class AgentModel(BaseModel):
	name: str
	realName: str
	rank: Literal['S', 'A'] = 'S'
	attribute: Literal['Physical', 'Electric', 'Fire', 'Ice', 'Ether'] = 'Physical'
	fightingStyle: Literal['Attack', 'Stun', 'Anomaly', 'Support', 'Defense'] = 'Attack'
	faction: Literal['Victoria Housekeeping', 'Belobog Heavy Industries', 'Criminal Investigation Special Response Team', 'Cunning Hares', 'Obol Squad', 'Section 6', 'Sons of Calydon'] = 'Victoria Housekeeping'
	moduleType: Literal['Slash', 'Pierce', 'Strike'] = 'Slash'


	nameIcon: Optional[str] = ""
	rankIcon: Optional[str] = ""
	attributeIcon: Optional[str] = ""
	fightingStyleIcon: Optional[str] = ""
	factionIcon: Optional[str] = ""
	moduleTypeIcon: Optional[str] = ""

	baseStatLevel: dict = {}

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.nameIcon = f'{BASE_DIR}/{MEDIA_DIR}/agents/{self.name}.png'
		self.rankIcon = f'{BASE_DIR}/{MEDIA_DIR}/rank/{self.rank}.png'
		self.attributeIcon = f'{BASE_DIR}/{MEDIA_DIR}/attributes/{self.attribute}.png'
		self.fightingStyleIcon = f'{BASE_DIR}/{MEDIA_DIR}/fightingStyle/{self.fightingStyle}.png'
		self.factionIcon = f'{BASE_DIR}/{MEDIA_DIR}/faction/{self.faction.replace(" ", "_")}.png'
		self.moduleTypeIcon = f'{BASE_DIR}/{MEDIA_DIR}/moduleType/{self.moduleType}.png'



	def __str__(self):
		return f'{self.name}'