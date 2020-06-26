from state import *
from utils import *

class AIAgent:

  def __init__(self, entity):
    self._entity = entity
    
  def request_action(self, state):
    raise NotImplementedError("Request Action not implemented yet!")
