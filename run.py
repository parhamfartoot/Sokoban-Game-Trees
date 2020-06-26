from utils import GFrame
from sokoban import Sokoban
from sokoban import TileMap
from argparse import ArgumentParser

if __name__ == "__main__":

  parser = ArgumentParser()

  parser.add_argument("-m", "--map", help="Map to run on", type=str, required = False, default = "test")
  
  args = parser.parse_args() 
  
  frame = GFrame("Sokoban")
  frame.display(Sokoban(30, args.map))
  frame.run() # Runs the Frame + Game 
