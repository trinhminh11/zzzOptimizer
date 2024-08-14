from pydantic import BaseModel, Json
from typing import Literal, Any, Optional

# Create your models here.
class AgentModel(BaseModel):
	name: str
	realName: str
	rank: Literal['S', 'A'] = 'S'
	attribute: Literal['Physical', 'Electric', 'Fire', 'Ice', 'Ether'] = 'Physical'
	fightingStyle: Literal['Attack', 'Stun', 'Anomaly', 'Support', 'Defense'] = 'Attack'
	faction: Literal['Victoria Housekeeping', 'Belobog Heavy Industries', 'Criminal Investigation Special Response Team', 'Cunning Hares', 'Obol Squad', 'Section 6', 'Sons of Calydon'] = 'Victoria Housekeeping'
	moduleType: Literal['Slash', 'Pierce', 'Strike'] = 'Slash'


	nameIcon: Optional[str]
	rankIcon: Optional[str]
	attributeIcon: Optional[str]
	fightingStyleIcon: Optional[str]
	factionIcon: Optional[str]
	moduleTypeIcon: Optional[str]

	baseStatLevel: dict = {}



	def __str__(self):
		return f'{self.name}'