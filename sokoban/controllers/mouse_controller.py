from .controller import Controller
from ..map_entities import *
from ..tile_entities import TileMap
from ..tile_entities import TileType
from utils import *

class MouseController(Controller):

  def __init__(self, map_entity: MapEntity):
    super().__init__(map_entity)

  def move_entity(self, direction: Direction, tile_map: TileMap):
    dr, dc = direction_to_vector(direction)
    row, col = self._map_entity.get_row() + dr, self._map_entity.get_col() + dc
    entity, _ = tile_map.get_entities_at(row, col)

    # Mouse gets caught when it runs into a player!
    if entity and entity.get_type() == EntityType.PLAYER:
      tile_map.get_state_handler().obtain_mouse((self._map_entity.get_row(), self._map_entity.get_col()))
      tile_map.get_entity_grid().remove_moveable_entity(self._map_entity)
      return
      
    # Otherwise move as normal
    super().move_entity(direction, tile_map)

    
