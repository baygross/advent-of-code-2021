bmap = []
def game(coords):
  for i in range(1000):
    bmap.append(["."]*1000)
  
  for i in range(len(coords)):
    coords[i]=[ coord.split(",") for coord in coords[i].split(" -> ")]
    coords[i][0][0] = int(coords[i][0][0])
    coords[i][0][1] = int(coords[i][0][1])
    coords[i][1][0] = int(coords[i][1][0])
    coords[i][1][1] = int(coords[i][1][1])

  for statement in coords:
    coorda = statement[0]
    coordb = statement[1]

    if coorda[0]==coordb[0]:
      drawRow(coorda[0], coorda[1], coordb[1])
    elif coorda[1]==coordb[1]:
      drawCol(coorda[1], coorda[0], coordb[0])
    else:
      drawDiag(coorda[0], coorda[1], coordb[0], coordb[1])
  
  sum = 0
  for r in bmap:
    for c in r:
      if c != "." and c >= 2:
        sum = sum + 1
  
  return sum


def drawCol (col, rowa, rowb):  
  if rowa < rowb:
    s = rowa
    f = rowb
  else: 
    s = rowb
    f = rowa

  for r in range(s,f+1):
    if bmap[r][col] == ".":
      bmap[r][col] = 1
    else: 
      bmap[r][col] = bmap[r][col] + 1

def drawRow (row, cola, colb):
  if cola < colb:
    s = cola
    f = colb
  else: 
    s = colb
    f = cola

  for c in range(s,f+1):
    if bmap[row][c] == ".":
      bmap[row][c] = 1
    else: 
      bmap[row][c] = bmap[row][c] + 1

def drawDiag (rowa, cola, rowb, colb):

  rstep = 1
  if rowa > rowb: rstep = -1
  cstep = 1
  if cola > colb: cstep = -1

  ridx = rowa
  cidx = cola

  while (ridx != rowb): #won't handle last step..
    if bmap[ridx][cidx] == ".":
      bmap[ridx][cidx] = 1
    else: 
      bmap[ridx][cidx] = bmap[ridx][cidx] + 1
    ridx = ridx + rstep
    cidx = cidx + cstep

  #sloppy but re-run here once due to exit conditions
  if bmap[ridx][cidx] == ".":
      bmap[ridx][cidx] = 1
  else: 
      bmap[ridx][cidx] = bmap[ridx][cidx] + 1


with open('input_bay.txt', 'r') as file:
  raw = list(map(str, file.read().splitlines()))
  print(game(raw))
