from utils.utils import load_state


class GameState:

    def __init__(self, map_file=None, prev_state=None):

        # If we have a previous state, copy over the information
        if prev_state:
            self._walls = prev_state.get_walls()
            self._player_position = prev_state.get_player_position()
            self._boxes = prev_state.get_boxes()[:]
            self._switches = {**prev_state.get_switches()}
            self._armory_points = prev_state.get_remaining_points()[:]
            self._mice = prev_state.get_mouse_locations()[:]
            self._points_obtained = prev_state.get_obtained_points()
            self._score = prev_state.get_score()
            self._r_enemies = prev_state.get_r_enemies()[:]
            self._c_enemies = prev_state.get_c_enemies()[:]
            self._win = prev_state.is_win()
            self._loss = prev_state.is_loss()

        # Otherwise, load it from scratch using the given file
        elif map_file:
            self._walls, self._player_position, self._boxes, self._switches, self._armory_points, self._mice, self._r_enemies, self._c_enemies = load_state(
                map_file)
            self._points_obtained = 0
            self._score = 0
            self._win = False
            self._loss = False

        # Got neither, there is an error
        else:
            raise AttributeError("Neither Map Name nor Previous State are given")

    def copy(self):
        return GameState(prev_state=self)

    def get_walls(self):
        return self._walls

    def is_win(self):
        return self._win

    def is_loss(self):
        return self._loss

    def win(self):
        self._win = True
        self._score += 500

    def lose(self):
        self._loss = True
        self._score -= 500

    def get_score(self):
        return self._score

    def get_enemies(self):
        enemies = []
        for e in self._r_enemies:
            enemies.append(e)

        for e in self._c_enemies:
            enemies.append(e)

        return enemies

    def get_r_enemies(self):
        return self._r_enemies

    def get_c_enemies(self):
        return self._c_enemies

    def update_score(self, amt):
        self._score += amt

    def update_obtained_points(self, count):
        self._points_obtained += count

    def get_obtained_points(self):
        return self._points_obtained

    def player_has_boots(self):
        return self._points_obtained >= 5

    def get_remaining_points(self):
        return self._armory_points

    def get_mouse_locations(self):
        return self._mice

    def get_boxes(self):
        return self._boxes

    def get_player_position(self):
        return self._player_position

    def set_player_position(self, new_position):
        self._player_position = new_position

    def get_switches(self):
        return self._switches

    def __str__(self):
        info = "#---------INFO-START---------#\n" \
               "Box Locations:\n" \
               "{}\n\n" \
               "Switch Locations:\n" \
               "{}\n\n" \
               "Remaining Armory Point Locations:\n" \
               "{}\n\n" \
               "Enemy Locations\n" \
               "{}\n\n" \
               "Player Location:\n" \
               "{}\n\n" \
               "Mouse Locations:\n" \
               "{}\n\n" \
               "Score:\n" \
               "{}\n" \
               "#---------INFO-END-----------#\n".format(self._boxes, self._switches, self._armory_points,
                                                         self.get_enemies(), self._player_position, self._mice,
                                                         self._score)
        return info

    def __eq__(self, other):
        return self._boxes == other.get_boxes() \
               and self._switches == other.get_switches() \
               and self._armory_points == other.get_remaining_points() \
               and self._player_position == other.get_player_position() \
               and self.get_enemies() == other.get_enemies() \
               and self.get_mouse_locations() == other.get_mouse_locations()

    def __hash__(self):
        val = hash(tuple(self._boxes)) + hash(tuple(self._switches)) \
              + hash(tuple(self._armory_points)) + hash(self._player_position) \
              + hash(tuple(self.get_enemies())) + hash(tuple(self._mice))
        return val
