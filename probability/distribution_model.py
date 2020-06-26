from .probability_generator import ProbabilityGenerator
from utils import direction_to_vector
from collections import Counter
import random

class DistributionModel:

  @staticmethod
  def normalize(distribution):
    s = float(sum(distribution.values()))
    for key in distribution:
      distribution[key] /= s

  @staticmethod
  def get_movement_distribution(state, mouse_pos):
    from state import GameStateHandler
    
    handler = GameStateHandler(state)
    possible_actions = handler.get_agent_actions(mouse_pos)
    player_pos = state.get_player_position()

    # How likely it is for a mouse to run away
    run_factor = random.random()

    distribution = Counter()
    for action in possible_actions:
      r, c = direction_to_vector(action)
      new_pos = (mouse_pos[0] + r, mouse_pos[1] + c)

      distance_to_player = abs(player_pos[0] - new_pos[0]) + abs(player_pos[1] - new_pos[1])
      distribution[new_pos] = distance_to_player * run_factor

      #distribution[new_pos] = 1.0
      
    DistributionModel.normalize(distribution)
    return distribution

  @staticmethod
  def sample_distribution(distribution, n):
    # Subject to change
    positions = list(distribution.keys())
    probabilities = list(distribution.values())
    total_positions = len(positions)
    
    threshold, i = random.random(), 0
    sample_size, cps, samples = 0, probabilities[random.randint(0, total_positions - 1)], []
    
    while sample_size < n:

      if cps > threshold:
        samples.append(positions[i])
        cps = probabilities[random.randint(0, total_positions - 1)]
        sample_size += 1
        threshold = random.random()
      else:
        i = i + 1 if i < total_positions - 1 else 0
        cps += probabilities[i]
        
    return samples
