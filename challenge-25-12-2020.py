#!/usr/bin/env python3

debug = 0
if debug:
  import time
  start = time.perf_counter()

def part1():
  
  data = [15113849, 4206373]
  i, loops, value, sn = 0, {x: None for x in data}, 1, 7
  while any([x is None for x in loops.values()]):
    value = (value * sn) % 20201227
    i += 1 
    if (value in data):
      loops[value] = i
  sn, val, value = [k for k in loops.keys() if k != value][0], value, 1
  for i in range(loops[val]):
    value = (value * sn) % 20201227
  return(value)

print("PartI:", part1())

if debug:
  end = time.perf_counter()
  print("Runtime: {:5.3f}".format(end-start))
    
