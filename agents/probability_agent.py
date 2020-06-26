from .ai_agent import AIAgent
from utils import vector_to_direction
from utils import direction_to_vector
from utils import Direction
from state import *

class ProbabilityAgent(AIAgent):
  
  def __init__(self, valid_positions):
    super().__init__(None)
    self._valid_positions = valid_positions
    self.reset_thoughts()

  def reset_thoughts(self):
    total_positions = len(self._valid_positions)
    self._thoughts = {pos : 1 / total_positions for pos in self._valid_positions}

  def listen(self, state):
    raise NotImplementedError("Agent's listen is not define")

  def predict(self, state):
    raise NotImplementedError("Agent's predict is not define")

  def thoughts(self):
    return self._thoughts
  
  def request_action(self, state):
    r, c = state.get_player_position()
    actions = GameStateHandler(state).get_agent_actions((r, c))
    actions.remove(Direction.STOP) # Don't want to stop
    
    current_max = float("-inf")
    best_pos = None
    
    for pos, prob in self._thoughts.items():
      if prob > current_max:
        current_max = prob
        best_pos = pos

    current_min = float("inf")
    chosen_action = None
    for action in actions:
      dr, dc = direction_to_vector(action)
      new_pos = (r + dr, c + dc)

      distance = abs(new_pos[0] - best_pos[0]) + abs(new_pos[1] - best_pos[1])
      if distance < current_min:
        current_min = distance
        chosen_action = action

    return chosen_action
