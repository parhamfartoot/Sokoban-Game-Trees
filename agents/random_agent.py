from state import *
from utils import *
from random import randint
from .ai_agent import AIAgent

class RandomAgent(AIAgent):

  def __init__(self, entity):
    super().__init__(entity)
    
  def request_action(self, state):
    agent_pos = (self._entity.get_row(), self._entity.get_col())
    actions = GameStateHandler(state).get_agent_actions(agent_pos)

    return actions[randint(0, len(actions) - 1)]
