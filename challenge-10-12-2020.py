

debug = 0
if debug:
  import time
  start = time.perf_counter()

with open("challenge-10-12-2020.txt","r") as f:
  puzzle_input = [int(x.strip()) for x in f]


def part1(input):
  count_1_diff = 0
  count_2_diff = 0
  count_3_diff = 1
  
  current_rating = 0
  
  input.sort()
  
  for i in range(0, len(input)):
    if (current_rating + 1 == input[i]):
      count_1_diff += 1
    elif (current_rating + 2 == input[i]):
      count_2_diff += 1
    elif (current_rating + 3 == input[i]):
      count_3_diff += 1
    else :
      return(0)
    current_rating = input[i]
  
  #print(input)
  return(count_1_diff * count_3_diff)

def part2(input):
  
  input.sort()
  
  cache = [0,0,1] + [0] * input[-1]
  for a in input:
    # a=1 corresponds to cache[3], so +2
    i = a + 2
    cache[i] = sum(cache[i-3:i])

  return(cache[-1])

print("PartI:", part1(puzzle_input))
print("PartII:",part2(puzzle_input))

if debug:
  end = time.perf_counter()
  print("Runtime: {:5.3f}".format(end-start))
    
