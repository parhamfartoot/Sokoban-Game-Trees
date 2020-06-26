from tkinter import PhotoImage
from utils import constants
from ..map_entities import *
from typing import List
from .tile import Tile
from .tile_types import TileType
from state import *

class TileMap:

  def __init__(self, map_name: str, map_frame: List[List[int]]):

    self._state = GameState(map_file=map_name)
    self._handler = GameStateHandler(self._state)

    self._entity_grid = EntityGrid(self._state)
    
    self._row_count = len(self._state.get_walls())
    self._col_count = len(self._state.get_walls()[0])

    self._frame = map_frame
    
    self._load_tiles()

  def _load_tiles(self):
    # Tiles used for Sokoban (my own tiles)
    self._tiles = {0:Tile("assets/simple_tile.gif", False, TileType.SIMPLE),
                   1:Tile("assets/wall.gif", True, TileType.WALL),
                   2:Tile("assets/switch.gif", False, TileType.SWITCH)}

  def _update_state(self, map_entity, n_pos):
    entity_type = map_entity.get_type()
    o_pos = (map_entity.get_row(), map_entity.get_col())
    
    if entity_type == EntityType.PLAYER:
      self._state.set_player_position(n_pos)
      
      if self._state.player_has_boots():
        self._handler.handle_switching(o_pos, n_pos)

      if map_entity.is_dead():
        self._state.lose()
        
    elif entity_type == EntityType.BOX:
      self._handler.move_box(o_pos, n_pos)
      self._handler.handle_switching(o_pos, n_pos)

    elif entity_type == EntityType.MONSTER:
      self._handler.move_enemy(o_pos, n_pos)

    elif entity_type == EntityType.MOUSE:
      self._handler.move_mouse(o_pos, n_pos)
      
    # All switches activated
    if all(t for t in self._state.get_switches().values()):
      self._state.win()

  def move_on_map(self, map_entity, new_pos):
    self._update_state(map_entity, new_pos)

    # Remove the entity from the old position
    self._entity_grid.remove_moveable_entity(map_entity)
    
    # Move the entity
    map_entity.set_row(new_pos[0])
    map_entity.set_col(new_pos[1])
    
    # Place it back on the tile map in it's new position
    self._entity_grid.add_moveable_entity(map_entity)

  def get_entity_grid(self):
    return self._entity_grid
    
  def get_entities_at(self, row: int, col: int):
    return self._entity_grid.get_moveable(row, col), self._entity_grid.get_collectible(row, col)

  def get_state_handler(self):
    return self._handler 

  def get_state(self):
    return self._state
  
  def get_tile_entity_at(self, row: int, col: int):
    return self._tiles[self._frame[row][col]]

  def get_enemies(self):
    return [e for e in self._entity_grid.get_moveable_entities().values() if e.get_type() == EntityType.MONSTER]

  def get_mice(self):
    return [m for m in self._entity_grid.get_moveable_entities().values() if m.get_type() == EntityType.MOUSE]
  
  def get_switches(self):
    return self._state.get_switches()

  def flip_switch(self, row, col):
    self._handler.flip_switch((row,col))
    
  def get_row_count(self):
    return self._row_count

  def get_col_count(self):
    return self._col_count
        
  def get_width(self):
    return self._col_count * constants.TILESIZE

  def get_height(self):
    return self._row_count * constants.TILESIZE
 
