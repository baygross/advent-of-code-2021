def step(grid):
  nrows = len(grid)
  ncols = len(grid[0])
  flash_count = 0

  # first part of a step is adding 1 to every octopus
  for r in range(nrows):
    for c in range(ncols):
      grid[r][c] +=1

  # FLASH
  # now read through and flash everyone
  someone_flashed = True
  while (someone_flashed):
    
    someone_flashed = False
    for r in range(nrows):
      for c in range(ncols):

        if grid[r][c] >= 10:
          someone_flashed = True
          flash_count += 1
          grid[r][c]= -10000 #arbitrary and low

          if r>0 and c>0:             grid[r-1][c-1]  += 1
          if r>0:                     grid[r-1][c]    += 1
          if r>0 and c<ncols-1:       grid[r-1][c+1]  += 1
          if c>0:                     grid[r][c-1]    += 1
          if c<ncols-1:               grid[r][c+1]    += 1
          if r<ncols-1 and c>0:       grid[r+1][c-1]  += 1
          if r<ncols-1:               grid[r+1][c]    += 1
          if r<ncols-1 and c<ncols-1: grid[r+1][c+1]  += 1
  
  # Clean up
  # reset all the negatives to zero (they just flashed)
  for r in range(nrows):
    for c in range(ncols):
      if grid[r][c] < 0: 
        grid[r][c] = 0
  
  return flash_count


with open('input_bay.txt', 'r') as file:
  lines = []
  for line in file.read().splitlines():
    line = list(line)
    line = list(map(int, line))
    lines.append(line)

  # Solution 1
  #print(sum( step(lines) for i in range(100)) )

  # Solution 2
  steps = 0
  octopus_count = len(lines) * len(lines[0])
  while(True):
    steps+=1
    if step(lines) == octopus_count: break
  print(steps)


  ## DEBUG PRINT CODE
  # sum = 0 
  # for i in range(2):
  #   sum += step(lines)
  #   print("After stage: ", i+1)
  #   for l in lines: 
  #     print( *l )
  # print (sum)
    