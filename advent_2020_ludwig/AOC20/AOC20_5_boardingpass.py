# https://adventofcode.com/2020/day/5

data = """BFFFBBFRRR
FFFBBBFRRR
BBFFBBFRLL
"""

import operator

debug = False 
printit = True
def pp(subject, name): #prints anything with a name as string 
    if debug or printit:
        #print()
        print(name, ": ", subject)

print("\n----------------------------------")   # reading file

file = "advent_2020_ludwig/AOC20/data_aoc20_5.txt"
if not debug:
    with open(file) as f:
        data = f.read()
data = [s for s in data.splitlines()]

#pp(data, "data")

def h(x):
    return x//2
    
max = 128
register = [[i] for i in data]
#print(register)

for rowindex, b in enumerate(data):
    row = [s for s in range(128)]
    col = [s for s in range(8)]
    seatid = row * 8 + col
    for c in b:
        x = len(row)
        y = len(col)
        if x >= 1:
            if c == "F":
                row = row[:h(x)]
            if c == "B":
                row = row[h(x):]
        if y >= 1:
            if c == "L":
                col = col[:h(y)]
            if c == "R":
                col = col[h(y):]
    seatid = row[0] * 8 + col[0]
    register[rowindex].append(row[0])
    register[rowindex].append(col[0])
    register[rowindex].append(seatid)
    #pp(register[rowindex], "solved row")

register.sort(key=operator.itemgetter(-1))
seat = register[0][-1]
for index, i in enumerate(register):
    #pp(register[index], "row")
    if i[-1] != seat:
        break
    seat+=1

print("The highest seat ID is: ", register[-1])
print("My seat is ", seat)