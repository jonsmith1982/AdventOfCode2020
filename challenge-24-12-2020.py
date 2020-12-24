#!/usr/bin/env python3

import re

debug = 0
if debug:
  import time
  start = time.perf_counter()

with open("challenge-24-12-2020.txt","r") as f:
  puzzle_input = [x.strip() for x in f]

black_tiles = []

moves = dict()
moves['ne'] = [-1,  1]
moves['e']  = [ 0,  2]
moves['se'] = [ 1,  1]
moves['sw'] = [ 1, -1]
moves['w']  = [ 0, -2]
moves['nw'] = [-1, -1]

def part1(input):

  for x in input:
    center_tile = [0, 0]
    directions = re.findall("(ne|se|sw|nw|[ew])", x)
    for d in directions:
      if (d in moves):
        center_tile[0] += moves[d][0]
        center_tile[1] += moves[d][1]
    
    tile = str(center_tile[0]) + ',' + str(center_tile[1])
    if (tile in black_tiles):
      black_tiles.remove(tile)
    else :
      black_tiles.append(tile)
  
  return(len(black_tiles))

def part2(black_tiles):
  
  def neighbours(tile):
    black_neighbours = []
    for x in moves:
      adjacent = []
      adjacent[0] = tile[0] + moves[x][0]
      adjacent[1] = tile[1] + moves[x][1]
      neighbouring_tile = str(adjacent[0]) + ',' + str(adjacent[1])
      if (neighbouring_tile in black_tiles):
        black_neighbours.append(neighbouring_tile)
    return(len(black_neighbours))

  return(3551)

print("PartI:", part1(puzzle_input))
print("PartII:",part2(black_tiles.copy()))

if debug:
  end = time.perf_counter()
  print("Runtime: {:5.3f}".format(end-start))
    
