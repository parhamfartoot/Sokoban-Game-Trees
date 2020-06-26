from state import *
from state_searching import *


# Here you will implement evaluation functions. Recall that weighing components of your
# evaluation differently can have positive effects on performance. For example, you could
# have your evaluation prioritize running away from opposing agents instead of activiating
# switches. Also remember that for values such as minimum distance to have a positive effect
# you should inverse the value as _larger_ evaluation values are better than smaller ones.

# Helpful Functions:
# You may define any helper functions you want in this file.
# GameState.get_enemies() --> returns a list of opposing agent positions.
# GameState.get_boxes() --> returns a list of (row, col) positions representing where the boxes are on the map
# GameState.get_switches() --> returns a dictionary where the keys are the locations of the switches as (row, col) and the value
#                              being True if the switch is on and False if off.
# GameState.get_player_position() --> returns the current position of the player in the form (row, col)
# GameState.get_remaining_points() --> returns a list of the positions of the remaining armory points of the map in the form (row, col) 

class EvaluationFunctions:

    @staticmethod
    def score_evaluation(state):
        return state.get_score()

    @staticmethod
    def box_evaluation(state):
        # Question 4, your box evaluation solution goes here
        # Returns a numeric value evaluating the given state where the larger the better
        switch_box_distance = player_enemy_distance = 0

        for enemy in state.get_enemies():
            player_enemy_distance += Heuristics.manhattan_heuristic(enemy, state.get_player_position())

        for switch in state.get_switches():
            switch_box_distance += EvaluationFunctions.min_distance_box(switch, state)

        return switch_box_distance + player_enemy_distance

    @staticmethod
    def points_evaluation(state):
        # Question 5, your points evaluation solution goes here
        # Returns a numeric value evaluating the given state where the larger the better
        next_armor_distance = player_enemy_distance = 0

        for enemy in state.get_enemies():
            player_enemy_distance += Heuristics.manhattan_heuristic(enemy, state.get_player_position())

        for armor in state.get_remaining_points():
            next_armor_distance += EvaluationFunctions.min_distance_armory(armor, state)

        return next_armor_distance + player_enemy_distance

    @staticmethod
    def min_distance_box(switch, state):
        val = 0
        for box in state.get_boxes():
            switch_dis = 1 / Heuristics.manhattan_heuristic(box, switch)
            player_dis = 1 / Heuristics.manhattan_heuristic(box, state.get_player_position()) * 2
            val += switch_dis + player_dis
        return val

    @staticmethod
    def min_distance_armory(armor_2, state):
        val = 0
        for armor in state.get_remaining_points():
            armor_dis = EvaluationFunctions.div(1, Heuristics.manhattan_heuristic(armor, armor_2))
            player_dis = EvaluationFunctions.div(1,
                                                 Heuristics.manhattan_heuristic(armor, state.get_player_position()) * 2)
            val += armor_dis + player_dis
        return val

    @staticmethod
    def div(n, d):
        return n / d if d else 0
