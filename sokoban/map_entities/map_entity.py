from utils import *
from .entity_types import EntityType

class MapEntity:

  def __init__(self, row: int, col: int, image_ref: int, entity_type: EntityType):
    self._row = row
    self._col = col
    self._image_ref = image_ref
    self._entity_type = entity_type
    
  def get_row(self) -> int:
    return self._row

  def get_col(self) -> int:
    return self._col

  def set_row(self, row:int):
    self._row = row
    
  def set_col(self, col:int):
    self._col = col

  def get_x(self) -> int:
    return self._col * constants.TILESIZE

  def get_y(self) -> int:
    return self._row * constants.TILESIZE

  def get_image_ref(self) -> int:
    return self._image_ref

  def set_image_ref(self, image_ref):
    self._image_ref = image_ref

  def get_type(self) -> str:
    return self._entity_type

  def set_type(self, entity_type: EntityType):
    self._entity_type = entity_type
