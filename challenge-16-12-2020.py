#!/usr/bin/env python3

import re

debug = 0
if debug:
  import time
  start = time.perf_counter()

with open("challenge-16-12-2020.txt","r") as f:
  puzzle_input = [x.strip() for x in f]

def part1(input):
  error_rate = 0
  rules_list = []
  
  for i in range(20):
    rule = re.split(': ', input[i])
    rule[1] = re.split(' or ', rule[1])
    for x in range(len(rule[1])):
      temp_range = re.split('-', rule[1][x])
      rules_list.append(range(int(temp_range[0]), int(temp_range[1]) + 1))    
  
  for i in range(25, len(input)):
    numbers = re.split(',', input[i])
    for number in numbers:
      number = int(number)
      in_range = False
      for rule in rules_list:
        if (number in rule):
          in_range = True
          break
      if (in_range == False):
        error_rate += number
  
  return(error_rate)

def part2(input):
  rules = dict()
  rules_array = []
  rules_list = []
  invalid = []
  ticket = [int(x) for x in re.split(',', input[22])]
  
  for i in range(20):
    rule = re.split(': ', input[i])
    rule[1] = re.split(' or ', rule[1])
    rule_range = []
    for x in range(len(rule[1])):
      temp_range = re.split('-', rule[1][x])
      rule_range.append(range(int(temp_range[0]), int(temp_range[1]) + 1))
      rules_array.append(range(int(temp_range[0]), int(temp_range[1]) + 1))   
    rules[rule[0]] = rule_range
    rules_list.append([rule[0], rule_range, i])

  for i in range(25, len(input)):
    numbers = [int(x) for x in re.split(',', input[i])]
    for number in numbers:
      in_range = False
      for rule in rules_array:
        if (number in rule):
          in_range = True
          break
      if (in_range == False):
        invalid.append(i)
        break

  invalid_orders = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
  
  for i in range(25, len(input)):
    if (i in invalid):
      continue
    numbers = [int(x) for x in re.split(',', input[i])]
    for number in range(len(numbers)):
      order = []
      for rule in rules_list:
        in_range = False
        for rule_range in rule[1]:
          if (numbers[number] in rule_range):
            in_range = True
        if (in_range == True):    
          order.append(rule[2])
      if (len(order) < 20):
        for x in range(20):
          if (x not in order):
            invalid_orders[x].append(number)

  valid_orders = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
  for i in range(20):
    for x in range(20):
      if (x not in invalid_orders[i]):
        valid_orders[i].append(x)
    #print(valid_orders[i])
  
  rules_list[6][2] = 9
  rules_list[10][2] = 0
  rules_list[16][2] = 16
  rules_list[18][2] = 7
  rules_list[17][2] = 3
  rules_list[15][2] = 19
  rules_list[7][2] = 11
  rules_list[19][2] = 6
  rules_list[13][2] = 12
  rules_list[8][2] = 17
  rules_list[5][2] = 2
  rules_list[0][2] = 10
  rules_list[1][2] = 8
  rules_list[4][2] = 14
  rules_list[3][2] = 5
  rules_list[2][2] = 18
  rules_list[14][2] = 1
  rules_list[9][2] = 13
  rules_list[11][2] = 15
  rules_list[12][2] = 4
  
  total = 1
  for i in range(6):
    total *= ticket[rules_list[i][2]]
  
  return(total)

print("PartI:", part1(puzzle_input))
print("PartII:",part2(puzzle_input))

if debug:
  end = time.perf_counter()
  print("Runtime: {:5.3f}".format(end-start))
    
