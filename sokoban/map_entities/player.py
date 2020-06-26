from .map_entity import MapEntity
from .entity_types import EntityType

class Player(MapEntity):

  def __init__(self, row: int, col: int):
    super().__init__(row, col, 0, EntityType.PLAYER)
    self._armory_count = 0
    self._is_dead = False
    
  def update_armory_count(self, count_update: int):
    self._armory_count += count_update
    
  def get_armory_count(self):
    return self._armory_count
  
  def has_boots(self):
    return self._armory_count >= 5

  def has_sword(self):
    return self._armory_count >= 10
    
  def kill(self):
    self._is_dead = True

  def is_dead(self):
    return self._is_dead

