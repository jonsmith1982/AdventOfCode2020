lines = 323
character = 1
row = 0
max_characters = 31
trees = 0

f = open("challenge-03-12-2020.txt", "r")
for x in f:
  
  x.rstrip()
  row = row + 1
  
  if (row == 1):
    continue
  
  if (row % 2 == 0): # Right 1 Down 2
    continue
  
  #character = character + 1 # Right 1 Down 1
  #character = character + 3 # Right 3 Down 1
  #character = character + 5 # Right 5 Down 1
  #character = character + 7 # Right 7 Down 1
  character = character + 1 # Right 1 Down 2
  
  
  
  if (character > max_characters):
    character = character - max_characters
  
  print(str(row) + ' : ' + str(character) + ' : ' + x[character - 1])
  
  if (x[character - 1] == '#'):
    trees = trees + 1

f.close()

# Right 1, down 1. 104
# Right 3, down 1. 230
# Right 5, down 1. 83
# Right 7, down 1. 98
# Right 1, down 2. 49

# 104 * 230 * 83 * 98 * 49 = 9533698720

print(trees)


