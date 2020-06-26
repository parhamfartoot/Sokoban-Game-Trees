from .box import Box
from .mouse import Mouse
from .armory_point import ArmoryPoint
from .random_monster import RandomMonster
from .chase_monster import ChaseMonster

class EntityGrid:

  def __init__(self, state):
    self._moveables = {}
    self._collectibles = {}

    # Add Boxes
    for pos in state.get_boxes():
      self._moveables[pos] = Box(pos[0], pos[1])

    # Add Points
    for pos in state.get_remaining_points():
      self._collectibles[pos] = ArmoryPoint(pos[0], pos[1])

    # Add Mice
    for pos in state.get_mouse_locations():
      self._moveables[pos] = Mouse(pos[0], pos[1])
      
    # Add Monsters
    for pos in state.get_r_enemies():
      self._moveables[pos] = RandomMonster(pos[0], pos[1])

    for pos in state.get_c_enemies():
      self._moveables[pos] = ChaseMonster(pos[0], pos[1])

  def add_moveable_entity(self, entity):
    pos = (entity.get_row(), entity.get_col())
    self._moveables[pos] = entity

  def remove_moveable_entity(self, entity):
    pos = (entity.get_row(), entity.get_col())
    del self._moveables[pos]

  def add_collectible_entity(self, entity):
    pos = (entity.get_row(), entity.get_col())
    self._collectibles[pos] = entity

  def remove_collectible_entity(self, entity):
    pos = (entity.get_row(), entity.get_col())
    del self._collectibles[pos]

  def get_collectible_entities(self):
    return self._collectibles

  def get_moveable_entities(self):
    return self._moveables

  def get_collectible(self, row, col):
    if (row, col) not in self._collectibles:
      return None

    return self._collectibles[(row, col)]

  def get_moveable(self, row, col):
    if (row, col) not in self._moveables:
      return None

    return self._moveables[(row, col)]
