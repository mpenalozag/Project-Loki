class Node:
  """
    A node is created from a father and a state.
    If a node is root, the father is None.
    The state is an object of the class State.
    """
  def __init__(self, father, state):
    self.father = father
    self.childs = []
    self.state = state

  def expand(self):
    """
    Function that expands a node. Expanding a node means creating a child for each possible action.
    Returns a list of new nodes that result from expanding this node.
    """
    possible_states = self.state.get_possible_states()
    for state in possible_states:
      self.childs.append( Node(father=self, state=state) )
    return self.childs

  def get_solution_path(self):
    """
    Function that returns the path from the root to this node.
    """
    path = []
    node = self
    while node.father is not None:
      path.append(node.state.previous_move)
      node = node.father
    path.reverse()
    return path