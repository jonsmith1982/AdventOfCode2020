

debug = 0
if debug:
  import time
  start = time.perf_counter()

with open("challenge-09-12-2020.txt","r") as f:
  puzzle_input = [x.strip() for x in f]


def part1(input):
  fault = 0
  
  for i in range(25, len(input)):
    found = False
    target = int(input[i])
    preamble = range(i - 25, i)
    for x in preamble:
      a = int(input[x])
      for y in preamble:
        b = int(input[y])
        if (a == b):
          continue
        if (a + b == target):
          found = True
          break
      if (found == True):
        break
    if (found == False):
      fault = target
      break
    
  return(fault)

def part2(input):
  target = 15690279
  within = range(0, 499)
  combination = range(2, 100)
  found = False
  numbers = []
  
  def find_min_max(numbers):
    min = numbers[0]
    max = numbers[-1]
    for x in numbers:
      if (x > min):
        min = x
      if (x < max):
        max = x
    return(min + max)
  
  for i in within:
    for x in combination:
      total = 0
      numbers = []
      for y in range(i, i + x):
        total += int(input[y])
        numbers.append(int(input[y]))
      if (total == target):
        found = True
        break
    if (found == True):
      break
  
  min_max_total = find_min_max(numbers)
  
  return(min_max_total)

print("PartI:", part1(puzzle_input))
print("PartII:",part2(puzzle_input))

if debug:
  end = time.perf_counter()
  print("Runtime: {:5.3f}".format(end-start))
    
