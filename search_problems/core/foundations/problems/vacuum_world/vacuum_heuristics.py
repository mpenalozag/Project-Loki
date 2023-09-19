# For this problem we want to minimize the dirty cells, so we create the evaluation function.

class DirtyCellsHeuristic():
  def __init__(self):
    pass

  def __str__(self):
    return "Dirty Cells Heuristic"

  def __call__(self, state):
    count = 0
    for row in state.display:
      for element in row:
        if element == ["D", " "]:
          count += 1
    return count

class EuclidianDistanceToDirt():
  def __init__(self):
    pass

  def __str__(self):
    return "Euclidian Distance to Dirt"

  def __call__(self, state):
    aggregated_distance = 0
    x = 0
    y = 0
    for row in state.display:
      y = 0
      for element in row:
        if element == ["D", " "]:
          aggregated_distance += ((state.agent_coords[0] - x)**2 + (state.agent_coords[1] - y)**2)**0.5
        y += 1
      x += 1
    return aggregated_distance

def vacuum_heuristic_factory(name):
  heuristics = {
    "dirty_cells": DirtyCellsHeuristic,
    "euclidian_distance": EuclidianDistanceToDirt,
  }

  return heuristics[name]()