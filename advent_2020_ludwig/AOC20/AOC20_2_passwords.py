# https://adventofcode.com/2020/day/2

data = """1-3 a: abcde
 1-3 b: cdefg
 2-9 c: ccccccccc"""

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
    count = s[2].count(s[1]) # the trick is here
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