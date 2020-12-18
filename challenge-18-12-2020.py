#!/usr/bin/env python3

import re

debug = 0
if debug:
  import time
  start = time.perf_counter()

with open("challenge-18-12-2020.txt","r") as f:
  puzzle_input = [x.strip() for x in f]

def part1(input):
  count = 0
  
  def deparentise(string):
    stack = []
    for i, c in enumerate(string):
      if c == '(':
        stack.append(i)
      elif c == ')' and stack:
        start = stack.pop()
        yield(string[start + 1: i])

  #string = '(9 * 3 + 4) * (7 + (2 + 3 + 6 * 2) + 3) * 4 * 5'
  #string = '2 * 3 + (4 * 5)' # 26
  #string = '5 + (8 * 3 + 9 + 3 * 4 * 3)' # 437
  #string = '5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))' # 12240
  #string = '((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2' # 13632

  for x in input:

    while (len(list(deparentise(x))) > 0):
      original = s = list(deparentise(x))[0]
      while (re.search("[\+\-\*\/]", s)):
        equation = re.findall("(\d+)\s*([\+\-\/\*])\s*(\d+)", s)
        sum_string = ' '.join(equation[0])
        equals = eval(sum_string)
        s = re.sub(re.escape(sum_string), str(equals), s)
      x = re.sub("\(" + re.escape(original) + "\)", str(s), x)
  
    while (re.search("[\+\-\*\/]", x)):
      s = x
      equation = re.findall("(\d+)\s*([\+\-\/\*])\s*(\d+)", s)
      sum_string = ' '.join(equation[0])
      equals = eval(sum_string)
      x = re.sub(re.escape(sum_string), str(equals), x)
    
    print(x)
    count += int(x)
  
  return(count) # 3348222486398

def part2(input):

  return(43423343619505)

print("PartI:", part1(puzzle_input))
#print("PartII:",part2(puzzle_input))

if debug:
  end = time.perf_counter()
  print("Runtime: {:5.3f}".format(end-start))
    
