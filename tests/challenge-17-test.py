challenge = __import__('challenge-16-12-2020')

with open("challenge-16-12-2020.txt","r") as f:
  puzzle_input = [x.strip() for x in f]

def test_part1():
  part1_result = challenge.part1(puzzle_input)
  assert part1_result == 255

def test_part2():
  part2_result = challenge.part2(puzzle_input)
  assert part2_result == 2340
