import re

# byr (Birth Year) - four digits; at least 1920 and at most 2002.
# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
# hgt (Height) - a number followed by either cm or in:
  # If cm, the number must be at least 150 and at most 193.
  # If in, the number must be at least 59 and at most 76.
# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
# pid (Passport ID) - a nine-digit number, including leading zeroes.
# cid (Country ID) - ignored, missing or not.

def validate_passport(a):
  if ('byr' in a and int(a['byr']) in range(1920, 2003)):
    if ('iyr' in a and int(a['iyr']) in range(2010, 2021)):
      if ('eyr' in a and int(a['eyr']) in range(2020, 2031)):
        if ('hgt' in a):
          height = re.split("^(\d{1,3})(cm|in)$", a['hgt'])
          if (len(height) == 4):
            height.pop(0)
            height.pop()
            if ((height[1] == 'cm' and int(height[0]) in range(150, 194)) or (height[1] == 'in' and int(height[0]) in range(59, 77))):
              if ('hcl' in a and re.match("^#[a-z0-9]{6}$", a['hcl'])):
                if ('ecl' in a and re.match("^(amb|blu|brn|gry|grn|hzl|oth)$", a['ecl'])):
                  if ('pid' in a and re.match("^\d{9}$", a['pid'])):
                    return 1
  return 0

passport = dict()
valid = 0

f = open("challenge-04-12-2020.txt", "r")
for x in f:
  
  x = x.rstrip()
  if  (len(x) == 0):
    # process passport if not empty then continue
    if (len(passport) == 8 or (len(passport) == 7 and 'cid' not in passport)):
      #print(len(passport))
      if (validate_passport(passport)):
        valid = valid + 1
    passport = dict()
    continue
  
  # add x to current passport dictionary
  matches = re.split("\s", x)
  for y in matches:
    item = re.split("\:", y)
    passport[item[0]] = item[1]
  
f.close()

print(valid)
