# https://adventofcode.com/2020/day/2
# For example, suppose you have the following list:

data = """1-3 a: abcde
 1-3 b: cdefg
 2-9 c: ccccccccc"""

# Each line gives the password policy and then the password. 
# The password policy indicates the lowest and highest number of times a given 
# letter must appear for the password to be valid. For example, 1-3 a means that 
# the password must contain a at least 1 time and at most 3 times.

# In the above example, 2 passwords are valid. The middle password, cdefg, is not; 
# it contains no instances of b, but needs at least 1. 
# The first and third passwords are valid: they contain one a or nine c, both within 
# the limits of their respective policies.

# How many passwords are valid according to their policies?

# Part 2
# Each policy actually describes two positions in the password, where 1 means the 
# first character, 2 means the second character, and so on. (Be careful; 
# Toboggan Corporate Policies have no concept of "index zero"!) Exactly one of these positions 
# must contain the given letter. Other occurrences of the letter are irrelevant for the purposes of policy enforcement.

# Given the same example list from above:

# 1-3 a: abcde is valid: position 1 contains a and position 3 does not.
# 1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
# 2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c.
# How many passwords are valid according to the new interpretation of the policies?

debug = False

def pp(subject, name): #prints anything with a name as string 
    if debug or True:
        #print()
        print(name, ": ", subject)

print("\n----------------------------------")   # reading file
file = "advent_2020_ludwig/AOC20/data_aoc20_2.txt"

if not debug:
    with open(file) as f:
        data = f.read()
data = [s.split() for s in data.splitlines()]

valids = 0

for i in range(len(data)):
    data[i][0] = [int(x) for x in data[i][0].split("-")]

for i in range(len(data)):
    s = data[i]
    valid = False
    min, max = s[0]
    s[1] = s[1][0]
    count = s[2].count(s[1])
    if min <= count <= max:
        valid = True
        valids += 1

print("Part 1: The database contains ", valids, "valid passwords")

valids = 0
for i in range(len(data)):
    s = data[i]
    valid = False
    pos1, pos2 = s[0]
    key = s[1] = s[1][0]
    matches = 0
    for index, c in enumerate(s[2]):
        if c == key and index+1 == pos1:
            matches += 1
        if c == key and index+1 == pos2:
            matches += 1
    if matches == 1:
        valid = True
        valids += 1

print("Part 2: The database contains ", valids, "valid passwords")