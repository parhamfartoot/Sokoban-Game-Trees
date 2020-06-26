from .constants import *
import json

_NORMAL = 0
_WALL = 1
_SWITCH = 2

def load_map(map_name: str):

  from sokoban import Player

  with open("assets/maps/{}.json".format(map_name), "r") as f:
    info = json.load(f)

    map_frame = info["map"]

    p_r, p_c = info["player"]
    player = Player(p_r, p_c)

  return player, map_frame

def load_state(map_name: str):
  with open("assets/maps/{}.json".format(map_name), "r") as f:
    map_info = json.load(f)
    
    map_state = map_info["map"]
    
    row_count = len(map_state)
    col_count = len(map_state[0])
      
    walls = []
    switches = {}
  
    for r in range(len(map_state)):
      row = []
      for c in range(len(map_state[0])):
        row.append(1 if map_state[r][c] == _WALL else 0) 
        
        if map_state[r][c] == _SWITCH: # Might as well add in switches at the same time
          switches[(r,c)] = False
          
      walls.append(row)
          
    start_position = tuple(map_info["player"])
          
    boxes = [tuple(b) for b in map_info["boxes"]]
    
    points = [tuple(p) for p in map_info["points"]]
    
    random_enemies = [tuple(e) for e in map_info["random_enemies"]]

    chase_enemies = [tuple(e) for e in map_info["chase_enemies"]]

    mice = [tuple(p) for p in map_info["mice"]]
    
  return walls, start_position, boxes, switches, points, mice, random_enemies, chase_enemies
    
