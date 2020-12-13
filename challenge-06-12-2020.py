
# challenge 06 - star coin 1

count = 0
questions = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

f = open("challenge-06-12-2020.txt", "r")
for x in f:
  
  x = x.rstrip()
  if  (len(x) == 0):
    # process questionaire per group here
    count = count + (26 - len(questions))
    questions = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    continue
  
  for y in x:
    if (y in questions):
      questions.remove(y)
  
f.close()

print(count)

# challenge 06 - star coin 2

count = 0
questions = dict()
people = 0

f = open("challenge-06-12-2020.txt", "r")
for x in f:
  
  x = x.rstrip()
  if  (len(x) == 0):
    # process questionaire per group here
    for q in questions:
      if (questions[q] == people):
        count = count + 1
    questions = dict()
    people = 0
    continue
  
  for y in x:
    if (y in questions):
      questions[y] = questions[y] + 1
    else :
      questions[y] = 1
  
  people = people + 1
  
f.close()

print(count)
