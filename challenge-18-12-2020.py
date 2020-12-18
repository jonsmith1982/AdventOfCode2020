#!/usr/bin/env python3

import re

debug = 0
if debug:
  import time
  start = time.perf_counter()

with open("challenge-18-12-2020.txt","r") as f:
  puzzle_input = [x.strip() for x in f]

def part1(input):
  
  def deparentise(string):
    stack = []
    for i, c in enumerate(string):
      if c == '(':
        stack.append(i)
      elif c == ')' and stack:
        start = stack.pop()
        if (re.match('[\(\)]', string[start + 1: i])):
          deparentise(string[start + 1: i])
        else :
          yield (len(stack), string[start + 1: i])

  string = '(9 * 3 + 4) * (7 + (2 + 3 + 6 * 2) + 3) * 4 * 5'
  sum_of = list(deparentise(string))
  print(sum_of)
  
  for i, s in enumerate(sum_of):
    if (re.match('[\(\)]', s[1])):
      print(list(deparentise(s[1])))

  #while (re.match('[\(\)]', string)):
    #breakdown.append(deparentise(string))
  
  return(3348222486398)

def part2(input):

  return(43423343619505)

print("PartI:", part1(puzzle_input))
#print("PartII:",part2(puzzle_input))

if debug:
  end = time.perf_counter()
  print("Runtime: {:5.3f}".format(end-start))
    
