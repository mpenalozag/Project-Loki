from solver import create_solver
  
#sokoban_solver = create_solver("sokoban", "easy_1", "bfs", None)
sokoban_solver = create_solver("sokoban", "game", "best_first", "boxes_out_of_goal")
sokoban_solver = create_solver("sokoban", "game", "best_first", "manhattan_distance")
