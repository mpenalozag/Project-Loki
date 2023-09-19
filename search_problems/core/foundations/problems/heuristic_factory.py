from .sliding_puzzle.sliding_heuristics import sliding_heuristic_factory
from .vacuum_world.vacuum_heuristics import vacuum_heuristic_factory

def heuristic_factory(problem, name, goal):
  heuristics = {
    "sliding": {
      "manhattan_distance": sliding_heuristic_factory("manhattan_distance", goal),
      "euclidian_distance": sliding_heuristic_factory("euclidian_distance", goal)
    },
    "vacuum": {
      "dirty_cells": vacuum_heuristic_factory("dirty_cells"),
      "euclidian_distance": vacuum_heuristic_factory("euclidian_distance")
    }
  }
  return heuristics[problem][name]