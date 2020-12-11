
debug = 0
if debug:
  import time
  start = time.perf_counter()

with open("challenge-11-12-2020.txt","r") as f:
  puzzle_input = [x.strip() for x in f]


def part1(current_model):
  equal_passes = 0
  current_previous_model = []
  
  while equal_passes < 15:

    new_copy = []
    
    for x in range(0, len(current_model)):
      current_line = list(current_model[x])
      for y in range(0, len(current_model[x])):
        occupied_seat_count = 0
        for z in [[-1,-1], [-1,0], [-1,1], [0,-1], [0,1], [1,-1], [1,0], [1,1]]:
          if (x + z[0] >= 0 and x + z[0] < len(current_model) and y + z[1] >= 0 and y + z[1] < len(current_model[x])):
            if (current_model[x + z[0]][y + z[1]] == '#'):
              occupied_seat_count += 1
        if (str(current_model[x][y]) == 'L' and occupied_seat_count == 0):
          current_line[y] = '#'
        elif (str(current_model[x][y]) == '#' and occupied_seat_count >= 4):
          current_line[y] = 'L'
      new_copy.append(current_line)
    current_model = new_copy

    if (current_model == current_previous_model):
      equal_passes += 1
    elif (equal_passes > 0):
      equal_passes = 0
      current_previous_model = current_model
    else :
      current_previous_model = current_model
  
  occupied_seats = 0
  
  for x in current_model:
    occupied_seats += x.count('#')
  
  return(occupied_seats)

def part2(current_model):
  equal_passes = 0
  current_previous_model = []
  
  while equal_passes < 15:

    new_copy = []
    
    for x in range(0, len(current_model)):
      current_line = list(current_model[x])
      for y in range(0, len(current_model[x])):
        
        occupied_seat_count = 0
        
        for z in range(1, len(current_model)):
          if (x - z >= 0 and y - z >= 0):
            if (current_model[x - z][y - z] == '#'):
              occupied_seat_count += 1
              break
            elif (current_model[x - z][y - z] == 'L'):
              break
          else :
            break
        
        for z in range(1, len(current_model)):
          if (x - z >= 0):
            if (current_model[x - z][y] == '#'):
              occupied_seat_count += 1
              break
            elif (current_model[x - z][y] == 'L'):
              break
          else :
            break
        
        for z in range(1, len(current_model)):
          if (x - z >= 0 and y + z < len(current_model[x])):
            if (current_model[x - z][y + z] == '#'):
              occupied_seat_count += 1
              break
            elif (current_model[x - z][y + z] == 'L'):
              break
          else :
            break
        
        for z in range(1, len(current_model)):
          if (y - z >= 0):
            if (current_model[x][y - z] == '#'):
              occupied_seat_count += 1
              break
            elif (current_model[x][y - z] == 'L'):
              break
          else :
            break
        
        for z in range(1, len(current_model)):
          if (y + z < len(current_model[x])):
            if (current_model[x][y + z] == '#'):
              occupied_seat_count += 1
              break
            elif (current_model[x][y + z] == 'L'):
              break
          else :
            break
        
        for z in range(1, len(current_model)):
          if (x + z < len(current_model) and y - z >= 0):
            if (current_model[x + z][y - z] == '#'):
              occupied_seat_count += 1
              break
            elif (current_model[x + z][y - z] == 'L'):
              break
          else :
            break
        
        for z in range(1, len(current_model)):
          if (x + z < len(current_model)):
            if (current_model[x + z][y] == '#'):
              occupied_seat_count += 1
              break
            elif (current_model[x + z][y] == 'L'):
              break
          else :
            break
        
        for z in range(1, len(current_model)):
          if (x + z < len(current_model) and y + z < len(current_model[x])):
            if (current_model[x + z][y + z] == '#'):
              occupied_seat_count += 1
              break
            elif (current_model[x + z][y + z] == 'L'):
              break
          else :
            break

        if (str(current_model[x][y]) == 'L' and occupied_seat_count == 0):
          current_line[y] = '#'
        elif (str(current_model[x][y]) == '#' and occupied_seat_count >= 5):
          current_line[y] = 'L'
      new_copy.append(current_line)
    current_model = new_copy

    if (current_model == current_previous_model):
      equal_passes += 1
    elif (equal_passes > 0):
      equal_passes = 0
      current_previous_model = current_model
    else :
      current_previous_model = current_model
  
  occupied_seats = 0
  
  for x in current_model:
    occupied_seats += x.count('#')
  
  return(occupied_seats)

print("PartI:", part1(puzzle_input))
print("PartII:",part2(puzzle_input))

if debug:
  end = time.perf_counter()
  print("Runtime: {:5.3f}".format(end-start))
    
