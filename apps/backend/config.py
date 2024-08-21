from typing import Literal

host = "127.0.0.1"
port = 8000

BASE_DIR = f'http://{host}:{port}'
MEDIA_DIR = "media"

RANKS = Literal["S", "A", "B"]
SPECIALTY = Literal["Attack", "Anomaly", "Stun", "Support", "Defense"]
ATTRIBUTES = Literal['Physical', 'Electric', 'Fire', 'Ice', 'Ether']
ATTACKTYPE = Literal['Slash', 'Strike', 'Pierce']
FACTIONS = Literal['Victoria Housekeeping', 'Belobog Heavy Industries', 'Criminal Investigation Special Response Team', 'Cunning Hares', 'Obol Squad', 'Section 6', 'Sons of Calydon']