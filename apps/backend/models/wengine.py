from pydantic import BaseModel
from typing import Optional
import config


# Create your models here.
class WEngineModel(BaseModel):
	name: str
	rank: config.RANKS
	specialty: config.SPECIALTY
	# nameIcon: Optional[str]

	mainStat: tuple[str, float]
	subStat: tuple[str, float]

	passive: str

	def __str__(self):
		return f'{self.name}'