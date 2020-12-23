#!/usr/bin/env python3

debug = 1
if debug:
  import time
  start = time.perf_counter()

puzzle_input = [4,6,9,2,1,7,5,3,8]

def part1(input):
  current_index = 0
  
  for y in range(100):
    current_number = input[current_index]
    pickup_start = current_index + 1 if current_index + 1 < len(input) else 0
    pickup_stop = pickup_start + 3
    if (pickup_stop > len(input)):
      pickup_stop = pickup_stop - len(input)
      pickup = input[pickup_start:]
      pickup += input[:pickup_stop]
    else :
      pickup = input[pickup_start:pickup_stop]
    for x in pickup:
      input.remove(x)
    destination_number = current_number - 1
    while (destination_number not in input):
      destination_number = max(input) if destination_number < min(input) else destination_number - 1
    destination_index = input.index(destination_number) + 1
    for i in range(destination_index, destination_index + 3):
      input.insert(i, pickup[i - destination_index])
    current_index = input.index(current_number) + 1 if input.index(current_number) + 1 < len(input) else 0
      
  index = input.index(1)
  answer = input[index + 1:]
  answer += input[:index]
  
  return(answer)

def part2(n):
  s = '389125467'
  s = '469217538'
  cups = [int(x) for x in s]
  ext = [x for x in range(10, n+1)]
  cups += ext

  d = {}
  for i in range(len(cups)):
    if i == len(cups)-1:
      d[cups[i]] = cups[0]
    else:
      d[cups[i]] = cups[i+1]

  start = int(s[0])
  for i in range((n*10)+1):
    a = d[start]
    b = d[a]
    c = d[b]
    d[start] = d[c]
    put = start-1
    if put in [a,b,c] or put < 1:
      while put in [a,b,c] or put < 1:
        put -=1
        if put < 1:
          put = n
    d[c] = d[put]
    d[put] = a
    start = d[start]

  return d[1] * d[d[1]]


print("PartI:", part1(puzzle_input.copy()))
print("PartII:",part2(1000000))

if debug:
  end = time.perf_counter()
  print("Runtime: {:5.3f}".format(end-start))
    
