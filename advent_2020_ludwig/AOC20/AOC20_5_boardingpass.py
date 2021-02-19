# https://adventofcode.com/2020/day/5
# https://www.reddit.com/r/adventofcode/comments/k52psu/2020_day_05_solutions/
# The first 7 characters will either be F or B; these specify exactly one of the 128 rows on the plane (numbered 0 through 127). Each letter tells you which half of a region the given seat is in. Start with the whole list of rows; the first letter indicates whether the seat is in the front (0 through 63) or the back (64 through 127). The next letter indicates which half of that region the seat is in, and so on until you're left with exactly one row.

# For example, consider just the first seven characters of FBFBBFFRLR:

# Start by considering the whole range, rows 0 through 127.
# F means to take the lower half, keeping rows 0 through 63.
# B means to take the upper half, keeping rows 32 through 63.
# F means to take the lower half, keeping rows 32 through 47.
# B means to take the upper half, keeping rows 40 through 47.
# B keeps rows 44 through 47.
# F keeps rows 44 through 45.
# The final F keeps the lower of the two, row 44.
# The last three characters will be either L or R; these specify exactly one of the 
# 8 columns of seats on the plane (numbered 0 through 7). The same process as above 
# proceeds again, this time with only three steps. L means to keep the lower half, while R means to keep the upper half.

# For example, consider just the last 3 characters of FBFBBFFRLR:

# Start by considering the whole range, columns 0 through 7.
# R means to take the upper half, keeping columns 4 through 7.
# L means to take the lower half, keeping columns 4 through 5.
# The final R keeps the upper of the two, column 5.
# So, decoding FBFBBFFRLR reveals that it is the seat at row 44, column 5.

# Every seat also has a unique seat ID: multiply the row by 8, then add the column. In this example, 
# the seat has ID 44 * 8 + 5 = 357.

# Here are some other boarding passes:

data = """BFFFBBFRRR
FFFBBBFRRR
BBFFBBFRLL
"""
# row 70, column 7, seat ID 567.
# FFFBBBFRRR: row 14, column 7, seat ID 119.
# BBFFBBFRLL: row 102, column 4, seat ID 820.
# As a sanity check, look through your list of boarding passes. What is the highest seat ID on a boarding pass?

import operator

debug = False 
printit = True
def pp(subject, name): #prints anything with a name as string 
    if debug or printit:
        #print()
        print(name, ": ", subject)

print("\n----------------------------------")   # reading file

file = "AOC20/data_aoc20_5.txt"
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