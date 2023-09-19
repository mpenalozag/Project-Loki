import copy

class State:
  def __init__(self, display, agent_coords):
    self.display = display
    self.agent_coords = agent_coords
    self.previous_move = None

  def print_self(self):
    for row in self.display:
      print(row)

  def get_possible_states(self):
    """
    Function that returns all possible states from this state.
    """
    pass

  def get_valid_movements(self):
    """
    Function that returns all valid movements, in a list, from current position.
    """
    pass

  def __eq__(self, other):
    return self.display == other.display


class SlidingState(State):
  def __init__(self, display, agent_coords):
    super().__init__(display, agent_coords)

  def get_possible_states(self):
    """
    Function that returns all possible states from this state.
    """
    valid_movements = self.get_valid_movements()
    possible_states = []
    for movement in valid_movements:
      new_display = copy.deepcopy(self.display)
      new_display[self.agent_coords[0]][self.agent_coords[1]] = new_display[movement[0][0]][movement[0][1]]
      new_display[movement[0][0]][movement[0][1]] = 0
      new_state = SlidingState(new_display, movement[0])
      new_state.previous_move = movement[1]
      possible_states.append(new_state)
    return possible_states

  def get_valid_movements(self):
    """
    Function that returns all valid movements from current agent position, in a list, from current position.
    """
    valid_movements = []
    # Change in position
    if not (self.agent_coords[0] - 1 < 0):
      valid_movements.append( [[self.agent_coords[0]-1, self.agent_coords[1]], "UP"] )
    if not (self.agent_coords[1] - 1 < 0):
      valid_movements.append( [[self.agent_coords[0], self.agent_coords[1]-1], "LEFT"] )
    if not (self.agent_coords[0] + 1 >= len(self.display)):
      valid_movements.append( [[self.agent_coords[0]+1, self.agent_coords[1]], "DOWN"] )
    if not (self.agent_coords[1] + 1 >= len(self.display[0])):
      valid_movements.append( [[self.agent_coords[0], self.agent_coords[1]+1], "RIGHT"] )
    return valid_movements


class VacuumState(State):
  def __init__(self, display, agent_coords):
    super().__init__(display, agent_coords)

  def get_possible_states(self):
    """
    Function that returns all possible states from this state.
    """
    valid_movements = self.get_valid_movements()
    possible_states = []
    for movement in valid_movements:
      new_display = copy.deepcopy(self.display)
      if movement[0] == "S":
        new_display[self.agent_coords[0]][self.agent_coords[1]][0] = "C"
        new_state = VacuumState(new_display, self.agent_coords)
      else:
        new_display[self.agent_coords[0]][self.agent_coords[1]][1] = " "
        new_display[movement[0][0]][movement[0][1]][1] = "A"
        new_state = VacuumState(new_display, movement[0])
      new_state.previous_move = movement[1]
      possible_states.append(new_state)
    return possible_states

  def get_valid_movements(self):
    """
    Function that returns all valid movements from current agent position, in a list, from current position.
    """
    valid_movements = []
    # Change in position
    if not (self.agent_coords[0] - 1 < 0):
      valid_movements.append( [[self.agent_coords[0]-1, self.agent_coords[1]], "UP"] )
    if not (self.agent_coords[1] - 1 < 0):
      valid_movements.append( [[self.agent_coords[0], self.agent_coords[1]-1], "LEFT"] )
    if not (self.agent_coords[0] + 1 >= len(self.display)):
      valid_movements.append( [[self.agent_coords[0]+1, self.agent_coords[1]], "DOWN"] )
    if not (self.agent_coords[1] + 1 >= len(self.display[0])):
      valid_movements.append( [[self.agent_coords[0], self.agent_coords[1]+1], "RIGHT"] )
    # Suck movement
    valid_movements.append(("S", "VACUUM!")) if self.display[self.agent_coords[0]][self.agent_coords[1]][0] == "D" else None
    return valid_movements


class SokobanState(State):
  def __init__(self, display, agent_coords):
    super().__init__(display, agent_coords)

  def get_possible_states(self):
    """
    Function that returns all possible states from this state.
    """
    possible_states = []
    return possible_states

  def get_valid_movements(self):
    """
    Function that returns all valid movements from current agent position, in a list, from current position.
    """
    valid_movements = []
    boxes_near_agent = self.get_boxes_near_agent()
    return valid_movements

  def get_boxes_near_agent(self):
    """
    Functions that checks if there is a box in any movable direction of the agent, i.e. UP, DOWN, LEFT, RIGHT.
    """
    boxes = {}
    boxes["UP"] = False
    boxes["DOWN"] = False
    boxes["LEFT"] = False
    boxes["RIGHT"] = False
    if not (self.agent_coords[0] - 1 < 0):
      if self.display[self.agent_coords[0]-1][self.agent_coords[1]] == "B":
        boxes["UP"] = True
    if not (self.agent_coords[1] - 1 < 0):
      if self.display[self.agent_coords[0]][self.agent_coords[1]-1] == "B":
        boxes["LEFT"] = True
    if not (self.agent_coords[0] + 1 >= len(self.display)):
      if self.display[self.agent_coords[0]+1][self.agent_coords[1]] == "B":
        boxes["DOWN"] = True
    if not (self.agent_coords[1] + 1 >= len(self.display[0])):
      if self.display[self.agent_coords[0]][self.agent_coords[1]+1] == "B":
        boxes["RIGHT"] = True
    return boxes