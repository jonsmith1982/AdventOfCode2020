#!/usr/bin/env python3

debug = 0
if debug:
  import time
  start = time.perf_counter()

with open("challenge-22-12-2020.txt","r") as f:
  puzzle_input = [x.strip() for x in f]

def part1(input):
  p1_cards = []
  p2_cards = []
  
  for x in range(1, 26):
    p1_cards.append(int(input[x]))
  for x in range(28, 53):
    p2_cards.append(int(input[x]))
    
  while (len(p1_cards) > 0 and len(p2_cards) > 0):
    a = p1_cards.pop(0)
    b = p2_cards.pop(0)
    if (a > b):
      p1_cards = p1_cards + [a, b]
    elif (b > a):
      p2_cards = p2_cards + [b, a]
    
  winner = p1_cards if len(p1_cards) > 0 else p2_cards
  total = 0
  for i in range(len(winner)):
    total += (len(winner) - i) * winner[i]
  
  return(total)

def part2(input):
  p1_cards = []
  p2_cards = []
  
  for x in range(1, 26):
    p1_cards.append(int(input[x]))
  for x in range(28, 53):
    p2_cards.append(int(input[x]))
  
  def new_game(p1_cards, p2_cards):
    previous_hands = set()
    while (len(p1_cards) > 0 and len(p2_cards) > 0):
      state = str((p1_cards, p2_cards))
      if (state in previous_hands):
        return(1, p1_cards)
      else :
        previous_hands.add(state)
      a = p1_cards.pop(0)
      b = p2_cards.pop(0)
      if (len(p1_cards) >= a and len(p2_cards) >= b):
        winner = new_game(p1_cards[:a], p2_cards[:b])[0]
        if (winner == 1):
          p1_cards = p1_cards + [a,b]
        elif (winner == 2):
          p2_cards = p2_cards + [b,a]
        else :
          return(0, p1_cards, p2_cards)
      elif (a > b):
        p1_cards = p1_cards + [a,b]
      elif (b > a):
        p2_cards = p2_cards + [b,a]
      else:
        return(0, p1_cards, p2_cards)
    return (1, p1_cards) if len(p1_cards) > 0 else (2, p2_cards)
  
  winner = new_game(p1_cards, p2_cards)[1]
  total = 0
  for i in range(len(winner)):
    total += (len(winner) - i) * winner[i]
  
  return(total)

print("PartI:", part1(puzzle_input))
print("PartII:",part2(puzzle_input))

if debug:
  end = time.perf_counter()
  print("Runtime: {:5.3f}".format(end-start))
    
