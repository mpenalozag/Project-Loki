import copy
from .algorithm import Algorithm
from .foundations.node import Node

class BestFirstSearch(Algorithm):
  def __init__(self):
    super().__init__()
    self.nodes_expanded = 0
    self.heuristic = None

  def __str__(self):
    return "Best First Search algorithm"

  def start(self):
    """
    Returns a solution node or failure.
    """
    node = Node(father=None, state=copy.deepcopy(self.problem.initial_state))
    frontier = [node]
    reached = [node.state]
    while len(frontier) != 0:
      node = frontier.pop(0)
      if self.problem.is_solution(node.state):
        return node
      self.nodes_expanded += 1
      for child in node.expand():
        if child.state not in reached:
          reached.append(child.state)
          self.insert_node_in_frontier(child, frontier)
    return False

  def insert_node_in_frontier(self, node, frontier):
    """
    Inserts a node in the frontier. The frontier is sorted by the heuristic value.
    So the first node in the frontier is the one with the lowest heuristic value.
    """
    frontier.append(node)
    index = len(frontier) - 2
    while index >= 0 and self.heuristic(frontier[index].state) > self.heuristic(frontier[index + 1].state):
      frontier[index], frontier[index + 1] = frontier[index + 1], frontier[index]
      index -= 1
