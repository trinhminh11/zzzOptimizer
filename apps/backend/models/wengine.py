from pydantic import BaseModel, Json
from typing import Literal, Any, Optional



# Create your models here.
class WEngineModel(BaseModel):
	name: str
	rank: Literal['S', 'A', 'B']

	mainStat: str
	subStat: str

	nameIcon: Optional[str]
	rankIcon: Optional[str]

	def __str__(self):
		return f'{self.name}'