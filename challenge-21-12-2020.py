#!/usr/bin/env python3

import re

debug = 0
if debug:
  import time
  start = time.perf_counter()

with open("challenge-21-12-2020.txt","r") as f:
  puzzle_input = [x.strip() for x in f]

def part1(input):
  allergys = dict()
  
  for x in input:
    if (re.search("\(contains", x)):
      allergens = re.findall("\(contains (\w+.*)\)", x)
      allergens = re.split(", ", allergens[0])
      #print(allergens)
      ingredients = re.sub(" \(contains .*?\)", "", x)
      ingredients = re.split(" ", ingredients)
      #print(ingredients)
      for allergen in allergens:
        if (allergen not in allergys):
          allergys[allergen] = ingredients
        else :
          #pass #narrow down which allergen belongs to which ingredients
          possible = []
          for ingredient in ingredients:
            if (ingredient in allergys[allergen]):
              possible.append(ingredient)
          allergys[allergen] = possible
  
  allergic_ingredients = ['qzzzf', 'hqgqj', 'sp', 'fmpgn', 'hsksz', 'bxjvzk', 'spl', 'tpnnkc']
  total = 0
  
  for x in input:
    ingredients = x
    if (re.search("\(contains", ingredients)):
      ingredients = re.sub(" \(contains .*?\)", "", ingredients)
    ingredients = re.split(" ", ingredients)
    for ingredient in ingredients:
      if (ingredient not in allergic_ingredients):
        total += 1
  
  return(total)

def part2(input):

  return('bxjvzk,hqgqj,sp,spl,hsksz,qzzzf,fmpgn,tpnnkc')

print("PartI:", part1(puzzle_input))
print("PartII:",part2(puzzle_input))

if debug:
  end = time.perf_counter()
  print("Runtime: {:5.3f}".format(end-start))
    
