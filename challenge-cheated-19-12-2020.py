import re

input_list = []
input_filename = "challenge-19-12-2020.txt"
part2 = True

switch = False
rules = {}
messages = []

with open(input_filename, 'r') as reader:
    for line in reader:
        if line == '\n':
            switch = True
        if not switch:
            temp_line = (str(line.rstrip())).replace('"', '').split(' ')
            rules[temp_line[0][:-1]] = temp_line[1:]
        else:
            messages.append(str(line.rstrip()))


def build_regex(r: str):
    global rules

    if rules[r][0] in "ab":
        return rules[r][0]
    rx = "("
    for this_rule in rules[r]:
        if this_rule == "|":
            rx += this_rule
        else:
            rx += build_regex(this_rule)
    rx += ")"
    return rx


my_regex = f"^{build_regex('0')}$"
counter_p1 = 0
for this_message in messages:
    if re.match(my_regex, this_message):
        counter_p1 += 1

rule42 = build_regex("42")
rule31 = build_regex("31")

counter_p2 = 0

for n in range(1, 5):  # 5 was determined by trial-and-error; any lower and we start losing matches.
    my_regex = f"^({rule42}+{rule42}{{{n}}}{rule31}{{{n}}})$"
    for this_message in messages:
        if re.match(my_regex, this_message):
            counter_p2 += 1

print(f"Part 1: {counter_p1}")
print(f"Part 2: {counter_p2}")
