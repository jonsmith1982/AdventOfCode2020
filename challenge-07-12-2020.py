import re

bags = ['shiny gold bag']
bags_copy = ['shiny gold bag']
count = 1


while (len(bags) != 0):
  for colour in bags:
    bags.remove(colour)
    print(colour)
    f = open("challenge-07-12-2020.txt", "r")
    for x in f:
  
      x = x.rstrip()
      #print x
      if (re.match("\w*\s*\w+ \w+ bags contain.*\d+ " + colour, x)):
        split = re.split("s contain", x)
        if (split[0] not in bags_copy):
	  bags_copy.append(split[0])
	  print(split[0])
          bags.append(split[0])
          count = count + 1
          #print x
    f.close()
    #print(bags)
  #print(count)


print(bags_copy)
print(len(bags_copy) - 1)


#all_levels = ['shiny gold bag']
#next_level = ['1 shiny gold bag']
#previous_levels = []
#next_levels = []
#bag_count = dict({'shiny_gold_bag': 1})

#current_branch = [0]

#level_number = 0

#total_count = 0



#while (len(next_level) != 0):
  #for current_level in next_level:
    #current_colour = re.sub("\d+ ", "", current_level)
    ##if (current_colour in all_levels):
      ##break
    #current_colour_count = re.sub(" \w*\s*\w+ \w+ bag$", "", current_level)
    #print(current_level)
    #f = open("challenge-07-12-2020.txt", "r")
    #for x in f:
  
      #x = x.rstrip()
      #if (re.match(current_colour + "s contain", x)):
        #print(x)#bags = ['shiny gold bag']
#bags_copy = ['shiny gold bag']
#count = 1


#while (len(bags) != 0):
  #for colour in bags:
    #bags.remove(colour)
    #print(colour)
    #f = open("challenge-07-12-2020.txt", "r")
    #for x in f:
  
      #x = x.rstrip()
      ##print x
      #if (re.match("\w*\s*\w+ \w+ bags contain.*\d+ " + colour, x)):
        #split = re.split("s contain", x)
        #if (split[0] not in bags_copy):
	  #bags_copy.append(split[0])
	  #print(split[0])
          #bags.append(split[0])
          #count = count + 1
          ##print x
    #f.close()
    ##print(bags)
  ##print(count)


#print(bags_copy)
#print(len(bags_copy) - 1)
        #bag_colours = re.findall("\d+ \w*\s*\w+ \w+ bag", x)
        #if (len(bag_colours) == 0):
          
          ## do calculations here i think - do it backwards
          
          #break # maybe this is wrong
        #else :
          #next_levels.append(bag_colours)
          #for bag_colour in bag_colours:
            ##print(bag_colour)
            #single = re.sub("\d+ ", "", bag_colour)
            #count = re.sub(" \w*\s*\w+ \w+ bag$", "", bag_colour)        
            
            #name = re.sub("\s", "_", single)
            
            #if (name in bag_count):
              #bag_count[name] = bag_count[name] + (int(current_colour_count) * int(count))
            #else :
              #bag_count[name] = int(current_colour_count) * int(count)
            
            #if (single not in all_levels):
              #all_levels.append(single)
    #f.close()
    #previous_levels.append(current_level)
    #next_level.remove(current_level)
    #total_count = total_count
    #print("\n")
  #if (len(next_level) == 0 and len(next_levels) > 0):
    #next_level = next_levels.pop(0)
    #level_number = level_number + 1

#print(bag_count)

all_colours = dict()

f = open("challenge-07-12-2020.txt", "r")
for x in f:
  x = x.rstrip()
  split = re.split("s contain", x)
  name = re.sub("\s", "_", split[0])
  bag_colours = re.findall("\d+ \w*\s*\w+ \w+ bag", split[1])
  if (len(bag_colours) == 0):
    all_colours[name] = []
  else :
    all_colours[name] = bag_colours

f.close()

all_levels = ['1 shiny gold bag']
current_levels = ['1 shiny gold bag']
next_levels = []
current_branch = []
finished = 0

index = 1

branched = []

level = 1;
  
for current_level in current_levels:
  print(current_level)
  colour = re.sub("\d+ ", "", current_level)
  amount = re.sub(" \w*\s*\w+ \w+ bag$", "", current_level)                 
  name = re.sub("\s", "_", colour)
  
  next_levels = all_colours[name]
  
  if (len(next_levels) != 0):
    level = level + 1
    if (len(next_levels) != 1):
      branched.append(index)
    for levels in next_levels:
      current_levels.append(levels)
      index = index + 1
    print(next_levels)
  else :
    print(branched)
    print("Completed line\n")


#print(current_levels)

