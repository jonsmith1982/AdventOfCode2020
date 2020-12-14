challenge = __import__('challenge-14-12-2020')

def test_part1():
  part1_result = challenge.part1(puzzle_input)
  assert part1_result == 16003257187056

def test_part2():
  part2_result = challenge.part2(puzzle_input)
  assert part2_result == 3219837697833
