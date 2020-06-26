from state import *
from .ai_agent import AIAgent

SEARCH_DEPTH = 2 # Good value, the higher you go the more time it will take per move

class GenericAgent(AIAgent):
  
  def __init__(self, search_algorithm, eval_fn):
    super().__init__(None)
    self._search_algorithm = search_algorithm
    self._eval_fn = eval_fn
    
  def request_action(self, state):
    return self._search_algorithm(state, self._eval_fn, SEARCH_DEPTH)
