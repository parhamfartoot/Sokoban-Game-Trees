from .map_entity import MapEntity
from .entity_types import EntityType

class ArmoryPoint(MapEntity):

  def __init__(self, row: int, col: int):
    super().__init__(row, col, 2, EntityType.POINT)
    
