def solution1(raw):
  called_numbers = raw[0].split(",")

  bingo_boards = []
  raw = raw[2:]
  while len(raw) > 1:
    bingo_boards.append( [row.split() for row in raw[0:5]] )
    raw = raw[6:]

  for n in called_numbers:
    # mark off squares
    for board in bingo_boards:
      for row in board:
        for cid, col in enumerate(row):
          if col == n: 
            row[cid] = "X"
  
    # check for winners
    for board in bingo_boards: 
      for row in board: 
        if row[0] == row[1] == row[2] == row[3] == row[4] == "X": 
          return winner(board, n) 
      
      for c in range (5):
        if board[0][c] == board[1][c] == board[2][c] == board[3][c] == board[4][c] == "X":
          return winner(board, n) 
          
  return "nobody won"

def winner(board, n):
  sum = 0
  for row in board:
    for col in row:
      if col != "X": sum += int(col)
  return sum * int(n)

    


with open('input_bay.txt', 'r') as file:
  raw = list(map(str, file.read().splitlines()))
  print(solution1(raw))
