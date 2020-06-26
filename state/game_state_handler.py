from .game_state import GameState
from utils import *

class GameStateHandler:

  def __init__(self, state):
    self._state = state

  def _attempt_box_move(self, pos, direction):
    dr, dc = direction_to_vector(direction)
    
    # Can't actually move the box so return
    if not self.can_move_box(pos, direction):
      return False

    # Make sure to handle the switching
    self.handle_switching(pos, (pos[0] + dr, pos[1] + dc))

    # Move the box now
    self.move_box(pos, (pos[0] + dr, pos[1] + dc))
    self.get_state().update_score(-4)
    
    return True

  def _attempt_player_move(self, direction):
    pr, pc = self._state.get_player_position()
    dr, dc = direction_to_vector(direction)
    new_row, new_col = pr + dr, pc + dc

    try:

      new_state = self._state.copy()
      state_handler = GameStateHandler(new_state)

      # Can't perform the move if there is a wall or a box we can't move
      if state_handler.is_wall(new_row, new_col):
        return None

      # There is a box in the way and we failed to move it
      if state_handler.is_box(new_row, new_col) and not state_handler._attempt_box_move((new_row, new_col), direction):
        return None

      if state_handler.is_armory_point(new_row, new_col):
        state_handler.obtain_point((new_row, new_col))

      if state_handler.is_mouse(new_row, new_col):
        state_handler.obtain_mouse((new_row, new_col))
        
      # If the player can activate a switch then check if we are moving on/off a switch
      if new_state.player_has_boots():
        state_handler.handle_switching((pr,pc), (new_row, new_col))

      # Did we win?
      if all(t for t in self._state.get_switches().values()):
        new_state.win()

      # Did we lose?
      if self.is_enemy(new_row, new_col):
        new_state.lose()
        
      new_state.set_player_position((new_row, new_col))
      new_state.update_score(-2)
      
      return new_state

    except IndexError:
      return None

  def _attempt_enemy_move(self, agent_pos, action):
    dr, dc = direction_to_vector(action)
    new_row, new_col = agent_pos[0] + dr, agent_pos[1] + dc
 
    try:

      new_state = self._state.copy()
      handler = GameStateHandler(new_state)

      # Can't perform the move if there is a wall or a box we can't move
      if handler.is_wall(new_row, new_col) or handler.is_box(new_row, new_col):
        return None

      handler.move_enemy(agent_pos, (new_row, new_col))

      # Enemy moved into the player so kill the player and the state is a lost game
      if (new_row, new_col) == new_state.get_player_position():
        new_state.lose()
        
      return new_state

    except IndexError:
      return None
    
  def _get_player_actions(self):
    return [pair[0] for pair in self.get_successors()]

  def _get_enemy_actions(self, enemy_pos):
    DIRECTIONS = [Direction.STOP, Direction.NORTH, Direction.EAST, Direction.SOUTH, Direction.WEST]
    possible_actions = []

    row_bound, col_bound = len(self._state.get_walls()), len(self._state.get_walls()[0])

    for direction in DIRECTIONS:
      row, col = direction_to_vector(direction)
      new_row, new_col = enemy_pos[0] + row, enemy_pos[1] + col

      in_bounds = new_row >= 0 and new_row < row_bound and new_col >= 0 and new_col < col_bound

      if in_bounds and not self.is_wall(new_row, new_col) and not self.is_box(new_row, new_col): 
        possible_actions.append(direction)

    return possible_actions
  
  def can_move_box(self, pos, direction):
    row, col = direction_to_vector(direction)
    new_row, new_col = pos[0] + row, pos[1] + col

    return not self.is_box(new_row, new_col) and not self.is_wall(new_row, new_col) 
  
  def handle_switching(self, o_pos, n_pos):
    
    # Moving from this switch, turn it off
    if self.is_switch(o_pos[0], o_pos[1]):
      self.flip_switch(o_pos)
      self._state.update_score(-50)

    # Deal with moving onto a switch, turn it on
    if self.is_switch(n_pos[0], n_pos[1]):
      self.flip_switch(n_pos)
      self._state.update_score(50)
    
  def get_state(self):
    return self._state.copy()

  def swap_state(self, state):
    self._state = state

  def is_wall(self, row, col):
    return self._state.get_walls()[row][col]

  def is_mouse(self, row, col):
    return (row, col) in self._state.get_mouse_locations()
  
  def is_box(self, row, col):
    return (row, col) in self._state.get_boxes()

  def is_enemy(self, row, col):
    return (row, col) in self._state.get_enemies()
  
  def is_switch(self, row, col):
    return (row, col) in self._state.get_switches()

  def is_armory_point(self, row, col):
    return (row, col) in self._state.get_remaining_points()
  
  def move_box(self, o_pos, n_pos):
    self._state.get_boxes().remove(o_pos)
    self._state.get_boxes().append(n_pos)

  def move_enemy(self, o_pos, n_pos):

    if o_pos in self._state.get_r_enemies():
      enemies = self._state.get_r_enemies()
    else:
      enemies = self._state.get_c_enemies()
    
    enemies.remove(o_pos)
    enemies.append(n_pos)

  def move_mouse(self, o_pos, n_pos):
    self._state.get_mouse_locations().remove(o_pos)
    self._state.get_mouse_locations().append(n_pos)
    
  def obtain_point(self, pos):
    self._state.update_obtained_points(1)
    self._state.get_remaining_points().remove(pos)
    self._state.update_score(25)

  def obtain_mouse(self, pos):
    self._state.get_mouse_locations().remove(pos)
    self._state.update_score(50)
    
  def flip_switch(self, pos):
    self._state.get_switches()[pos] = not self._state.get_switches()[pos]

  def get_agents(self):
    # Player goes first
    agents = [self._state.get_player_position()]

    # Then all the enemies
    for enemy in self._state.get_enemies():
      agents.append(enemy)

    for mouse in self._state.get_mouse_locations():
      agents.append(mouse)

    return agents

  def get_agent_count(self):
    return len(self.get_agents())
 
  def get_agent_actions(self, agent_pos):
    if agent_pos == self._state.get_player_position():
      return self._get_player_actions()
    else:
      return self._get_enemy_actions(agent_pos)
  
  def get_successor(self, agent_pos, action):
    if not action in self.get_agent_actions(agent_pos):
      return None

    if action == Direction.STOP:
      state = self._state.copy()
      state.update_score(-15)
      return state
    
    if agent_pos == self._state.get_player_position():
      return self._attempt_player_move(action)
    else:
      return self._attempt_enemy_move(agent_pos, action)
                     
  def get_successors(self):

    DIRECTIONS = [Direction.STOP, Direction.NORTH, Direction.EAST, Direction.SOUTH, Direction.WEST]
    successors = []

    for direction in DIRECTIONS:
      new_state = self._attempt_player_move(direction)
      
      if new_state:
        successors.append((direction, new_state))

    return successors

  def get_valid_positions(self):
    positions = []
    row_count, col_count = len(self._state.get_walls()), len(self._state.get_walls()[0])
    for r in range(row_count):
      for c in range(col_count):
        if not self.is_wall(r, c) and not self.is_box(r, c):
          positions.append((r,c))

    return positions
          
