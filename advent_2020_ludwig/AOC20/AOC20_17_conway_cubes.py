# https://adventofcode.com/2020/day/17

import copy

data = """.#.
..#
###"""

part2 = True
debug = False
printit = False

if not debug:
    data = """.###..#.
##.##...
....#.#.
#..#.###
...#...#
##.#...#
#..##.##
#......."""

def pp(subject, name = "", override = False): #prints anything with a name as string 
    if debug or printit or override:
        #print("\n", name, ": ", subject)
        #print()
        print(name, ": ", subject)


def ppp(subject, name = "", override = False, levels = 2, isDictionary=False): #prints list entries
    if debug or printit or override:
        #print("\n", name, ": ", subject)
        print()
        print(name, ": ")
        if levels == 1:
            print(subject)
        elif levels == 2:
            for item in subject:
                if isDictionary:
                    print(item, ":", end="")
                    print(subject[item])
            else:
                print(item)
        else:
            for item in subject:
                print()
                for item in item:
                    print(item)

        

print("\n----------------------------------")   # reading file

data = [[ t for t in s] for s in data.split("\n")]
pp(data, "data")
gridw, grid, gridx, gridy = [], [], [], []

cycle_count = 7

required_grid_size = len(data[0]) + 2*cycle_count
required_grid_size_z = 1 + 2*cycle_count
pp(required_grid_size, "req grid size")

for i in range(required_grid_size):
    gridx.append(".")
for i in range(required_grid_size):
    gridy.append(copy.deepcopy(gridx))
for i in range(required_grid_size_z):
    grid.append(copy.deepcopy(gridy))
if part2:    
    for i in range(required_grid_size_z):
        gridw.append(copy.deepcopy(grid))

for index_y, y in enumerate(data):
    for index_x, x in enumerate(y):
        if part2:
            gridw[cycle_count][cycle_count][index_y+cycle_count][index_x+cycle_count] = x
        else:
            grid[cycle_count][index_y+cycle_count][index_x+cycle_count] = x


def check_neighbors(pos_z, pos_y, pos_x, value, gridtocheck, pos_w, debug=False):
    neighbors = []
    active = 0
    checked = 0
    if part2:
        for w in gridtocheck[pos_w-1:pos_w+2]:
            for z in w[pos_z-1:pos_z+2]:
                for y in z[pos_y-1:pos_y+2]:
                    for x in y[pos_x-1:pos_x+2]:
                        checked += 1
                        if x == "#":
                            active += 1
                        neighbors.append(x)
    else:
        for z in gridtocheck[pos_z-1:pos_z+2]:
            for y in z[pos_y-1:pos_y+2]:
                for x in y[pos_x-1:pos_x+2]:
                    checked += 1
                    if x == "#":
                        active += 1
                    neighbors.append(x)
    #pp(checked, "number of checked neighbors")
    if value == ".":
        if active == 3:
            return "#"
        else:
            return "."
    elif value == "#":
        active -= 1
        if active in range(2,4):
            return "#"
        else:
            return "."

cycle = 1
#ppp(grid,"grid", False, 3)
while cycle <= (cycle_count):
    if part2:
        grid_temp = copy.deepcopy(gridw)
        for pos_w, w in enumerate(grid_temp):
            for pos_z, z in enumerate(w):
                for pos_y, y in enumerate(z):
                    for pos_x, cube in enumerate(y):
                        gridw[pos_w][pos_z][pos_y][pos_x] = check_neighbors(pos_z, pos_y, pos_x, cube, grid_temp, pos_w, False)
    else:
        grid_temp = copy.deepcopy(grid)
        for pos_z, z in enumerate(grid_temp):
            for pos_y, y in enumerate(z):
                for pos_x, cube in enumerate(y):
                    grid[pos_z][pos_y][pos_x] = check_neighbors(pos_z, pos_y, pos_x, cube, grid_temp, False, 0)
    
    #ppp(grid,"grid", False, 3)
    actives = 0
    if part2:
        for w in gridw:
            for z in w:
                for y in z:
                    for x in y:
                        if x == "#":
                            actives += 1
    else:
        for z in grid:
            for y in z:
                for x in y:
                    if x == "#":
                        actives += 1
    print(f"actives after {cycle} cycles(s): {actives}")
    cycle += 1


