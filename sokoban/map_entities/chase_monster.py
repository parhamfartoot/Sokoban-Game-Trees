from .monster import Monster
from agents import ChaseAgent

class ChaseMonster(Monster, ChaseAgent):

  def __init__(self, row: int, col: int):
    Monster.__init__(self, row, col)
    ChaseAgent.__init__(self, self)
