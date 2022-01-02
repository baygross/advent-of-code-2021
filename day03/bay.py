def solution1(raw):
  num_lines = len(raw)
  num_digits = len(raw[0])
  digit_counts_arr = [0]*num_digits

  for line in raw:
    for digit in range(0, num_digits):
        digit_counts_arr[digit] += int(line[digit])

  gamma = ""
  epsilon = ""

  for i in range(num_digits):
    if digit_counts_arr[i] >= num_lines/2:
      gamma += "1"
      epsilon += "0"
    else: 
      gamma += "0"
      epsilon += "1"
  
  gamma = int(gamma,2)
  epsilon = int(epsilon,2)

  return gamma * epsilon
    
    
def solution2(rows):
  rows_backup=rows[:] #copy

  di = 0
  while (di<12):
    print (len(rows))
    if sum( map(lambda row: int(row[di]), rows)) >= len(rows)/2:
      rows = list(filter(lambda row: row[di] == "1", rows))
    else: 
      rows = list(filter(lambda row: row[di] == "0", rows))
    di = di+1
    if len(rows) == 1: break 
  o_rating = rows[0]
  
  rows=rows_backup
  di = 0
  while (di<12):
    print (len(rows))
    if sum( map(lambda row: int(row[di]), rows)) >= len(rows)/2:
      rows = list(filter(lambda row: row[di] == "0", rows))
    else: 
      rows = list(filter(lambda row: row[di] == "1", rows))
    di = di+1
    if len(rows) == 1: break 
  c_rating = rows[0]

  o_rating = int(o_rating,2)
  c_rating = int(c_rating,2)
  return o_rating * c_rating



with open('input_bay.txt', 'r') as file:
  raw = list(map(str, file.read().splitlines()))
  print(solution1(raw))
  print(solution2(raw))
