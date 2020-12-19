#!/usr/bin/env python3

import re, string

debug = 0
if debug:
  import time
  start = time.perf_counter()

with open("challenge-19-12-2020.txt","r") as f:
  puzzle_input = [x.strip() for x in f]

def part1(input):
  all_rules = dict()
  
  def parse_rules(i, rules):
    rule = []
    if (isinstance(rules, list)):
      print(i, rules)
      for x in rules:
        #rule[i].append(x)
        next_rules = re.findall("(\d+)", x)
        for y in next_rules:
          rule.append(all_rules[y])
          parse_rules(y, all_rules[y])
    elif (isinstance(rules, str)):
      print(i, rules)
      return(rule)
  
  for i in range(139):
    rule = re.split(': ', input[i])
    if (re.search(re.escape("|"), rule[1])):
      rule[1] = re.split(re.escape(" | "), rule[1])
    elif (re.search("[0-9]", rule[1])):
      rule[1] = [rule[1]]
    all_rules[rule[0]] = rule[1]
    #break
  
  
  combinations = [parse_rules('0', all_rules['0'])]
  #print(all_rules['0'])
  print(combinations)
  
  return(1)

def part2(input):

  return(1)

print("PartI:", part1(puzzle_input))
#print("PartII:",part2(puzzle_input))

if debug:
  end = time.perf_counter()
  print("Runtime: {:5.3f}".format(end-start))
    
