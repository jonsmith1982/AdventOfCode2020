import re

debug = 0
if debug:
  import time
  start = time.perf_counter()

with open("challenge-14-12-2020.txt","r") as f:
  puzzle_input = [x.strip() for x in f]

def part1(input):
  memory = dict()
  mask = ''
  
  #binary_out = f"{12:#038b}"
  #int_out = int(binary_out, 2)
  #print(int_out)
  
  for x in input:
    if (re.match('^mask', x)):
      mask = re.split(' = ', x)[1]
    elif (re.match('^mem', x)):
      data = re.findall('mem\[(\d+)\] \= (\d+)', x)[0]
      binary_data = int(data[1])
      memory_location = int(data[0])
      binary_data = f"{binary_data:#038b}"
      binary_data = list(binary_data)
      for i in range(0, len(mask)):
        if (mask[i] != 'X'):
          binary_data[i + 2] = mask[i]
      memory[memory_location] = int(''.join(binary_data), 2)
  
  return(sum(memory.values()))

def part2(input):
  memory = dict()
  mask = ''
  
  def get_addresses_string(from_main_address):
    addresses = []
    for i in range(len(from_main_address)):
      if from_main_address[i] == "X":
        addresses += get_addresses_string(from_main_address[:i] + "1" + from_main_address[i+1:])
        addresses += get_addresses_string(from_main_address[:i] + "0" + from_main_address[i + 1:])
        return addresses
    return [from_main_address]
  
  for x in input:
    if (re.match('^mask', x)):
      mask = re.split(' = ', x)[1]
    elif (re.match('^mem', x)):
      data = re.findall('mem\[(\d+)\] \= (\d+)', x)[0]
      value = int(data[1])
      memory_location = int(data[0])
      binary_data = f"{memory_location:#038b}"
      memory_locations = []
      binary_data = list(binary_data)
      for i in range(0, len(mask)):
        if (mask[i] != '0'):   
          binary_data[i + 2] = mask[i]
      
      memory_locations = get_addresses_string(''.join(binary_data))
      
      for y in memory_locations:
        memory[y] = value

  return(sum(memory.values()))

def test_part1(answer):
  part1_result = part1(puzzle_input)
  assert part1_result == 16003257187056

def test_part2(answer):
  part2_result = part2(puzzle_input)
  assert part2_result == 3219837697833

part1_result = part1(puzzle_input)
part2_result = part2(puzzle_input)
#print("PartI:", part1_result)
#test_part1(part1_result)
#print("PartII:",part2_result)
#test_part2(part2_result)

if debug:
  end = time.perf_counter()
  print("Runtime: {:5.3f}".format(end-start))
