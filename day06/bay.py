def reproduce(fish):
  new_fish = []
  for fid in range(len(fish)):
    fish[fid] = fish[fid] - 1
    if fish[fid] == -1:
      fish[fid] = 6
      new_fish.append(8)
  return fish + new_fish

def reproduceHub(fishHub):
  carry_over = fishHub[0]
  fishHub = fishHub[1:]
  fishHub.append(carry_over)
  fishHub[6] += carry_over
  return fishHub

with open('input_bay.txt', 'r') as file:
  raw = list(map(str, file.read().splitlines()))
  fish=[int(f) for f in raw[0].split(",")]
  
  # Solution 1
  # for i in range(80):
  #   fish = reproduce(fish)
  #   print(i)
  # print(len(fish))

  #Solution 2
  fishHub = [0]*9
  for f in fish:
    fishHub[f] += 1

  for i in range(256):
    fishHub = reproduceHub(fishHub)
    print(i+1, fishHub)
  print(sum(fishHub))
  



