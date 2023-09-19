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



sokoban_problems = {
  "easy_1": {
    "init_agent_coords": [0, 3],
    "initial": [
      ["G", "B", " ", "A"],
      ["G", "B", " ", " "],
      ["G", "B", " ", " "],
      ["G", "B", " ", " "],
    ],
    "goals": generate_possible_goals([
      ["B", " ", " ", " "],
      ["B", " ", " ", " "],
      ["B", " ", " ", " "],
      ["B", " ", " ", " "],
    ])
  },
  "easy_2": {
    "init_agent_coords": [0, 0],
    "initial": [
      ["A", " ", "B", "G"],
      [" ", " ", "B", "G"],
      [" ", " ", "B", "G"],
      [" ", " ", "B", "G"],
    ],
    "goals": generate_possible_goals([
      [" ", " ", " ", "B"],
      [" ", " ", " ", "B"],
      [" ", " ", " ", "B"],
      [" ", " ", " ", "B"],
    ])
  }
}