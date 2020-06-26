from collections import Counter
from .distribution_model import DistributionModel

class ParticleGrid:

  def __init__(self, valid_positions, particle_count=400):
    self._particle_count = particle_count
    self._valid_positions = valid_positions
    self.reset()

  def reset(self):
    # Question 3, your reset implementation goes here.
    # Recall this method resets the particle distribution to be a uniform distribution.
    # Make sure to have the particle distribution be a _Counter_ not a regular dictionary!
    
    self._particle_distribution = Counter()
    raise NotImplementedError("Reset method not implemented")
    
  def reweight_particles(self, distribution):
    # Qustion 4, your reweight particles implementation goes here.
    # This method focuses on updating the particle distribution by sampling the given distribution.
    # Remember to normalize the distribution!

    # For sampling use DistributionModel.sample_distribution(distribution, sample_amount) which will
    # return a list of legal positions got by sampling the given distribution.
    self._particle_distribution = Counter()
    raise NotImplementedError("Reweight Particles method not implemented")
    
      
  def get_particle_distribution(self):
    return self._particle_distribution
