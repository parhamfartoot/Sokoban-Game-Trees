from .monster import Monster
from agents import RandomAgent

class RandomMonster(Monster, RandomAgent):

  def __init__(self, row: int, col: int):
    Monster.__init__(self, row, col)
    RandomAgent.__init__(self, self)
