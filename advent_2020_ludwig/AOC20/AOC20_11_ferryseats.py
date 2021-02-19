# https://adventofcode.com/2020/day/11

data = """L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL"""

# If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
# If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
# Otherwise, the seat's state does not change.
import copy
debug = False
printit = True
def pp(subject, name = "", override = False): #prints anything with a name as string 
    if debug or printit or override:
        #print("\n", name, ": ", subject)
        print(name, ": ", subject)

print("\n----------------------------------")   # reading file

file = "advent_2020_ludwig/AOC20/data_aoc20_11.txt"
if not debug:
    with open(file) as f:
        data = f.read()
data = [[t for t in s] for s in data.split("\n")]

for i in data:
    pp(i)
maxrow = len(data)
maxcolumn = len(data[0])

def checkseat(row, column, seats):
    adjacent_seats = []
    #column = 1
    #row = 1
    # for seat 1,1 -> 0,0 0,1 0,2 
    #                 1,0     1,2
    #                 2,0 2,1 2,2
    # for seat 1,1 -> 0,0 0,1 0,2 
    #                 1,0     1,2
    
    
    # for seat 1,1 -> 0,1 0,2 
    #                     1,2
    #                 2,1 2,2
    # for seat 1,1 -> 0,0 0,1 
    #                 1,0    
    #                 2,0 2,1
    # for seat 1,1 -> 0,0 0,1
    #                 1,0    
    
    seat = seats[row][column]
    skippercolumn, skipperrow = 1,1
    numberempty = 0
    numberoccupied = 0
    if seat != ".":
        min = [row-1,column-1]
        max= [row+1,column+1]
        if column == 0:
            min[1] = column
            skippercolumn = 0
        if column == maxcolumn:
            max[1] = column
            skippercolumn = 1
        if row == 0:
            min[0] = row
            skipperrow = 0
        if row == maxrow:
            max[0] = row
            skipperrow = 1
        #pp(min, "min")
        #pp(max, "max")
        for irow, row in enumerate(seats[min[0]:max[0]+1]):
            #print()
            for icolumn, column in enumerate(row[min[1]:max[1]+1]):
                skip = irow == skipperrow and icolumn == skippercolumn
                if not skip:
                    adjacent_seats.append(column)
                    if column == "L":
                        numberempty += 1
                    elif column == "#":
                        numberoccupied += 1
                    else:
                        pass
                    #print(column, end="")           
        #print("\n---------")
    else:
        return "."
    if seat == "L":
        if numberoccupied == 0:
            return "#"
        else:
            return "L"
    if seat == "#":
        if numberoccupied >= 4:
            return "L"
        else:
            return "#"
    

def checkseatpart2(row, column, seats):
    seat = seats[row][column]
    #print(f"checking position {[row]},{[column]}, has value: {seat}")
    numberempty = 0
    numberoccupied = 0
    if seat != ".":
        #print("-is not floor")
        directions = [[0,-1],[0,1],[1,0],[-1,0],[1,1],[1,-1],[-1,1],[-1,-1]]
        directionnames = ["left", "right", "down", "up", "downright", "downleft", "upright", "upleft"]
        
        #print(f"--seat coordinates row: {baserow}, column: {basecolumn}")
        for i, dir in enumerate(directions):
            baserow = row 
            basecolumn = column
            #print(f"---checking {directionnames[i]}")
            directionrow = dir[0]
            directioncolumn = dir[1]
            hit = False
            while not hit:
                baserow += directionrow
                basecolumn += directioncolumn
                #print(f"----checking seat coordinates row: {baserow}, column: {basecolumn}")
                if baserow in range(maxrow) and basecolumn in range(maxcolumn):
                    check = seats[baserow][basecolumn]
                    if check == "L":
                        numberempty += 1
                        hit = True
                    elif check == "#":
                        numberoccupied += 1
                        hit = True
                    else: pass
                else:
                    hit = True
    else:
        return "."
    if seat == "L":
        if numberoccupied == 0:
            return "#"
        else:
            return "L"
    if seat == "#":
        if numberoccupied >= 5:
            return "L"
        else:
            return "#"


part2 = True

history = []
history.append(data)
#pp(history, "history")
datatemp = copy.deepcopy(data)
count = 0

while count < 1000:
    dataprevious = copy.deepcopy(datatemp)
    for indexrow, row in enumerate(datatemp):
        for indexcolumn, column in enumerate(row):
            if not part2:
                datatemp[indexrow][indexcolumn] = checkseat(indexrow, indexcolumn, dataprevious)
            else:
                datatemp[indexrow][indexcolumn] = checkseatpart2(indexrow, indexcolumn, dataprevious)
    history.append(copy.deepcopy(datatemp))
    count += 1
    if datatemp == dataprevious:
        print("no changes in seat layout --> breaking")
        break
''
for h in history:
    print("\n----------------\n")
    for d in h:
        print(d)
''   
pp(count-1, "number of times seat layout changed")

numberofoccupiedseats_final = 0
for row in history[-1]:
    for column in row:
        if column == "#":
            numberofoccupiedseats_final += 1

pp(numberofoccupiedseats_final, "final number of occupied seats")
