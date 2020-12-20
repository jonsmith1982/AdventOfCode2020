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
  routes = []
  
  def parse_rules(i, rules):
    routes_copy = routes
    #print(i, rules)
    if (isinstance(rules, list)):
      #routes.append(rules)
      for x, y in enumerate(rules):
        #print(x, y)
        for z in range(len(routes_copy)):
          if (x == 1):
            routes.append(re.sub(' *' + i + ' *', ' ' + y + ' ', routes_copy[z]))
          else :
            routes[z] = re.sub(' *' + i + ' *', ' ' + y + ' ', routes[z])
        #print(routes[z])
        ##rule[i].append(x)
        next_rules = re.findall("(\d+)", y)
        #all_rules['0'] = [re.sub(i, ' '.join(next_rules), z) for z in all_rules['0']]
        #print(all_rules['0'])
        for z in next_rules:
          #print(i,' - ', x, ' - ', y)
          #all_rules['0'] = re.sub(re.escape(str(i)), re.escape(str(y)), all_rules['0'])  
          #rule.append(all_rules[y])
          #print(rule)
          parse_rules(z, all_rules[z])
    elif (isinstance(rules, str)):
      for z in range(len(routes_copy)):
        routes[z] = re.sub(i, ' ' + rules + ' ', routes[z])
      #for route in routes:
        #print(route)
      #return(rule)
  
  for i in range(139):
    rule = re.split(': ', input[i])
    if (re.search(re.escape("|"), rule[1])):
      rule[1] = re.split(re.escape(" | "), rule[1])
    elif (re.search("[0-9]", rule[1])):
      rule[1] = [rule[1]]
    all_rules[rule[0]] = rule[1]
    #break
  
  routes.append(' '.join(all_rules['0']))
  combinations = [parse_rules('0', all_rules['0'])]
  for route in routes:
    print(route)
  #print(combinations)
  
  return(1)

def part2(input):

  return(1)

print("PartI:", part1(puzzle_input))
#print("PartII:",part2(puzzle_input))

if debug:
  end = time.perf_counter()
  print("Runtime: {:5.3f}".format(end-start))
    
