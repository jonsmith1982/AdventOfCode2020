
# puzzle 2 - star coiin 1
import re
correct = 0
f = open("challenge-02-12-2020.txt", "r")
for x in f:
  matches = re.split("(\d+)\-(\d+) (\w)\: (\w+)", x.rstrip())
  matches.pop(0)
  matches.pop(-1)
  #print(matches)
  policy = range(int(matches[0]), int(matches[1])+1)
  #print(policy)
  password = re.findall(matches[2], matches[3])
  if (len(password) in policy):
    #print(password)
    correct = correct + 1
f.close()
print(correct)

#puzzle 2 - star coin 2
correct = 0
f = open("challenge-02-12-2020.txt", "r")
for x in f:
  matches = re.split("(\d+)\-(\d+) (\w)\: (\w+)", x.rstrip())
  matches.pop(0)
  matches.pop(-1)
  #print(matches)
  password = matches[3]
  letter = matches[2]
  if (len(password) > int(matches[0]) and password[int(matches[0])-1] == letter ):
    if (len(password) >= int(matches[1]) and password[int(matches[1])-1] != letter):
      #print(password)
      correct = correct + 1
  elif (len(password) >= int(matches[1]) and password[int(matches[1])-1] == letter):
    #print(password)
    correct = correct + 1
f.close()
print(correct)