def solve(lines):
  mistake_points = 0

  for line in lines:
    closes = []

    for char in line:

      if char == "[":
        closes.append("]") 
      if char == "(":
        closes.append(")") 
      if char == "{":
        closes.append("}") 
      if char == "<":
        closes.append(">") 

      expected = closes[-1]
      if char == "]" and closes.pop() != "]":
        print("%s  \tExpected %s, but found %s instead." % (''.join(line), expected, char)) 
        mistake_points += 57
        break
      if char == ")" and closes.pop() != ")":
        print("%s  \tExpected %s, but found %s instead." % (''.join(line), expected, char)) 
        mistake_points += 3
        break 
      if char == "}" and closes.pop() != "}": 
        print("%s  \tExpected %s, but found %s instead." % (''.join(line), expected, char)) 
        mistake_points += 1197
        break
      if char == ">" and closes.pop() != ">": 
        print("%s  \tExpected %s, but found %s instead." % (''.join(line), expected, char)) 
        mistake_points += 25137
        break
  return mistake_points
  

with open('input_bay.txt', 'r') as file:
  raw = list(map(list, file.read().splitlines()))
  print(solve(raw))