# https://adventofcode.com/2020/day/24

import re
from copy import deepcopy as deep

debug = False
printit = False
part2 = False

def p(text = "", override = False): #prints as string 
    if debug or printit or override:
        print(text, flush=True)
def pp(subject, name = "", override = False): #prints anything with a name as string 
    if debug or printit or override:
        #print("\n", name, ": ", subject)
        #   print()
        print(name, ": ", subject)
def ppp(subject, name = "", override = False, isDictionary=False): #prints list entries
    if debug or printit or override:
        #print("\n", name, ": ", subject)
        print()
        print(name, ": ")
        for item in subject:
            if isDictionary:
                print(item, ":", end="")
                print(subject[item])
            else:
                print(item)
def pppp(subject, name = "", override = False, isDictionary=False): #prints list's list entries without linebreak
    if debug or printit or override:
        #print("\n", name, ": ", subject)
        print()
        print(name, ": ")
        for item in subject:
            print()
            if isDictionary:
                print(item, ":", end="")
                print(subject[item])
            else:
                for tile in item:
                    
                    print(tile, end="")

print("\n----------------------------------")   # reading file

DATA = """sesenwnenenewseeswwswswwnenewsewsw
neeenesenwnwwswnenewnwwsewnenwseswesw
seswneswswsenwwnwse
nwnwneseeswswnenewneswwnewseswneseene
swweswneswnenwsewnwneneseenw
eesenwseswswnenwswnwnwsewwnwsene
sewnenenenesenwsewnenwwwse
wenwwweseeeweswwwnwwe
wsweesenenewnwwnwsenewsenwwsesesenwne
neeswseenwwswnwswswnw
nenwswwsewswnenenewsenwsenwnesesenew
enewnwewneswsewnwswenweswnenwsenwsw
sweneswneswneneenwnewenewwneswswnese
swwesenesewenwneswnwwneseswwne
enesenwswwswneneswsenwnewswseenwsese
wnwnesenesenenwwnenwsewesewsesesew
nenewswnwewswnenesenwnesewesw
eneswnwswnwsenenwnwnwwseeswneewsenese
neswnwewnwnwseenwseesewsenwsweewe
wseweeenwnesenwwwswnew"""

if not debug:
    file = "advent_2020_ludwig/AOC20/DATA_aoc20_24.txt"
    with open(file) as f:
        DATA = f.read()
DATA = [line for line in DATA.split("\n")]
ppp(DATA)
directions = []

decode = re.compile(r"[^we]*(?:[e])|[^we]*(?:[w])|ne|nw|se|sw") # -- thank u, https://regex101.com/
print(decode.findall(DATA[0]))

for i, line in enumerate(DATA):
    directions.append(decode.findall(line))

ppp(directions)

def determine_floorsize():
    eastmax, westmax, northmax, southmax = [], [], [], []
    for line in directions:
        east, west, north, south = 0, 0, 0, 0
        for direction in line:
            if "e" in direction:
                east += 1
            if "w" in direction:
                west += 1
            if "s" in direction:
                south += 1
            if "n" in direction:
                north += 1
        eastmax.append(east)
        westmax.append(west)
        northmax.append(north)
        southmax.append(south)

    eastmax = max(eastmax)
    westmax = max(westmax)
    northmax = max(northmax)
    southmax = max(southmax)
    
    largest_side = max([eastmax, westmax, northmax, southmax])
    recommended_floorsize = largest_side * 2 + 24
    print(f"recommended floor size is {recommended_floorsize}")
    # pp(eastmax, "east max"), pp(southmax, "south max"), pp(westmax, "west max"), pp(northmax, "north max")
    return recommended_floorsize
    
size = determine_floorsize()
ref = size // 2
print(f"reference tile is {ref},{ref}")
floor = [["." for j in range(size)] for i in range(size)]

for row_index in range(0, size): 
    col = row_index % 2
    for col_index in range(col, size, 2):  # marking actual tiles on the grid (alternating by modulo of row_index)
        floor[row_index][col_index] = "_"

pppp(floor)
floor_pristine = deep(floor)

blacks = 0
for line in directions:
    row = ref
    col = ref
    for direction in line:
        if direction == "e":
            col += 2
        elif direction == "w":
            col -= 2
        elif direction == "nw":
            row -= 1
            col -= 1
        elif direction == "ne":
            row -= 1
            col += 1
        elif direction == "sw":
            row += 1
            col -= 1
        elif direction == "se":
            row += 1
            col += 1
    
    tile = floor[row][col]
    if tile == ".":
        print("ERROR, no tile here!!")
        break
    elif tile == "_":
        floor[row][col] = "X"
        blacks += 1
    elif tile == "X":
        floor[row][col] = "_"
        blacks -= 1

pppp(floor, "", True)

print(f"\nThere are {blacks} tiles left black")

# -- part 2 --
cycle_count = 100
for i, line in enumerate(floor_pristine):
    floor_pristine[i] = deep(line) * 5
    floor[i] = deep(line) * 2 + deep(floor[i]) + deep(line) * 2
floor = deep(floor_pristine) + deep(floor) + deep(floor_pristine)

#floor = deep(floor)

#pppp(floor, "", True)


def check_neighbors(pos_y, pos_x, value, gridtocheck):
    neighbors = []
    blacks = 0
    whites = 0
    checked = 0
    for y in gridtocheck[pos_y-1:pos_y+2]:
        for x in y[pos_x-2:pos_x+3]:
            checked += 1
            if x == "X":
                blacks += 1
                neighbors.append(x)
            elif x == "_":
                whites += 1
                neighbors.append(x)
            else:
                pass

    if value == "_":
        whites -= 1
        if blacks == 2:
            return "X"
        else:
            return "_"
    elif value == "X":
        blacks -= 1
        if blacks == 0 or blacks > 2:
            return "_"
        else:
            return "X"
    else:
        return "."

cycle = 1

while cycle <= (cycle_count):
    floor_temp = deep(floor)
    for pos_y, y in enumerate(floor_temp):
        for pos_x, tile in enumerate(y):
            floor[pos_y][pos_x] = check_neighbors(pos_y, pos_x, tile, floor_temp)
    
    blacks = 0

    for y in floor:
        for x in y:
            if x == "X":
                blacks += 1
    print(f"blacks after {cycle} cycles(s): {blacks}")
    cycle += 1


#pppp(floor, "", True)

'''
  0123456789012
0 .x.x.x.x.x.x.
1 x.x.x.x.x.
2 .x.x.x.x.x
3 x.x.x.x.x.
4 .x.x.x.x.x

'''
