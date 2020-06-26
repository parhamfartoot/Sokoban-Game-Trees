from ..map_entities import *
from ..tile_entities import TileMap
from ..tile_entities import TileType
from utils import *

class Controller:

  def __init__(self, map_entity: MapEntity):
    self._map_entity = map_entity

  def move_entity(self, direction: Direction, tile_map: TileMap):

    # Get the direction vector
    drow, dcol = direction_to_vector(direction)

    new_row = self._map_entity.get_row() + drow 
    new_col = self._map_entity.get_col() + dcol 

    # Avoid moving outside the bounds of the map
    if (new_row < 0 or new_col < 0
        or new_row > tile_map.get_row_count() - 1
        or new_col > tile_map.get_col_count() - 1):
      return False

    # Avoid moving into a Tile on the map which is solid (one which cannot be moved into)
    if tile_map.get_tile_entity_at(new_row, new_col).is_solid():
      return False

    blockable_entity, _ = tile_map.get_entities_at(new_row, new_col)

    # Can't move into another moveable entity
    if blockable_entity:
      return False

    # Update TileMap
    tile_map.move_on_map(self._map_entity, (new_row, new_col))

    return True
