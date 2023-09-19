import copy

def generate_possible_goals(goal):
  goals = []
  row_index = 0
  for row in goal:
    column_index = 0
    for column in row:
      if column == " ":
        new_goal = copy.deepcopy(goal)
        new_goal[row_index][column_index] = "A"
        goals.append(new_goal)
      column_index += 1
    row_index += 1
  return goals

goal = [
      [" ", " ", " "],
      [" ", " ", "B"],
      [" ", " ", " "]
    ]

sokoban_problems = {
  "easy_1": {
    "init_agent_coords": [0, 0],
    "initial": [
      ["A", " ", " "],
      [" ", "B", "G"],
      [" ", " ", " "]
    ],
    "goals": generate_possible_goals([
      [" ", " ", " "],
      [" ", " ", "B"],
      [" ", " ", " "]
    ])
  }
}