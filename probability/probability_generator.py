import random

class ProbabilityGenerator:

  @staticmethod
  def generate_probability():
    return random.random()

  @staticmethod
  def generate_range(limit):
    dist = [random.random() for i in range(limit)]
    dist.sort(reverse=True)

    return dist
