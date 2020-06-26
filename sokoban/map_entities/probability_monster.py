from .monster import Monster
from agents import ProbabilityAgent

class ChaseMonster(Monster, ProbabilityAgent):

  def __init__(self, row: int, col: int):
    Monster.__init__(self, row, col)
    ProbabilityAgent.__init__(self, self)
