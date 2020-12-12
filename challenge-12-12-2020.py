import re

debug = 0
if debug:
  import time
  start = time.perf_counter()

with open("challenge-12-12-2020.txt","r") as f:
  puzzle_input = [x.strip() for x in f]


def part1(input):
  directions = {'n': 0, 'e': 0, 's': 0, 'w': 0}
  angle = 90
  compass = ['n', 'e', 's', 'w', 'n']

  for x in input:
    next_instruction = re.findall('([FRLNSEW]{1})(\d+)' ,x)
    next_instruction = next_instruction[0]
    
    direction = next_instruction[0]
    amount = int(next_instruction[1])
    
    if (direction == 'L'):
      angle -= amount
      if (angle < 0):
        angle += 360
    elif (direction == 'R'):
      angle += amount
      if (angle >= 360):
        angle -= 360
    elif (direction == 'N'):
      directions['n'] += amount
    elif (direction == 'S'):
      directions['s'] += amount
    elif (direction == 'E'):
      directions['e'] += amount
    elif (direction == 'W'):
      directions['w'] += amount
    elif (direction == 'F'):
      way_point = angle / 90
      directions[compass[round(way_point)]] += amount
      
  return((directions['s'] - directions['n']) + (directions['w'] - directions['e']))

def part2(input):
  waypoint = {'n': 1, 'e': 10, 's': 0, 'w': 0}
  position = {'n': 0, 'e': 0, 's': 0, 'w': 0}
  compass = ['n', 'e', 's', 'w', 'n']

  for x in input:
    next_instruction = re.findall('([FRLNSEW]{1})(\d+)' ,x)
    next_instruction = next_instruction[0]
    
    direction = next_instruction[0]
    amount = int(next_instruction[1])

    if (direction == 'L'):
      while (amount > 0):
        waypoint_copy = waypoint.copy()
        amount -= 90
        waypoint['n'] = waypoint_copy['e']
        waypoint['e'] = waypoint_copy['s']
        waypoint['s'] = waypoint_copy['w']
        waypoint['w'] = waypoint_copy['n']
      
    elif (direction == 'R'):
      while (amount > 0):
        waypoint_copy = waypoint.copy()
        amount -= 90
        waypoint['n'] = waypoint_copy['w']
        waypoint['e'] = waypoint_copy['n']
        waypoint['s'] = waypoint_copy['e']
        waypoint['w'] = waypoint_copy['s']
        
    elif (direction == 'N'):
      if (waypoint['s'] > 0 and waypoint['s'] > amount):
        waypoint['s'] = waypoint['s'] - amount
        waypoint['n'] = 0
      elif (waypoint['s'] > 0):
        waypoint['n'] = amount - waypoint['s']
        waypoint['s'] = 0
      else :
        waypoint['n'] += amount
      
    elif (direction == 'S'):
      if (waypoint['n'] > 0 and waypoint['n'] > amount):
        waypoint['n'] = waypoint['n'] - amount
        waypoint['s'] = 0
      elif (waypoint['n'] > 0):
        waypoint['s'] = amount - waypoint['n']
        waypoint['n'] = 0
      else :
        waypoint['s'] += amount
      
    elif (direction == 'E'):
      if (waypoint['w'] > 0 and waypoint['w'] > amount):
        waypoint['w'] = waypoint['w'] - amount
        waypoint['e'] = 0
      elif (waypoint['w'] > 0):
        waypoint['e'] = amount - waypoint['w']
        waypoint['w'] = 0
      else :
        waypoint['e'] += amount
      
    elif (direction == 'W'):
      if (waypoint['e'] > 0 and waypoint['e'] > amount):
        waypoint['e'] = waypoint['e'] - amount
        waypoint['w'] = 0
      elif (waypoint['e'] > 0):
        waypoint['w'] = amount - waypoint['e']
        waypoint['e'] = 0
      else :
        waypoint['w'] += amount
      
    elif (direction == 'F'):
      for point in waypoint:
        position[point] += (waypoint[point] * amount)    
  
  return((position['s'] - position['n']) + (position['e'] - position['w']))

print("PartI:", part1(puzzle_input))
print("PartII:",part2(puzzle_input))

if debug:
  end = time.perf_counter()
  print("Runtime: {:5.3f}".format(end-start))
    
