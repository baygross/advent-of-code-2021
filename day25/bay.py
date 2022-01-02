def move(ocean):
  nrows = len(ocean)
  ncols = len(ocean[0])
  move_count = 0
  made_move = True

  # kick off our main game engine loop
  while (made_move == True):
    made_move = False
    move_count += 1

    # Log the loop
    #print("After ", move_count, " steps: ")
    #for row in ocean: print(row) 

    ## Move the eastern'ers
    # prep all free moves, hold spot with e/E
    for r in range(nrows):
      for c in range(ncols):   
        if ocean[r][c] == ">":
          if ocean[r][(c+1)%ncols] == ".":
            ocean[r][c] = "e"
            ocean[r][(c+1)%ncols] = "E"
            made_move = True  
    # now go make those emoves
    for r in range(nrows):
      for c in range(ncols):
        if ocean[r][c] == "e":
          ocean[r][c] = "."
        if ocean[r][c] == "E":
          ocean[r][c] = ">"


    ## Move the southern'ers
    # prep all free moves, hold spot with S
    for r in range(nrows):
      for c in range(ncols):   
        if ocean[r][c] == "v":
          if ocean[(r+1)%nrows][c] == ".":
            ocean[r][c] = "s"
            ocean[(r+1)%nrows][c] = "S"
            made_move = True
    # now go make those emoves
    for r in range(nrows):
      for c in range(ncols):
        if ocean[r][c] == "s":
          ocean[r][c] = "."
        if ocean[r][c] == "S":
          ocean[r][c] = "v"

  print(move_count)
    

with open('input_bay.txt', 'r') as file:
  ocean = list(map(list, file.read().splitlines()))
  move(ocean)