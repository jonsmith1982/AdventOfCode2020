
numbers_array = []

f = open("challenge-01-12-2020.txt", "r")
for x in f:
  numbers_array.append(int(x.rstrip()))
f.close()

# Puzzle 1 - star coin 1
a = b = 0
for x in numbers_array:
  a = x
  for y in numbers_array:
    b = y
    c = a + b
    print(str(a) + ' + ' + str(b) + ' = ' + str(c))
    if (c == 2020):
      break
  if (a + b == 2020):
    break
print(str(a) + ' * ' + str(b) + ' = ' + str(a*b))

# Puzzle 1 - star coin 2
a = b = c = 0
for x in numbers_array:
  a = x
  for y in numbers_array:
    b = y
    for z in numbers_array:
      c = z
      d = a + b + c
      print(str(a) + ' + ' + str(b) + ' + ' + str(c) + ' = ' + str(d))
      if (d == 2020):
        break
    if (a + b + c == 2020):
      break
  if (a + b + c == 2020):
    break
print(str(a) + ' * ' + str(b) + ' * ' + str(c) + ' = ' + str(a*b*c))



