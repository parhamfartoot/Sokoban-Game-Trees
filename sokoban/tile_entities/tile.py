from tkinter import PhotoImage
from .tile_types import TileType

class Tile:

  def __init__(self, image_path: str, solid: bool, tile_type: TileType):
    self._image = PhotoImage(file=image_path)  
    self._solid = solid
    self._type = tile_type

  def set_type(self, tile_type: TileType):
    self._type = tile_type

  def get_type(self):
    return self._type
    
  def set_image(self, image_path: str):
    self._image_ref = PhotoImage(file=image_path)
    
  def get_image(self):
    return self._image
    
  def is_solid(self):
    return self._solid

  def set_solid(self, b: bool):
    self._solid = b

  def copy(self):
    return Tile(self._image_ref, self._solid, self._tile_type)
    
  
