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
    valid_movements = self.get_valid_movements()
    for movement in valid_movements:
      new_display = copy.deepcopy(self.display)
      if movement[1] in "UP/LEFT/DOWN/RIGHT":
        new_display[self.agent_coords[0]][self.agent_coords[1]] = " "
        new_display[movement[0][0]][movement[0][1]] = "A"
        new_state = SokobanState(new_display, movement[0])
        possible_states.append(new_state)
      elif movement[1] == "PUSH UP":
        new_display[self.agent_coords[0]][self.agent_coords[1]] = " "
        new_display[movement[0][0]][movement[0][1]] = "A"
        new_display[movement[0][0]-1][movement[0][1]] = "B"
        new_state = SokobanState(new_display, movement[0])
        possible_states.append(new_state)
      elif movement[1] == "PUSH LEFT":
        new_display[self.agent_coords[0]][self.agent_coords[1]] = " "
        new_display[movement[0][0]][movement[0][1]] = "A"
        new_display[movement[0][0]][movement[0][1]-1] = "B"
        new_state = SokobanState(new_display, movement[0])
        possible_states.append(new_state)
      elif movement[1] == "PUSH DOWN":
        new_display[self.agent_coords[0]][self.agent_coords[1]] = " "
        new_display[movement[0][0]][movement[0][1]] = "A"
        new_display[movement[0][0]+1][movement[0][1]] = "B"
        new_state = SokobanState(new_display, movement[0])
        possible_states.append(new_state)
      elif movement[1] == "PUSH RIGHT":
        new_display[self.agent_coords[0]][self.agent_coords[1]] = " "
        new_display[movement[0][0]][movement[0][1]] = "A"
        new_display[movement[0][0]][movement[0][1]+1] = "B"
        new_state = SokobanState(new_display, movement[0])
        possible_states.append(new_state)
      new_state.previous_move = movement[1]
    return possible_states

  def get_valid_movements(self):
    """
    Function that returns all valid movements from current agent position, in a list, from current position.
    """
    valid_movements = []
    # Change in position with no box nearby.
    if not (self.agent_coords[0] - 1 < 0) and self.display[self.agent_coords[0]-1][self.agent_coords[1]] != "B":
      valid_movements.append( [[self.agent_coords[0]-1, self.agent_coords[1]], "UP"] )
    if not (self.agent_coords[1] - 1 < 0) and self.display[self.agent_coords[0]][self.agent_coords[1]-1] != "B":
      valid_movements.append( [[self.agent_coords[0], self.agent_coords[1]-1], "LEFT"] )
    if not (self.agent_coords[0] + 1 >= len(self.display)) and self.display[self.agent_coords[0]+1][self.agent_coords[1]] != "B":
      valid_movements.append( [[self.agent_coords[0]+1, self.agent_coords[1]], "DOWN"] )
    if not (self.agent_coords[1] + 1 >= len(self.display[0])) and self.display[self.agent_coords[0]][self.agent_coords[1]+1] != "B":
      valid_movements.append( [[self.agent_coords[0], self.agent_coords[1]+1], "RIGHT"] )

    # Change in position with box nearby.
    if not (self.agent_coords[0] - 2 < 0) and self.display[self.agent_coords[0]-1][self.agent_coords[1]] == "B" and self.display[self.agent_coords[0]-2][self.agent_coords[1]] != "B":
      valid_movements.append( [[self.agent_coords[0]-1, self.agent_coords[1]], " PUSH UP"] )
    if not (self.agent_coords[1] - 2 < 0) and self.display[self.agent_coords[0]][self.agent_coords[1]-1] == "B" and self.display[self.agent_coords[0]][self.agent_coords[1]-2] != "B":
      valid_movements.append( [[self.agent_coords[0], self.agent_coords[1]-1], "PUSH LEFT"] )
    if not (self.agent_coords[0] + 2 >= len(self.display)) and self.display[self.agent_coords[0]+1][self.agent_coords[1]] == "B" and self.display[self.agent_coords[0]+2][self.agent_coords[1]] != "B":
      valid_movements.append( [[self.agent_coords[0]+1, self.agent_coords[1]], "PUSH DOWN"] )
    if not (self.agent_coords[1] + 2 >= len(self.display[0])) and self.display[self.agent_coords[0]][self.agent_coords[1]+1] == "B" and self.display[self.agent_coords[0]][self.agent_coords[1]+2] != "B":
      valid_movements.append( [[self.agent_coords[0], self.agent_coords[1]+1], "PUSH RIGHT"] )
  
    return valid_movements