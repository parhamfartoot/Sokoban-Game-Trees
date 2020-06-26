from .map_entity import MapEntity
from .entity_types import EntityType
from agents import RandomAgent

class Mouse(MapEntity, RandomAgent):
  
  def __init__(self, row: int, col: int):
    MapEntity.__init__(self, row, col, 4, EntityType.MOUSE) 
    RandomAgent.__init__(self, self)
