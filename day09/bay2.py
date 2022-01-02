def solve(cave):
  nrows = len(cave)
  ncols = len(cave[0])
  basins = []

  for r in range(nrows):
    for c in range(ncols):

      adjacents = []
      if r>0: adjacents.append(cave[r-1][c])
      if r<nrows-1: adjacents.append(cave[r+1][c])
      if c>0: adjacents.append(cave[r][c-1])
      if c<ncols-1: adjacents.append(cave[r][c+1])

      # If we find a low point, start painting!
      if min(adjacents)>cave[r][c]: 
        paintBasin(cave, r, c)
        basins.append( countBasin(cave) )

  product = 1
  basins.sort()
  for b in basins[-3:]:
    product = product * b
  print (product)

# recursive painting function
def paintBasin(cave, r, c):
  cave[r][c]="A"

  if r>0 and cave[r-1][c] not in [9, "A"]:
    paintBasin(cave, r-1, c)
  if r<len(cave)-1 and cave[r+1][c] not in [9, "A"]:
    paintBasin(cave, r+1, c)
  if c>0 and cave[r][c-1] not in [9, "A"]:
    paintBasin(cave, r, c-1)
  if c<len(cave[0])-1 and cave[r][c+1] not in [9, "A"]:
    paintBasin(cave, r, c+1)  


# count the number of "A"s in the basin, overwrite with 9s
def countBasin(cave):
  nrows = len(cave)
  ncols = len(cave[0])
  basin_size = 0
  for r in range(nrows):
    for c in range(ncols):
      if cave[r][c]=="A":
        cave[r][c]=9
        basin_size +=1
  return basin_size



with open('input_bay.txt', 'r') as file:
  lines = []
  for line in file.read().splitlines():
    line = list(line)
    line = list(map(int, line))
    lines.append(line)
  solve(lines)