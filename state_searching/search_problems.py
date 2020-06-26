from state import *

class SearchProblems:

  @staticmethod
  def all_switches(state):
    switch_statuses = state.get_switches().values()
    return all(t for t in switch_statuses)

  @staticmethod
  def all_points(state):
    remaining_points = state.get_remaining_points()
    return len(remaining_points) == 0

  @staticmethod
  def find_position(state, position):
    return state.get_player_position() == position

  @staticmethod
  def no_boxes(state):
    # only armory points are available here and exactly one switch
    return state.player_has_boots() and all(t for t in state.get_switches().values())
