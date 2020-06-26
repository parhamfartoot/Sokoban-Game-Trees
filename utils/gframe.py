from tkinter import Canvas, Frame, BOTH
from tkthread import tk, TkThread
from sokoban import Game

class GFrame(Frame):

  def __init__(self, title: str = "Game"):
    
    # Setup the master root
    self._master = tk.Tk()
    self._interactive_master = TkThread(self._master)
    self._master.title(title)
    self._master.protocol("WM_DELETE_WINDOW", self._close)
    self._master.resizable(False, False)
    
    super().__init__(self._master)
    self.pack(fill=BOTH, expand=1)
    self._canvas = Canvas(self)

    # Give the GFrame focus
    self.focus_set()

  def _close(self):
    self._game.set_done(True)

  def interactive_master(self):
    return self._interactive_master
    
  def display(self, game: Game):
    # Setup game
    self._game = game
    self._game.set_master(self._master)
    self._game.set_canvas(self._canvas)

    width, height = self._game.get_dimensions()
    self.set_size(width, height)

    self._game.bind_inputs(self)
    
  def set_size(self, new_width: int, new_height: int):
    self._master.geometry("{}x{}".format(new_width, new_height))
    self._canvas.config(width=new_width, height=new_height)
    self._canvas.pack(fill=BOTH, expand=1)

  def get_canvas(self) -> Canvas:
    return self._canvas
    
  def run(self):
    self._game.run()
