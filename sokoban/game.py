from tkinter import Canvas, Tk
from time import time
from time import sleep

class Game():

  def __init__(self, fps: int):
    super().__init__()
    self._fps = fps # The fps to run the game at (how fast it renders)
    self._master = None
    self._canvas = None
    self._is_done = False

  def is_done(self):
    return self._is_done

  def set_done(self, b: bool):
    self._is_done = b
    
  def bind_inputs(self, frame):
    raise NotImplementedError("bindsInputs is not implemented yet")
    
  def _update(self):
    raise NotImplementedError("_update is not implemented yet")

  def _render(self):
    raise NotImplementedError("_render is not implemented yet")

  def _check_finished(self):
    raise NotImplementedError("_check_finished is not implemented yet")
  
  def set_master(self, master):
    self._master = master

  def set_canvas(self, canvas: Canvas):
    self._canvas = canvas
    
  def run(self):
    start = 0
    elapsed = 0
    wait = 0

    while not self.is_done():

      start = time()

      # Input happens straight from the window as soons as it happens using
      # bindings on the main root
      
      # Update
      self._update()
      
      # Render
      self._render()

      # Check if the game has finished
      self._check_finished()

      elapsed = time() - start
      wait = ((1000.0 / self._fps) - elapsed) / 1000000.0
      
      try:
        sleep(wait)
      except Exception as e:
        print(str(e))
        raise(e)

    self._master.destroy()
