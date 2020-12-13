import re

bags = ['shiny gold bag']
bags_copy = ['shiny gold bag']
count = 1


while (len(bags) != 0):
  for colour in bags:
    bags.remove(colour)
    #print(colour)
    f = open("challenge-07-12-2020.txt", "r")
    for x in f:
  
      x = x.rstrip()
      #print x
      if (re.match("\w*\s*\w+ \w+ bags contain.*\d+ " + colour, x)):
        split = re.split("s contain", x)
        if (split[0] not in bags_copy):
          bags_copy.append(split[0])
          #print(split[0])
          bags.append(split[0])
          count = count + 1
          #print x
    f.close()
    #print(bags)
  #print(count)


#print(bags_copy)
print(len(bags_copy) - 1)

#all_colours = dict()

#f = open("challenge-07-12-2020.txt", "r")
#for x in f:
  #x = x.rstrip()
  #split = re.split("s contain", x)
  #name = re.sub("\s", "_", split[0])
  #bag_colours = re.findall("\d+ \w*\s*\w+ \w+ bag", split[1])
  #if (len(bag_colours) == 0):
    #all_colours[name] = []
  #else :
    #all_colours[name] = bag_colours

#f.close()

current_levels = ['1 shiny gold bag']
remaining_levels = []
#next_levels = []
count = 0
all_levels = []
all_levels.append(['1 shiny gold bag'])

while (len(current_levels) != 0):
  for current_level in current_levels:
    
    
    colour = re.sub("\d+ ", "", current_level)
    amount = re.sub(" \w*\s*\w+ \w+ bag$", "", current_level)                 
    #name = re.sub("\s", "_", colour)
  
    #f = open("challenge-example-07-12-2020.txt", "r")
    f = open("challenge-07-12-2020.txt", "r")
    for x in f:
      x = x.rstrip()
      if (re.match(colour + 's contain', x)):

        split = re.split("s contain", x)
        #name = re.sub("\s", "_", split[0])
        next_levels = re.findall("\d+ \w*\s*\w+ \w+ bag", split[1])
        #print(next_levels)
        if (len(next_levels) != 0):
          #print('wtf')
          remaining_levels.append(next_levels)
          all_levels.append(next_levels)
          #print(colour, ' '.join(next_levels))
          for level in next_levels:
            level_amount = re.sub(" \w*\s*\w+ \w+ bag$", "", level)
            count += int(amount) * int(level_amount)
            #print(count)
    f.close()

    current_levels.pop(current_levels.index(current_level))
    print(remaining_levels)
  if (len(current_levels) == 0 and len(remaining_levels) > 0):
    current_levels = remaining_levels.pop(0)


print(count)
#print(current_levels)
#print(remaining_levels)
#print(len(all_levels))
print(all_levels)
