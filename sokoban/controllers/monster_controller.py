from .controller import Controller
from ..map_entities import *
from ..tile_entities import TileMap
from ..tile_entities import TileType
from utils import *

class MonsterController(Controller):

  def __init__(self, map_entity: MapEntity):
    super().__init__(map_entity)

  def move_entity(self, direction: Direction, tile_map: TileMap):
    dr, dc = direction_to_vector(direction)
    row, col = self._map_entity.get_row() + dr, self._map_entity.get_col() + dc
    entity, _ = tile_map.get_entities_at(row, col)
    
    if entity and entity.get_type() == EntityType.PLAYER:
      tile_map.get_state().lose()
      
    # Otherwise move as normal
    super().move_entity(direction, tile_map)

    
