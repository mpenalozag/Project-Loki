from solver import create_solver
  


sliding_solver = create_solver("sliding", "game", "best_first", "manhattan_distance")
sliding_solver = create_solver("sliding", "game", "best_first", "euclidian_distance")

