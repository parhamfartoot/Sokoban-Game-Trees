from collections import Counter
from .probability_generator import ProbabilityGenerator
from .distribution_model import DistributionModel

ECHO_FACTOR = 3
PRIME = 5

class EchoGrid:

  def update(self, state):
    self._echo_distribution = Counter()
    mouse_positions = state.get_mouse_locations()
    for pos in mouse_positions:
      r, c = pos
      self._echo_distribution[pos] = 1.0
      self._echo(r, c)

  def _echo(self, r, c):
    distance_probabilities = ProbabilityGenerator.generate_range(ECHO_FACTOR)
    
    # Echo out ECHO_FACTOR out in the four cardinal directions
    for i in range(ECHO_FACTOR):
      self._echo_distribution[(r - i, c)] += distance_probabilities[i]
      self._echo_distribution[(r + i, c)] += distance_probabilities[i]
      self._echo_distribution[(r, c - i)] += distance_probabilities[i]
      self._echo_distribution[(r, c + i)] += distance_probabilities[i]

    # Echo one less in the diagonals
    for i in range(ECHO_FACTOR - 1):
      self._echo_distribution[(r + i, c + i)] += distance_probabilities[i]
      self._echo_distribution[(r + i, c - i)] += distance_probabilities[i]
      self._echo_distribution[(r - i, c + i)] += distance_probabilities[i]
      self._echo_distribution[(r - i, c - i)] += distance_probabilities[i]

    DistributionModel.normalize(self._echo_distribution)

  def get_echo_distribution(self):
    return self._echo_distribution
