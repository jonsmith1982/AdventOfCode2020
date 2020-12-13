import re, math

debug = 0
if debug:
  import time
  start = time.perf_counter()

with open("challenge-13-12-2020.txt","r") as f:
  puzzle_input = [x.strip() for x in f]


def part1(input):
  timestamp = int(input[0])
  bus_ids = re.findall("\d+", input[1])
  
  lowest_wait = 0
  lowest_wait_bus_id = 0
  
  for x in bus_ids:
    x = int(x)
    result = (int(math.ceil(timestamp / x)) * x) - timestamp
    if (lowest_wait == 0 or result < lowest_wait):
      lowest_wait = result
      lowest_wait_bus_id = x
  
  return(lowest_wait * lowest_wait_bus_id)

def part2(input):
  schedule = re.split(",", input[1])
  bus_ids = re.findall("\d+", input[1])
  
  equal_occurrances = []
  
  for id in bus_ids:
    minutes = schedule.index(id)
    index = bus_ids.index(id)
    id = int(id)
    timestamp = id + minutes
    #result = 775230782877242
    #print(id, minutes, result / timestamp)
    if (minutes == len(bus_ids) - 1):
        break
    for multiplier in range(1025437543400, 33705686212100):
      total = timestamp + (id * multiplier)
      for i in range(index + 1, len(bus_ids)):
        bus_id = int(bus_ids[i])
        bus_minutes = schedule.index(bus_ids[i])
        bus_timestamp = bus_id + minutes
        bus_multiplier = int(math.floor((total - bus_minutes) / bus_id)) - 1
        while (total > bus_timestamp + (bus_id * bus_multiplier)):
          bus_multiplier += 1
          if (total == bus_timestamp + (bus_id * bus_multiplier)):
            equal_occurrances.append(total)
            
  # 775230782877242
  return(equal_occurrances.sort())

print("PartI:", part1(puzzle_input))
print("PartII:",part2(puzzle_input))

if debug:
  end = time.perf_counter()
  print("Runtime: {:5.3f}".format(end-start))
    
