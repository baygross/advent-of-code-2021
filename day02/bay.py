def solution1(raw):
  depth = 0
  distance = 0
  for line in raw:
    steer, d = line.split()
    d = int(d)
    if steer == "forward":
        distance += d
    if steer == "up":
        depth -= d
    if steer == "down":
        depth += d
  return depth * distance
    


def solution2(raw):
  depth = 0
  distance = 0
  aim = 0
  for line in raw:
    steer, d = line.split()
    d = int(d)
    if steer == "forward":
        distance += d
        depth += (aim * d)
    if steer == "up":
        aim -= d
    if steer == "down":
        aim += d
  return depth * distance


with open('input_bay.txt', 'r') as file:
  raw = file.readlines()
  print(solution1(raw))
  print(solution2(raw))
