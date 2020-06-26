from state import *
from utils import *

# For the Below implementations we have already imported a Stack class, a Queue class and a PriorityQueue class
# to help you complete the algorithms. PLEASE DO NOT ADD OR REMOVE ANY IMPORTS.

# You will also find that the GameStateHandler class (already imported) will help perform needed operations on the
# the game states. To declare a GameStateHandler simply wrap it around a GameState like such,
# handler = GameStateHandler(GameState) where GameState will be an instance of GameState.

# Below is a list of helpful functions:
# GameStateHandler.get_successors() --> returns successors of the handled state
# GameState.get_player_position() --> returns the players position in that game state as (row, col)

class SearchAlgorithms:

  @staticmethod
  def depth_first_search(goal_fn, start_state):
    # Question 1, your DFS solution should go here
    # Returns a list of actions to take to get to the solution or [] if no solution exists 
    raise NotImplementedError("Depth First Search not implemented")

  @staticmethod
  def breadth_first_search(goal_fn, start_state):
    # Question 2, your BFS solution should go here
    # Returns a list of actions to take to get to the solution or [] if no solution exists 
    raise NotImplementedError("Breadth First Search not implemented")

  @staticmethod
  def uniform_cost_search(goal_fn, start_state, cost_fn = lambda pos : 1):
    # Question 3, your UCS solution should go here
    # Returns a list of actions to take to get to the solution or [] if no solution exists 
    raise NotImplementedError("Uniform Cost Search not implemented")
  
  @staticmethod
  def a_star_search(goal_fn, start_state, cost_fn = lambda pos : 1, heuristic = lambda state: 0):
    # Question 4, your A Star solution should go here
    # Returns a list of actions to take to get to the solution or [] if no solution exists 
    raise NotImplementedError("A Star Search not implemented")
 
