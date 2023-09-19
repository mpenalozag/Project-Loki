import copy
from .algorithm import Algorithm
from .foundations.node import Node

class BFS(Algorithm):
  def __init__(self):
    super().__init__()
    self.nodes_expanded = 0

  def __str__(self):
    return "Breadth First Search algorithm"

  def start(self):
    node = Node(father=None, state=copy.deepcopy(self.problem.initial_state))
    frontier = [node]
    reached = [node.state]
    while len(frontier) != 0:
      node = frontier.pop(0)
      self.nodes_expanded += 1
      for child in node.expand():
        if self.problem.is_solution(child.state):
          return child
        if child.state not in reached:
          reached.append(child.state)
          frontier.append(child)
    return False