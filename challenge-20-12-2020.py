#!/usr/bin/env python3

import re

debug = 0
if debug:
  import time
  start = time.perf_counter()

with open("challenge-20-12-2020.txt","r") as f:
  puzzle_input = [x.strip() for x in f]

def part1(input):
  tiles = dict()
  tile_list = []
  position = ''
  tiles_edges = dict()
  tiles_log = dict()

  def rotate_90(tile):
    rotated = []
    for x in [9,8,7,6,5,4,3,2,1,0]:
      row = []
      for y in [0,1,2,3,4,5,6,7,8,9]:
        row.append(tile[y][x])
      rotated.append(''.join(row))
    return(rotated)

  for x in input:
    if (re.search(':', x)):
      position = re.findall("(\d+)", x)[0]
      tile_list.append(position)
    elif (x == ''):
      continue
    else :
      if (position not in tiles):
        tiles[position] = []
      tiles[position].append(x)

  for x in range(len(tile_list)):
    if (tile_list[x] not in tiles_edges):
      tiles_edges[tile_list[x]] = []
    for y in range(4):
      row = tiles[tile_list[x]][0]
      tiles_edges[tile_list[x]].append(row)
      row = row[::-1]
      tiles_edges[tile_list[x]].append(row)
      tiles[tile_list[x]] = rotate_90(tiles[tile_list[x]])

  for x in tile_list:
    for y in tile_list:
      if (x == y):
        continue
      if (set(tiles_edges[x]).intersection(tiles_edges[y])):
        if (x not in tiles_log):
          tiles_log[x] = 0
        tiles_log[x] += 1

  total = 1

  for x in tile_list:
    if (tiles_log[x] == 2):
      total *= int(x)

  return(total)

def part2(input):

  return(1)

print("PartI:", part1(puzzle_input))
print("PartII:",part2(puzzle_input))

if debug:
  end = time.perf_counter()
  print("Runtime: {:5.3f}".format(end-start))
    
