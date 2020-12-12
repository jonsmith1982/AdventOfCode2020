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
      #print(angle, amount)
      directions[compass[round(way_point)]] += amount
      
  #print(directions['n'], directions['s'], directions['e'], directions['w'])
  return((directions['s'] - directions['s']) + (directions['e'] - directions['w']))

def part2(input):
  waypoint = {'n': 1, 'e': 10, 's': 0, 'w': 0}
  position = {'n': 0, 'e': 0, 's': 0, 'w': 0}
  angle = 0
  compass = ['n', 'e', 's', 'w', 'n']
  compass_point = 0

  for x in input:
    next_instruction = re.findall('([FRLNSEW]{1})(\d+)' ,x)
    next_instruction = next_instruction[0]
    
    direction = next_instruction[0]
    amount = int(next_instruction[1])
    #print(next_instruction)

    if (direction == 'L'):
      previous_waypoint = [waypoint[compass[compass_point]], waypoint[compass[compass_point+1]]]
      previous_compass_point = compass_point
      angle -= amount
      if (angle < 0):
        angle += 360
      compass_point = int(angle / 90)
      waypoint[compass[compass_point]] = previous_waypoint[0]
      waypoint[compass[compass_point+1]] = previous_waypoint[1]
      if (previous_compass_point not in [compass_point, compass_point + 1]):
        waypoint[compass[previous_compass_point]] = 0
      if (previous_compass_point + 1 not in [compass_point, compass_point + 1]):
        waypoint[compass[previous_compass_point+1]] = 0
      
    elif (direction == 'R'):
      previous_waypoint = [waypoint[compass[compass_point]], waypoint[compass[compass_point+1]]]
      previous_compass_point = compass_point
      angle += amount
      if (angle >= 360):
        angle -= 360
      compass_point = int(angle / 90)
      waypoint[compass[compass_point]] = previous_waypoint[0]
      waypoint[compass[compass_point+1]] = previous_waypoint[1]
      if (previous_compass_point not in [compass_point, compass_point + 1]):
        waypoint[compass[previous_compass_point]] = 0
      if (previous_compass_point + 1 not in [compass_point, compass_point + 1]):
        waypoint[compass[previous_compass_point+1]] = 0
        
    elif (direction == 'N'):
      if (waypoint['s'] > 0 and waypoint['s'] > amount):
        waypoint['s'] = waypoint['s'] - amount
        waypoint['n'] = 0
      elif (waypoint['s'] > 0):
        waypoint['n'] = amount - waypoint['s']
        waypoint['s'] = 0
        if (waypoint['e'] > 0):
          compass_point = 0
        else :
          compass_point = 3
      else :
        waypoint['n'] += amount
      
    elif (direction == 'S'):
      if (waypoint['n'] > 0 and waypoint['n'] > amount):
        waypoint['n'] = waypoint['n'] - amount
        waypoint['s'] = 0
      elif (waypoint['n'] > 0):
        waypoint['s'] = amount - waypoint['n']
        waypoint['n'] = 0
        if (waypoint['e'] > 0):
          compass_point = 1
        else :
          compass_point = 2
      else :
        waypoint['s'] += amount
      
    elif (direction == 'E'):
      if (waypoint['w'] > 0 and waypoint['w'] > amount):
        waypoint['w'] = waypoint['w'] - amount
        waypoint['e'] = 0
      elif (waypoint['w'] > 0):
        waypoint['e'] = amount - waypoint['w']
        waypoint['w'] = 0
        if (waypoint['s'] > 0):
          compass_point = 2
        else :
          compass_point = 0
      else :
        waypoint['e'] += amount
      
    elif (direction == 'W'):
      if (waypoint['e'] > 0 and waypoint['e'] > amount):
        waypoint['e'] = waypoint['e'] - amount
        waypoint['w'] = 0
      elif (waypoint['e'] > 0):
        waypoint['w'] = amount - waypoint['e']
        waypoint['e'] = 0
        if (waypoint['s'] > 0):
          compass_point = 2
        else :
          compass_point = 3
      else :
        waypoint['w'] += amount
      
    elif (direction == 'F'):
      for point in waypoint:
        position[point] = position[point] + (waypoint[point] * amount)
      #print('position', position)
    
    #print(waypoint, amount)
  
  #print(position['s'], position['n'], position['e'], position['w'])
  return((position['s'] - position['n']) + (position['e'] - position['w']))

print("PartI:", part1(puzzle_input))
print("PartII:",part2(puzzle_input))

if debug:
  end = time.perf_counter()
  print("Runtime: {:5.3f}".format(end-start))
    
