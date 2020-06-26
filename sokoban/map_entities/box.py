from .map_entity import MapEntity
from .entity_types import EntityType

class Box(MapEntity):

  def __init__(self, row: int, col: int):
    super().__init__(row, col, 1, EntityType.BOX)
