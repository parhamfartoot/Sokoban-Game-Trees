from enum import Enum

class Direction(Enum):
  STOP = (0, 0)
  NORTH = (-1, 0)
  SOUTH = (1, 0)
  EAST = (0, 1)
  WEST = (0, -1)

def direction_to_vector(direction:Direction):
  return direction.value

def vector_to_direction(vector):
  if vector == Direction.STOP.value:
    return Direction.STOP
  if vector == Direction.NORTH.value:
    return Direction.NORTH
  if vector == Direction.WEST.value:
    return Direction.WEST
  if vector == Direction.SOUTH.value:
    return Direction.SOUTH
  if vector == Direction.EAST.value:
    return Directin.EAST
