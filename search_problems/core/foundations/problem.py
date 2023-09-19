from .state import *
from .problems.sliding_puzzle.sliding_problems import *
from .problems.vacuum_world.vacuum_problems import *

class Problem:
  """
  A problem is defined by an initial state and a goal state. 
  """
  def __init__(self, problem):
    self.instantiate_problem(problem)

  def instantiate_problem(self, problem):
    pass

  def is_solution(self, state):
    return state.display == self.goal_state.display

class SlidingProblem(Problem):
  def __init__(self, chosen_problem):
    self.problem = sliding_problems[chosen_problem]
    super().__init__(chosen_problem)

  def instantiate_problem(self, problem):
    self.initial_state = SlidingState(self.problem["initial"], self.problem["init_agent_coords"])
    self.goal_state = SlidingState(self.problem["goal"], None)

class VacuumProblem(Problem):
  def __init__(self, chosen_problem):
    self.problem = vacuum_problems[chosen_problem]
    super().__init__(chosen_problem)

  def instantiate_problem(self, chosen_problem):
    self.initial_state = VacuumState(self.problem["initial"], self.problem["init_agent_coords"])
    self.goal_state = VacuumState(self.problem["goal"], None)

def problem_factory(name, chosen):
  problems = {
    "sliding": SlidingProblem,
    "vacuum": VacuumProblem,
  }
  return problems[name](chosen)