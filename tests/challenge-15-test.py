challenge = __import__('challenge-15-12-2020')

puzzle_input = [9,12,1,4,17,0,18]

def test_part1():
  part1_result = challenge.part1(puzzle_input)
  assert part1_result == 610

def test_part2():
  part2_result = challenge.part2(puzzle_input)
  assert part2_result == 1407
