from pydantic import BaseModel, Json
from typing import Literal, Any, Optional
import config


# Create your models here.
class AgentModel(BaseModel):
	name: str
	realName: str
	rank: config.RANKS
	attribute: config.ATTRIBUTES
	specialty: config.SPECIALTY
	faction: config.FACTIONS
	attackType: config.ATTACKTYPE


	nameIcon: Optional[str] = ""
	rankIcon: Optional[str] = ""
	attributeIcon: Optional[str] = ""
	specialtyIcon: Optional[str] = ""
	factionIcon: Optional[str] = ""
	attackTypeIcon: Optional[str] = ""

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.nameIcon = f'{config.BASE_DIR}/{config.MEDIA_DIR}/agents/Icon/{self.name}.png'
		self.rankIcon = f'{config.BASE_DIR}/{config.MEDIA_DIR}/rank/{self.rank}.png'
		self.attributeIcon = f'{config.BASE_DIR}/{config.MEDIA_DIR}/attributes/{self.attribute}.png'
		self.specialtyIcon = f'{config.BASE_DIR}/{config.MEDIA_DIR}/specialty/{self.specialty}.png'
		self.factionIcon = f'{config.BASE_DIR}/{config.MEDIA_DIR}/faction/{self.faction.replace(" ", "_")}.png'
		self.attackTypeIcon = f'{config.BASE_DIR}/{config.MEDIA_DIR}/attackType/{self.attackType}.png'


	def __str__(self):
		return f'{self.name}'
	

class AgentNameModel(BaseModel):
	pass