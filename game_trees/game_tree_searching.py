from state import *
from utils import *

import math


class GameTreeSearching:
    # You will also find that the GameStateHandler class (already imported) will help perform needed operations on the
    # the game states. To declare a GameStateHandler simply wrap it around a GameState like such,
    # handler = GameStateHandler(GameState) where GameState will be an instance of GameState.

    # Below is a list of helpful functions:
    # GameStateHandler.get_successors() --> returns successors of the handled state
    # GameStateHandler.get_agents() --> returns a list of the positions of the agents on the map
    # GameStateHandler.get_agent_count() --> returns the number of agents on the map
    # GameStateHandler.get_agent_actions(agent_pos) --> returns a list of the possible actions the given agent can take
    # GameStateHandler.get_successor(agent_pos, action) --> returns the successor state if the given agent took the given action
    # GameState.get_player_position() --> returns the players position in that game state as (row, col)
    # GameState.copy() --> returns a copy
    # GameState.is_win() --> returns True if the game state is a winning state
    # GameState.is_loss() --> returns True if the game state is a losing state

    # Hint:
    # To avoid unwanted issues with recursion and state manipulation you should work with a _copy_ of the state
    # instead of the original.

    @staticmethod
    def minimax_search(state, eval_fn, depth=2):
        # Question 1, your minimax search solution goes here
        # Returns a SINGLE action based off the results of the search
        state_copy = state.copy()
        return GameTreeSearching.minimax_search_helper(state_copy, eval_fn, depth, True)[0]

    @staticmethod
    def minimax_search_helper(state, eval_fn, depth, max_turn):
        best_move = None
        game_handler = GameStateHandler(state)
        agents = game_handler.get_agents()

        if depth == -2:  # reached depth end
            return best_move, eval_fn(state)
        elif (max_turn and state.is_win()) or ((not max_turn) and state.is_loss()):  # is win or lose
            return best_move, eval_fn(state)
        if max_turn:
            val = -math.inf
            agents = agents[:1]
        else:
            val = math.inf
            agents = agents[1:]
        for agent in agents:
            for move in game_handler.get_agent_actions(agent):
                nxt_pos = game_handler.get_successor(agent, move)
                nxt_move, nxt_val = GameTreeSearching.minimax_search_helper(nxt_pos, eval_fn, depth - 1, not max_turn)
                if max_turn:
                    if val < nxt_val:
                        val, best_move = nxt_val, move
                else:
                    if val > nxt_val:
                        val, best_move = nxt_val, move
        return best_move, val

    @staticmethod
    def alpha_beta_search(state, eval_fn, depth):
        # Question 2, your alpha beta pruning search solution goes here
        # Returns a SINGLE action based off the results of the search
        state_copy = state.copy()
        return GameTreeSearching.alpha_beta_search_helper(state_copy, eval_fn, depth, -math.inf, math.inf, True)[0]

    @staticmethod
    def alpha_beta_search_helper(state, eval_fn, depth, alpha, beta, max_turn):
        best_move = None
        game_handler = GameStateHandler(state)
        agents = game_handler.get_agents()

        if depth == -2:  # reached depth end
            return best_move, eval_fn(state)
        elif (max_turn and state.is_win()) or ((not max_turn) and state.is_loss()):  # is win or lose
            return best_move, eval_fn(state)

        if max_turn:
            val = -math.inf
            agents = agents[:1]
        else:
            val = math.inf
            agents = agents[1:]
        for agent in agents:
            for move in game_handler.get_agent_actions(agent):
                nxt_pos = game_handler.get_successor(agent, move)
                nxt_move, nxt_val = GameTreeSearching.alpha_beta_search_helper(nxt_pos, eval_fn, depth - 1, alpha, beta,
                                                                               not max_turn)
                if max_turn:
                    if val < nxt_val:
                        val, best_move = nxt_val, move
                    if val >= beta:
                        return best_move, val
                    alpha = max(alpha, val)
                else:
                    if val > nxt_val:
                        val, best_move = nxt_val, move
                    if val <= alpha:
                        return best_move, val
                    beta = min(beta, val)
        return best_move, val

    @staticmethod
    def expectimax_search(state, eval_fn, depth):
        # Question 3, your expectimax search solution goes here
        # Returns a SINGLE action based off the results of the search
        state_copy = state.copy()
        return GameTreeSearching.expectimax_search_helper(state_copy, eval_fn, depth, True)[0]

    @staticmethod
    def expectimax_search_helper(state, eval_fn, depth, max_turn):
        best_move = None
        game_handler = GameStateHandler(state)
        agents = game_handler.get_agents()

        if depth == -2:  # reached depth end
            return best_move, eval_fn(state)
        elif (max_turn and state.is_win()) or ((not max_turn) and state.is_loss()):  # is win or lose
            return best_move, eval_fn(state)

        if max_turn:
            val = -math.inf
            agents = agents[:1]
        else:
            val = 0
            agents = agents[1:]
        for agent in agents:
            for move in game_handler.get_agent_actions(agent):
                nxt_pos = game_handler.get_successor(agent, move)
                nxt_move, nxt_val = GameTreeSearching.expectimax_search_helper(nxt_pos, eval_fn, depth - 1,
                                                                               not max_turn)
                if max_turn:
                    if val < nxt_val:
                        val, best_move = nxt_val, move
                else:
                    val += 1 / len(game_handler.get_agent_actions(agent)) * nxt_val
        return best_move, val
