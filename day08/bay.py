def solve(input, output):
  mapping = [""]*10
  input.sort(key=len)

  ## Identify the ones w/ unique segment counts
  mapping[1]=input[0]
  mapping[7]=input[1]
  mapping[4]=input[2]
  mapping[8]=input[9]

  ## Identify the ones w/ 6 segment counts
  # we can use 4 to get 9
  # we can use 7 to get 0
  # then the last one is 6
  for code in input:
    if len(code)==6:
      if subsetCheck(mapping[4], code):
        mapping[9] = code 
      elif subsetCheck(mapping[7], code):
        mapping[0] = code 
      else:
         mapping[6] = code 
      
  ## Identify the ones w/ 5 segment counts
  # we can use 1 to get 3
  # then 5 is in 9
  # last option is 2
  for code in input:
      if len(code)==5:
        if subsetCheck(mapping[1], code):
          mapping[3] = code 
        elif subsetCheck(code, mapping[9]):
          mapping[5] = code 
        else:
          mapping[2] = code 

  ## At this point all the mappings have codes. 
  # Let's now solve for the output code
  # casting as a string to do easy digit concatenation
  result = ""
  for code in output:
    for i, key in enumerate(mapping):
      if samesetCheck(code, key):
        result += str(i)
  return int(result)



# determine if all letters in subset appear in fullset
def subsetCheck(sub, full):
  return (set(sub) & set(full) == set(sub))

# determine if all letters in subset appear in fullset
def samesetCheck(a, b):
  return set(a) == set(b)


with open('input_bay.txt', 'r') as file:
  raw = list(map(str, file.read().splitlines()))
  inputs = [ r.split("|")[0].split() for r in raw ]
  outputs = [ r.split("|")[1].split() for r in raw ]
  
  print("Part one:")
  print(sum( len(x) in {2, 3, 4, 7} for row in outputs for x in row))

  print("Part two:")
  total = 0
  for i in range(len(inputs)):
    total += solve(inputs[i], outputs[i])
  print(total)