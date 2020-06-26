from json import load
from utils import Direction

def direction_to_string(direction):
  if direction == Direction.STOP:
    return "stop"

  elif direction == Direction.NORTH:
    return "north"

  elif direction == Direction.SOUTH:
    return "south"

  elif direction == Direction.WEST:
    return "west"

  elif direction == Direction.EAST:
    return "east"

def convert_answer(answer):
  return [direction_to_string(direction) for direction in answer]

def load_test(test_name):
  with open("assets/tests/{}.json".format(test_name), "r") as f:
    test = load(f)
    
  return test["test_name"], test["maps"], test["seed"], test["solution"]
