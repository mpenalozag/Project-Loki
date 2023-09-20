# For this problem we want to minimize the dirty cells, so we create the evaluation function.

class BoxesOutOfGoal():
  def __init__(self, goal):
    self.goal = goal

  def get_goal_coords(self):
    goals = []
    row_index = 0
    for row in self.goal:
      column_index = 0
      for element in row:
        if element == "B":
          goals.append((row_index, column_index))
        column_index += 1
      row_index += 1
    return goals

  def __str__(self):
    return "Boxes out of goal"

  def __call__(self, state):
    count = 0
    goals_coords = self.get_goal_coords()
    for coord in goals_coords:
      if state.display[coord[0]][coord[1]] != "B":
        count += 1
    return count

class ManhattanDistanceToGoal():
  def __init__(self, goal):
    self.goal = goal

  def get_goal_coords(self):
    goals = []
    row_index = 0
    for row in self.goal:
      column_index = 0
      for element in row:
        if element == "B":
          goals.append((row_index, column_index))
        column_index += 1
      row_index += 1
    return goals

  def __str__(self):
    return "Manhattan Distance to Goal"

  def get_manhattan_distance(self, coord1, coord2):
    return abs(coord1[0] - coord2[0]) + abs(coord1[1] - coord2[1])

  def get_closest_goal(self, original_box_position):
    goals_coords = self.get_goal_coords()
    closest_goal = goals_coords[0]
    closest_distance = self.get_manhattan_distance(original_box_position, closest_goal)
    for coord in goals_coords:
      distance = self.get_manhattan_distance(original_box_position, coord)
      if distance < closest_distance:
        closest_distance = distance
        closest_goal = coord
    return closest_distance

  def __call__(self, state):
    total_distance = 0
    row_index = 0
    for row in state.display:
      column_index = 0
      for element in row:
        if element == "B":
          total_distance += self.get_closest_goal((row_index, column_index))
        column_index += 1
      row_index += 1
    return total_distance

class EuclidianDistanceToGoal():
  def __init__(self, goal):
    self.goal = goal

  def __str__(self):
    return "Euclidian Distance to Goal"

  def get_euclidian_distance(self, coord1, coord2):
    return ((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)**0.5

  def get_goal_coords(self):
    goals = []
    row_index = 0
    for row in self.goal:
      column_index = 0
      for element in row:
        if element == "B":
          goals.append((row_index, column_index))
        column_index += 1
      row_index += 1
    return goals

  def get_closest_goal(self, original_box_position):
    goals_coords = self.get_goal_coords()
    closest_goal = goals_coords[0]
    closest_distance = self.get_euclidian_distance(original_box_position, closest_goal)
    for coord in goals_coords:
      distance = self.get_euclidian_distance(original_box_position, coord)
      if distance < closest_distance:
        closest_distance = distance
        closest_goal = coord
    return closest_distance

  def __call__(self, state):
    total_distance = 0
    row_index = 0
    for row in state.display:
      column_index = 0
      for element in row:
        if element == "B":
          total_distance += self.get_closest_goal((row_index, column_index))
        column_index += 1
      row_index += 1
    return total_distance

def sokoban_heuristic_factory(name, goal):
  heuristics = {
    "boxes_out_of_goal": BoxesOutOfGoal,
    "euclidian_distance": EuclidianDistanceToGoal,
    "manhattan_distance": ManhattanDistanceToGoal,
  }

  return heuristics[name](goal)