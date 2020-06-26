from .map_entity import MapEntity
from .entity_types import EntityType

class Monster(MapEntity):

  def __init__(self, row: int, col: int):
    super().__init__(row, col, 3, EntityType.MONSTER)
