from state import *

class Heuristics:

  # We have included above two common heuristics, manhattan distance and euclidean distance so feel free to use
  # either if needed.
  #
  # Helpful functions:
  # GameState.get_boxes() --> returns a list of (row, col) positions representing where the boxes are on the map
  # GameState.get_switches() --> returns a dictionary where the keys are the locations of the switches as (row, col) and the value
  #                              being True if the switch is on and False if off.
  # GameState.get_player_position() --> returns the current position of the player in the form (row, col)
  # GameState.get_remaining_points() --> returns a list of the positions of the remaining armory points of the map in the form (row, col) 
  
  @staticmethod
  def manhattan_heuristic(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

  @staticmethod
  def euclidean_heuristic(p1, p2):
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5
 
  @staticmethod
  def two_boxes_heuristic(state):
    # Question 5, your solution for the two boxes heuristic will go here.
    # Return a heuristic value (an integer) representing the heuristic cost of the given state.
    raise NotImplementedError("Two Boxes Heuristic not implemented")
    
  @staticmethod
  def points_only_heuristic(state):
    # Question 6, your solution for the points only heuristic will go here.
    # Return a heuristic value (an integer) representing the heuristic cost of the given state.
    raise NotImplementedError("Points Only Heuristic not implemented")


      
