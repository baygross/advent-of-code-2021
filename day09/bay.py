def solve(cave):
  nrows = len(cave)
  ncols = len(cave[0])
  low_points = []

  for r in range(nrows):
    for c in range(ncols):

      adjacents = []
      if r>0: adjacents.append(cave[r-1][c])
      if r<nrows-1: adjacents.append(cave[r+1][c])
      if c>0: adjacents.append(cave[r][c-1])
      if c<ncols-1: adjacents.append(cave[r][c+1])

      if min(adjacents)>cave[r][c]: 
        low_points.append(cave[r][c])

  print(len(low_points))
  print(sum(low_points)+len(low_points))

  

with open('input_bay.txt', 'r') as file:
  lines = []
  for line in file.read().splitlines():
    line = list(line)
    line = list(map(int, line))
    lines.append(line)
  solve(lines)