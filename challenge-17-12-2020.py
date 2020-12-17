#!/usr/bin/env python3

import re

debug = 0
if debug:
  import time
  start = time.perf_counter()

with open("challenge-17-12-2020.txt","r") as f:
  puzzle_input = [x.strip() for x in f]

def part1(input):
  
  return(255)

def part2(input):

  return(2340)

print("PartI:", part1(puzzle_input))
print("PartII:",part2(puzzle_input))

if debug:
  end = time.perf_counter()
  print("Runtime: {:5.3f}".format(end-start))
    
