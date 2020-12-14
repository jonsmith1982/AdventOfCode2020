import challenge14

with open("challenge-14-12-2020.txt","r") as f:
  puzzle_input = [x.strip() for x in f]

def test_part1():
  part1_result = part1(puzzle_input)
  assert part1_result == 16003257187056

def test_part2():
  part2_result = part2(puzzle_input)
  assert part2_result == 3219837697833
