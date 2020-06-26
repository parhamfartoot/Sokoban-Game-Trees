from utils import GFrame
from sokoban import *
from utils import *
from state import *
from time import sleep
from threading import Thread, currentThread, active_count
from tkthread import TkThread
import random

class Simulator():

  def __init__(self, map="fake", wait_time=1):
    self._map = map
    self._wait_time = wait_time
    self._verbose = False
    
  def _setup(self):
    self._frame = GFrame("Sokoban Simulator")
    self._game = Sokoban(30, self._map, True)
    self._frame.display(self._game)
    
  def verbose(self, b):
    self._verbose = b

  def swap_map(self, map_file):
    self._map = map_file
    
  def _simulate(self, agent):
    action = agent.request_action(self._game.get_state()) 
    if self._verbose:
      print("Move: ", action)

    self._game.move_player(action)
    self._game.move_enemies()

    return action
    
  def _simulate_tree_search(self, agent, record):
    if self._verbose:
      print("#------------STARTING SIMULATION------------#")
      
    # We change the way its scored
    # The agent just needs to turn on ONE switch by stepping on it
    self._game.get_state().update_obtained_points(5) # Give the player boots (ability to activate switches)

    # Loop while no switches are activated
    while all(not t for t in self._game.get_state().get_switches().values()):
      sleep(self._wait_time)
      record.append(self._simulate(agent))

    if self._verbose:
      print("#------------SIMULATION FINISHED------------#")

    self._game.set_done(True)

  def _simulate_probability_agent(self, agent, sense_func):
    if self._verbose:
      print("#------------STARTING SIMULATION------------#")

    # Simulate the given actions every "speed" seconds
    while self._game.get_state().get_mouse_locations():
      sleep(self._wait_time)
      sense_func(self._game.get_state())
      self._simulate(agent)
      
    self._game.set_done(True)
    
    if self._verbose:
      print("#------------SIMULATION FINISHED------------#")

  def simulate_generic_agent(self, agent):
    self._setup()

    # Quick Hack to help out when students haven't implemented a function yet
    try:
      agent.request_action(None)
    except AttributeError:
      pass
      
    record = []
    
    # Setup the simulation in its own thread
    simulation_thread = Thread(target= lambda: self._simulate_tree_search(agent, record), daemon=True)
    simulation_thread.start()
    
    # Run the game and frame
    self._frame.run()

    return record

  def simulate_probability_agent(self, agent, sense_func):
    self._setup()

    # Quick Hack to help out when students haven't implemented a function yet
    try:
      sense_func(None)
    except AttributeError:
      pass

    # Setup the simulation in its own thread
    simulation_thread = Thread(target = lambda : self._simulate_probability_agent(agent, sense_func), daemon=True)
    simulation_thread.start()

    # Run the game and frame
    self._frame.run()

    return self._game.get_state().get_score() 
