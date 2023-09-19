from .best_first_search import BestFirstSearch
from .bfs import BFS

def algorithm_factory(algorithm_name):
  algorithms = {
    "best_first": BestFirstSearch,
    "bfs": BFS,
  }

  return algorithms[algorithm_name]()