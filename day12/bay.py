def step(grid):

  return 0


with open('input_bay.txt', 'r') as file:
  lines = []
  for line in file.read().splitlines():
    line = list(line)
    line = list(map(int, line))
    lines.append(line)

