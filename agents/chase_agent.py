from state import *
from utils import *
from .ai_agent import AIAgent
from random import random, randint, seed

class ChaseAgent(AIAgent):

  def __init__(self, entity):
    super().__init__(entity)
    
  def request_action(self, state):
    agent_pos = (self._entity.get_row(), self._entity.get_col())
    actions = GameStateHandler(state).get_agent_actions(agent_pos)

    pr, pc = state.get_player_position()

    if random() > 0.5:
      return actions[randint(0, len(actions) - 1)]
    
    best_action = actions[0]
    min_dis = float("inf")
    
    for direction in actions:
      dr, dc = direction_to_vector(direction)
      nr, nc = agent_pos[0] + dr, agent_pos[1] + dc

      distance = abs(nr - pr) + abs(nc - pc)

      if distance < min_dis:
        best_action = direction
        min_dis = distance
    
    return best_action
