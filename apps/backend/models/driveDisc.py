from pydantic import BaseModel
from typing import Optional
import config


# Create your models here.
class DriveDiscModel(BaseModel):
	name: str

	passiveDescription2Pieces: str

	passiveDescription4Pieces: str

	def __str__(self):
		return f'{self.name}'