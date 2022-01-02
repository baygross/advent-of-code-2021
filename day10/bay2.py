def solve(lines):
  incomplete_points = []

  for line in lines:
    closes = []

    for c in range(len(line)):
      char = line[c]

      # process all open brackets
      if char == "[":
        closes.append("]") 
      if char == "(":
        closes.append(")") 
      if char == "{":
        closes.append("}") 
      if char == "<":
        closes.append(">") 

      # skip the corrup lines
      if char == "]" and closes.pop() != "]": break
      if char == ")" and closes.pop() != ")": break 
      if char == "}" and closes.pop() != "}": break
      if char == ">" and closes.pop() != ">": break

      # if end of line, see if incomplete
      if c == len(line)-1 and len(closes) > 0:
        
        # calculate points
        points = 0
        lookup = {")":1, "]":2, "}":3, ">":4}
        while len(closes) > 0:
          points = points * 5
          points += lookup[closes.pop()]
        incomplete_points.append(points)

  incomplete_points.sort()
  return incomplete_points[ int(len(incomplete_points)/2) ]

with open('input_bay.txt', 'r') as file:
  raw = list(map(list, file.read().splitlines()))
  print(solve(raw))