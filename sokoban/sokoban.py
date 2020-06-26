from tkinter import Canvas, PhotoImage
from sokoban import *
from utils import *
from .controllers import *
from utils.utils import load_map

class Sokoban(Game):

  def __init__(self, fps, map_name, is_simulation = False):
    super().__init__(fps)
    self._HUD_HEIGHT = 50
    self._HUD_WIDTH = 300
    self._ENEMY_MOVEMENT_DELAY = 75
    self._is_simulation = is_simulation
    self._load(map_name)
    self._timer = 0
    
  def _load(self, map_name: str):
    
    self._player, map_frame = load_map(map_name)

    self._controller = PlayerController(self._player)
    
    self._map = TileMap(map_name, map_frame)

    # Add the player
    self._map.get_entity_grid().add_moveable_entity(self._player)

    self._switch_positions = self._map.get_switches()

    self._width = self._map.get_width() if self._map.get_width() > self._HUD_WIDTH else self._HUD_WIDTH
    self._height = self._map.get_height() + self._HUD_HEIGHT
  
  def move_player(self, direction: Direction):
    self._controller.move_entity(direction, self._map)

  def get_state(self):
    return self._map.get_state()
    
  def get_dimensions(self):
    return self._width, self._height 
    
  def bind_inputs(self, frame):
    frame.bind('<Escape>', lambda event: self._master.destroy())

    if not self._is_simulation:
      frame.bind('<Left>', lambda event: self.move_player(Direction.WEST))
      frame.bind('<Right>', lambda event: self.move_player(Direction.EAST))
      frame.bind('<Up>', lambda event: self.move_player(Direction.NORTH))
      frame.bind('<Down>', lambda event: self.move_player(Direction.SOUTH))
    
  def _render_map(self):
    for i in range(self._map.get_row_count()):
      for j in range(self._map.get_col_count()):
        tile = self._map.get_tile_entity_at(i, j)
        self._master.images.append(tile.get_image())
        self._canvas.create_image(j * constants.TILESIZE, i * constants.TILESIZE, image=tile.get_image(), anchor="nw") 

  def _render_hud(self):
    PIXEL_DIFF = 5
  
    # Fill in the empty space with a black rectangle
    self._canvas.create_rectangle(0, self._map.get_height(), self._width,
                                  self._map.get_height() + self._HUD_HEIGHT, fill = "black")

    # Put a smaller red border around it about 5 pixels in
    self._canvas.create_rectangle(PIXEL_DIFF, self._map.get_height() + PIXEL_DIFF,
                                  self._width - PIXEL_DIFF, self._map.get_height() + self._HUD_HEIGHT - PIXEL_DIFF,
                                  outline = "#CD6600")

    # Image of Armory Point
    img = PhotoImage(file=constants.ASSETS[constants.ARMORY_POINT_IMAGE_REF])
    self._master.images.append(img)
    self._canvas.create_image(PIXEL_DIFF * 2, self._map.get_height() + PIXEL_DIFF * 1.5, image=img, anchor="nw")

    # How Many Armory points the player has
    self._canvas.create_text(constants.TILESIZE + PIXEL_DIFF * 5, self._map.get_height() + PIXEL_DIFF * 6, fill="white",
                             font= ("Times", 20), text = self._map.get_state().get_obtained_points())

    # Make a line separator
    self._canvas.create_line(constants.TILESIZE + (PIXEL_DIFF * 12), self._map.get_height() + PIXEL_DIFF,
                             constants.TILESIZE + (PIXEL_DIFF * 12), self._height - PIXEL_DIFF, fill="#CD6600")

    self._canvas.create_text(constants.TILESIZE + (PIXEL_DIFF * 30), self._map.get_height() + PIXEL_DIFF * 6, fill="white",
                               font= ("Times", 20), text = "Score: {}".format(self._map.get_state().get_score()))

  def move_enemies(self):
    for enemy_agent in self._map.get_enemies():
      con = MonsterController(enemy_agent)
      con.move_entity(enemy_agent.request_action(self._map.get_state()), self._map)

    for mouse_agent in self._map.get_mice():
      con = MouseController(mouse_agent)
      con.move_entity(mouse_agent.request_action(self._map.get_state()), self._map)
      
  def _update(self):

    self._timer += 1

    # If the player is actually playing the game then move the enemies on
    # a clock.
    if not self._is_simulation and self._timer == self._ENEMY_MOVEMENT_DELAY:
      self.move_enemies()
      self._timer = 0
 
    self._canvas.update()
    
  def _render(self):

    #Attempt to render, and if it fails just wait for another chance
    
    try:
      # clear the screen to get ready for the next render
      self._master.images = []
      
      # Draw Tile Map
      self._render_map()

      # Draw Player
      player_img = PhotoImage(file=constants.ASSETS[self._player.get_image_ref()])
      self._master.images.append(player_img)
      self._canvas.create_image(self._player.get_x(), self._player.get_y(), image=player_img, anchor="nw")

      collectible_entities = {*self._map.get_entity_grid().get_collectible_entities().values()}
      moveable_entities = {*self._map.get_entity_grid().get_moveable_entities().values()}

      # Draw Collectibles
      for collectible in collectible_entities:
        img = PhotoImage(file=constants.ASSETS[collectible.get_image_ref()])
        self._master.images.append(img)
        self._canvas.create_image(collectible.get_x(), collectible.get_y(), image=img, anchor="nw") 

      # Draw Moveable Entities
      for entity in moveable_entities:
        img = PhotoImage(file=constants.ASSETS[entity.get_image_ref()])
        self._master.images.append(img)
        self._canvas.create_image(entity.get_x(), entity.get_y(), image=img, anchor="nw") 

      # Render a HUD for the user
      self._render_hud()
      
    except Exception as e:
      return


  def _check_finished(self):
    state = self._map.get_state()
    
    if state.is_win():
      if not self._is_simulation: print("Win:\n Your score was {}.".format(state.get_score()))
      self.set_done(True)
      
    if state.is_loss():
      if not self._is_simulation: print("Loss:\n Your score was {}.".format(state.get_score()))
      self.set_done(True)
        
