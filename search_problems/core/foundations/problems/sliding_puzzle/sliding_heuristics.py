import random
from .sliding_problems import *

class ManhattanDistance():
  def __init__(self, goal):
    self.goal = goal

  def __str__(self):
    return "Manhattan Distance Heuristic"

  def manhattan_distance(self, p1, p2):
    # return manhattan distance
    return (abs(p1[0] - p2[0]) + abs(p1[1] - p2[1]))

  def get_element_coords(self, element, state):
    x = 0
    y = 0
    for row in state.display:
      y = 0
      for e in row:
        if e == element:
          return (x, y)
        y += 1
      x += 1

  def __call__(self, state):
    aggregated_distance = 0
    x = 0
    y = 0
    for row in state.display:
      y = 0
      for element in row:
        if element != self.goal[x][y]:
          aggregated_distance += self.manhattan_distance((x, y), self.get_element_coords(self.goal[x][y], state))
        y += 1
      x += 1
    return aggregated_distance


class EuclidianDistance():
  def __init__(self, goal):
    self.goal = goal

  def __str__(self):
    return "Euclidian Distance Heuristic"

  def euclidian_distance(self, p1, p2):
    return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**(1/2)

  def get_element_coords(self, element, state):
    x = 0
    y = 0
    for row in state.display:
      y = 0
      for e in row:
        if e == element:
          return (x, y)
        y += 1
      x += 1

  def __call__(self, state):
    aggregated_distance = 0
    x = 0
    y = 0
    for row in state.display:
      y = 0
      for element in row:
        if element != self.goal[x][y]:
          aggregated_distance += self.euclidian_distance((x, y), self.get_element_coords(self.goal[x][y], state))
        y += 1
      x += 1
    return aggregated_distance


def sliding_heuristic_factory(name, goal):
  heuristics = {
    "manhattan_distance": ManhattanDistance,
    "euclidian_distance": EuclidianDistance,
  }

  return heuristics[name](goal)