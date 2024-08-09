from pydantic import BaseModel, Json
from typing import Literal, Any, Optional

# def auto_increment():
# 	largest = agentModel.objects.all().order_by('id').last()
# 	if not largest:
# 		return 1
# 	return largest.id + 1

# Create your models here.
class AgentModel(BaseModel):
	id: int
	name: str
	realName: str
	rank: Literal['S', 'A'] = 'S'
	attribute: Literal['Physical', 'Electric', 'Fire', 'Ice', 'Ether'] = 'Physical'
	fightingStyle: Literal['Attack', 'Stun', 'Anomaly', 'Support', 'Defense'] = 'Attack'
	faction: Literal['Victoria Housekeeping', 'Belobog Heavy Industries', 'Criminal Investigation Special Response Team', 'Cunning Hares', 'Obol Squad', 'Section 6', 'Sons of Calydon'] = 'Victoria Housekeeping'
	moduleType: Literal['Slash', 'Pierce', 'Strike'] = 'Slash'

	baseStat: dict = {}

	nameIcon: Optional[str]
	rankIcon: Optional[str]
	attributeIcon: Optional[str]
	fightingStyleIcon: Optional[str]
	factionIcon: Optional[str]
	moduleTypeIcon: Optional[str]


	def __str__(self):
		return f'{self.name}'