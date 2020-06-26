from .controller import Controller
from ..map_entities import *
from ..tile_entities import TileMap
from ..tile_entities import TileType
from utils import *

class PlayerController(Controller):

  def __init__(self, map_entity: MapEntity):
    super().__init__(map_entity)
    
  def move_entity(self, direction: Direction, tile_map: TileMap):
    dr, dc = direction_to_vector(direction)
    row, col = self._map_entity.get_row() + dr, self._map_entity.get_col() + dc
    entity, collectible = tile_map.get_entities_at(row, col)

    if collectible: 
      tile_map.get_state_handler().obtain_point((collectible.get_row(), collectible.get_col())) 
      tile_map.get_entity_grid().remove_collectible_entity(collectible)

    if entity and entity.get_type() == EntityType.MOUSE:
      tile_map.get_state_handler().obtain_mouse((entity.get_row(), entity.get_col()))
      tile_map.get_entity_grid().remove_moveable_entity(entity)
      
    # Do a check for a box, since we can try to move it
    if entity and entity.get_type() == EntityType.BOX:

      # Do some recursion and try to move the box
      box_controller = Controller(entity)
      box_controller.move_entity(direction, tile_map) 

    if entity and entity.get_type() == EntityType.MONSTER:
      tile_map.get_state().lose()
      
    moved = super().move_entity(direction, tile_map)
    
    if moved:
      tile_map.get_state().update_score(-2)

      if entity and entity.get_type() == EntityType.BOX:
        tile_map.get_state().update_score(-4) 
      


    
