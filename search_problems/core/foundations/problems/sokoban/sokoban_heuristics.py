# For this problem we want to minimize the dirty cells, so we create the evaluation function.

class BoxesOutOfGoal():
  def __init__(self):
    pass

  def __str__(self):
    return "Boxes out of goal"

  def __call__(self, state):
    pass

class EuclidianDistanceToGoal():
  def __init__(self):
    pass

  def __str__(self):
    return "Euclidian Distance to Goal"

  def __call__(self, state):
    pass

def sokoban_heuristic_factory(name):
  heuristics = {
    "boxes_out_of_goal": BoxesOutOfGoal,
    "euclidian_distance": EuclidianDistanceToGoal,
  }

  return heuristics[name]()