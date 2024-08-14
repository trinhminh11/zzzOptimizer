from pydantic import BaseModel, Json
from typing import Literal, Any, Optional


# def auto_increment():
# 	largest = agentModel.objects.all().order_by('id').last()
# 	if not largest:
# 		return 1
# 	return largest.id + 1

# Create your models here.
class WEngineModel(BaseModel):
	name: str
	rank: Literal['S', 'A', 'B'] = 'S'

	mainStat: str
	subStat: str

	nameIcon: Optional[str]
	rankIcon: Optional[str]

	baseStatLevel: dict = {}

	

	def __str__(self):
		return f'{self.name}'