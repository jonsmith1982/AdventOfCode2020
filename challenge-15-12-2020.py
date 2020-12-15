#!/usr/bin/env python3

debug = 0
if debug:
  import time
  start = time.perf_counter()

puzzle_input = [9,12,1,4,17,0,18]
#puzzle_input = [3,1,2]

def part1(input):
  numbers = input

  def list_rindex(li, x):
    for i in reversed(range(len(li)-1)):
        if li[i] == x:
            return i
    raise ValueError("{} is not in list".format(x))

  for i in range(len(numbers) - 1, 2019):
    last_number = numbers[i]
    if (last_number not in numbers[:-1]):
      numbers.append(0)
    else :
      index = list_rindex(numbers, last_number)
      number = i - index
      numbers.append(number)
  
  #print(numbers)
  return(numbers[-1])

def part2(input):
  numbers = dict([(y,x+1) for (x,y) in enumerate(input[:len(input)-1])])
  last = input[-1]
  
  for turn in range(len(input),30000000):
    if last in numbers:
        nxt = turn - numbers[last]
        numbers[last] = turn
        last = nxt
    else:
        numbers[last] = turn
        last = 0
  
  return(last)

print("PartI:", part1(puzzle_input))
print("PartII:",part2(puzzle_input))

if debug:
  end = time.perf_counter()
  print("Runtime: {:5.3f}".format(end-start))
    
