import re, time

debug = 0
if debug: 
  start = time.perf_counter()

with open("challenge-08-12-2020.txt","r") as f:
  puzzle_input = [x.strip() for x in f]


def part1(input):
  history = []
  infinite_loop = False
  count = 0
  i = 0
  
  def parse_signed_int(signed_int):
    if (re.match('\+', signed_int)):
      operand = '+'
    else :
      operand = '-'
    [integer] = re.findall('\d+', signed_int)
    return([operand, int(integer)])
  
  while(infinite_loop == False):
    if (i in history or i > len(input)):
      infinite_loop = True
      continue
    history.append(i)
    
    next_code = input[i]
    [operation, signed_int] = re.split(' ', next_code)
    #print(operation)
    
    if (re.match('^acc', operation)):
      [operand, integer] = parse_signed_int(signed_int)
      #count =  signed_int +/- count  # define another function to parse signed_int
      [operand, integer] = parse_signed_int(signed_int)
      if (operand == '+'):
        count += integer
      else :
        count -= integer
      i += 1
    elif (re.match('^jmp', operation)):
      #i = signed_int +/- i # define another function to parse signed_int
      [operand, integer] = parse_signed_int(signed_int)
      if (operand == '+'):
        i += integer
      else :
        i -= integer
    else :
      i += 1
    
  return(count)

def part2(input):
  history = []
  infinite_loop = False
  count = 0
  i = 0
  now = time.time()
  
  def parse_signed_int(signed_int):
    if (re.match('\+', signed_int)):
      operand = '+'
    else :
      operand = '-'
    [integer] = re.findall('\d+', signed_int)
    return([operand, int(integer)])
  
  def copy_input(input):
    input_copy = input
    for x in range(160, len(input_copy)):
      if (re.match('^jmp', input_copy[x]) and x not in history):
        input_copy[x] = re.sub('^jmp', 'nop', input_copy[x])
        history.append(x)
        break
      x += 1
    return(input_copy)  
  
  input_copy = copy_input(input)
  
  while(infinite_loop == False):

    if (time.time() - now > 8 or i > len(input)):
      count = 0
      i = 0
      now = time.time()
      input_copy = copy_input(input)
      print(history[-1])
      
    
    next_code = input_copy[i]
    [operation, signed_int] = re.split(' ', next_code)
    
    if (re.match('^acc', operation)):
      [operand, integer] = parse_signed_int(signed_int)
      #count =  signed_int +/- count  # define another function to parse signed_int
      [operand, integer] = parse_signed_int(signed_int)
      if (operand == '+'):
        count += integer
      else :
        count -= integer
      i += 1
    elif (re.match('^jmp', operation)):
      #i = signed_int +/- i # define another function to parse signed_int
      [operand, integer] = parse_signed_int(signed_int)
      if (operand == '+'):
        i += integer
      else :
        i -= integer
    else :
      i += 1
    
    if (i == len(input)):
      infinite_loop = True
    
  return(count)

print("PartI:", part1(puzzle_input))
print("PartII:",part2(puzzle_input))

if debug:
  end = time.perf_counter()
  print("Runtime: {:5.3f}".format(end-start))
    
