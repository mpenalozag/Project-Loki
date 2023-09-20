import time
from core.foundations.problem import problem_factory
from core.algorithm_factory import algorithm_factory
from core.foundations.problems.heuristic_factory import heuristic_factory

class Solver:
  def __init__(self, problem, algorithm, heuristic=None):
    self.problem = problem
    self.algorithm = algorithm
    self.heuristic = heuristic
    self.present_problem()
    self.set_algorithm_elements()
    self.solve()

  def present_problem(self):
    print()
    print("Initial State:") 
    self.problem.initial_state.print_self()
    print("Heuristic: ", self.heuristic)
    print("Algorithm: ", self.algorithm)
    print()

  def set_algorithm_elements(self):
    self.algorithm.problem = self.problem
    self.algorithm.heuristic = self.heuristic

  def solve(self):
    self.start_time = time.time()
    solution_node = self.algorithm.start()
    solution_path = solution_node.get_solution_path()
    self.end_time = time.time()
    print(f"Solution Found in {len(solution_path)} steps.")
    print(f"Time: {round(self.end_time - self.start_time, 4)} seconds")
    print(solution_path)
    solution_node.state.print_self()
    print()
    print()
    return solution_node

def create_solver(problem_type, name, algorithm, heuristic):
  created_problem = problem_factory(problem_type, name)
  algorithm = algorithm_factory(algorithm)
  chosen_heuristic = None
  if heuristic is not None:
    chosen_heuristic = heuristic_factory(problem_type, heuristic, created_problem.goal_state.display)
  solver = Solver(created_problem, algorithm, chosen_heuristic)
  return solver