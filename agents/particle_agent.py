from .probability_agent import ProbabilityAgent
from utils import vector_to_direction
from probability import *
from state import *
from collections import Counter

class ParticleAgent(ProbabilityAgent):
  
  def __init__(self, valid_positions):
    super().__init__(valid_positions)
    self._particle_grid = ParticleGrid(self._valid_positions)
    self._echo_grid = EchoGrid()
    self._thoughts = self._particle_grid.get_particle_distribution()

  # Helpful Hints and Functions:
  # EchoGrid.get_echo_distribution() --> returns a distribution over all legal positions on the map as a dictionary
  #                                      where the key is a position and value is the probability of a mouse being there.
  # ProbabilityAgent.reset_thoughts() --> resets self._thoughts to be uniform (i.e. agent thinks all positions may have a mouse)
  # DistributionModel.normalize(distribution) --> normalizes the given distribution
  # DistributionModel.get_movement_distribution(state, agent_pos) --> returns a movement distribution for the given agent through it's position 
  # GameState.copy() --> returns a copy
  # GameStateHandler.move_mouse(old_pos, new_pos) --> moves the mouse from the old position to the new position on the map
  # ParticleGrid.reset() --> Resets the particle distribution to be uniform
  # ParticleGrid.reweight_particles(distribution) --> reweights the particles based on the given distribution
  
  # Instead of using a regular dictionary we recommend you use a Counter object to avoid needing to check for keys before using
  # them. Counters default any unseen key to the value of 0.

  # Remember to normalize brefore updating the agents thoughts and to look over only valid positions (use self._valid_positions).
  
  def listen(self, state):
    # Question 5, your ParticleAgent listen solution goes here.
    # Similar to the MarkovAgent this method uses echo distributions from the EchoGrid but it also uses particle distributions
    # provided by the ParticleGrid build the agent's thoughts. Just like the MarkovAgent there is a special case to consider which
    # happens when the distribution given by the EchoGrid has only information which has NOT been seen before. In this case you must
    # reset your current thought distribution AND the particle distribution before continuing. Remember to reweight the particles after
    # updating the agent's thoughts.

    # Uncomment this when you start implementing
    # self._echo_grid.update(state)

    # Write your code here
    raise NotImplementedError("ParticleAgent's Listen not implemented")
    
  def predict(self, state):
    # Question 6, your ParticleAgent predict solution goes here.
    # Recall for the predict method we want to track one mouse down at a time by "predicting their moves". This should
    # be done through moving the mouse into positions on the map using this distribution to update your thoughts.
    # To avoid annoyances of state manipulation you should use a copy of the given state when you pretend to move the mouse
    # so that it does not effect the actual state.

    # As an addition the special case from above carries through to this method and should be handled in the same fashion
    # and remember to reweight the particles after updating the agent's thoughts.

    # Uncomment this when you start implementing
    # self._echo_grid.update(state) # Do Not Remove, it is required to have the EchoGrid give accurate information

    # Write your code here
    raise NotImplementedError("ParticleAgent's Predict not implemented")
