challenge = __import__('challenge-19-12-2020')

with open("challenge-19-12-2020.txt","r") as f:
  puzzle_input = [x.strip() for x in f]

def test_part1():
  part1_result = challenge.part1(puzzle_input)
  assert part1_result == 198

def test_part2():
  part2_result = challenge.part2(puzzle_input)
  assert part2_result == 372
