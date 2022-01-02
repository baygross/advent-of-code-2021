def solve(crabs):
  fuel = 0

  while (True):
    crabs.sort() 

    # when front is same as back, we are done!
    if crabs[0]==crabs[-1]: break

    # find the weighted center
    mid = sum(crabs)/len(crabs)

    # then decide which crab is farthest away
    lower_delta = mid-crabs[0]
    upper_delta = crabs[-1]-mid
 
    # then step that crab closer
    # originally I stepped 1 step at time, but was too slow
    # so now just doing a meaningfully larger but safe step
    # overstepping will cause problems
    step = int((upper_delta + lower_delta)/5) #rounds down
    if step==0: step = 1

    # make the step
    if (lower_delta>upper_delta):
      crabs[0]+=step
    else:
      crabs[-1]-=step
    fuel += step

  print(crabs[0], fuel)


def solveB(crabs):
  fuel = 0
  crabs_fuel = [1]*len(crabs)

  while (True):
    front_crab = min(crabs)
    back_crab = max(crabs)  
    
    # when front is same as back, we are done!
    if front_crab==back_crab: break

    # now instead of moving the farthest, we move the cheapest
    # with the important caveat that if we move one crab we are 
    # signing up to move all other crabs at that position
    front_crab_cost = 0
    back_crab_cost = 0

    # count cost of moving back or front
    for c in range(len(crabs)):
      if crabs[c] == front_crab:
        front_crab_cost += crabs_fuel[c]
      if crabs[c] == back_crab:
        back_crab_cost += crabs_fuel[c]
      
    # depending on which one is cheaper.. do it!
    if front_crab_cost < back_crab_cost:
      # move em all up
      for c in range(len(crabs)):
        if crabs[c] == front_crab:
          crabs[c]+=1
          fuel += crabs_fuel[c]
          crabs_fuel[c] += 1
    else:
        # move em all back
      for c in range(len(crabs)):
        if crabs[c] == back_crab:
          crabs[c]-=1
          fuel += crabs_fuel[c]
          crabs_fuel[c] += 1
    
    #print( front_crab, back_crab, front_crab_cost, back_crab_cost, fuel)
  
  # done
  print(crabs[0], fuel)



with open('input_bay.txt', 'r') as file:
  raw = list(map(str, file.read().splitlines()))
  crabs = list(map(int, raw[0].split(",")))
  solve(crabs)
  solveB(crabs)
