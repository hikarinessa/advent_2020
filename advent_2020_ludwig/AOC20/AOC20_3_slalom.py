
# https://adventofcode.com/2020/day/3
# 
# 
# the same pattern repeats to the right many times
# You start on the open square (.) in the top-left corner and need 
# to reach the bottom (below the bottom-most row on your map).
# start by counting all the trees you would encounter for the slope right 3, down 1:
# 
# part 2: Determine the number of trees you would encounter if, for each of the following slopes, you start at the top-left corner and traverse the map all the way to the bottom:
# Right 1, down 1.
# Right 3, down 1. (This is the slope you already checked.)
# Right 5, down 1.
# Right 7, down 1.
# Right 1, down 2.
# In the above example, these slopes would find 2, 7, 3, 4, and 2 tree(s) respectively; 
# multiplied together, these produce the answer 336.
# What do you get if you multiply together the number of trees encountered on each of the listed slopes?

data = """..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#
"""

debug = False 
printit = True
def pp(subject, name): #prints anything with a name as string 
    if debug or print:
        #print()
        print(name, ": ", subject)

print("\n----------------------------------")   # reading file
file = "advent_2020_ludwig/AOC20/data_aoc20_3.txt"

if not debug:
    with open(file) as f:
        data = f.read()
data = [s for s in data.splitlines()]

pp(data, "data")
pp(len(data), "Items in data")

linecount = len(data)
patternlength = len(data[0])
pp(patternlength, "pattern length")

slopes = [[1,1],[3,1],[5,1],[7,1],[1,2]]
tree_prod = 0

for s in slopes:
    x, y = s
    trees = 0
    posx = 0
    posy = 0
    print("x ", x, " y ", y)

    for index, i in enumerate(data[y:]):
        #pp(index+y, "index")
        posy = index + y
        if posy == linecount:
            break
        if posy % y == 0:
            #pp(posy, "posy"), pp(linecount,"linecount"), pp(patternlength, "patternlength"), pp(posx, "posx"), pp(x, "x")
            if posx+x >= patternlength:
                posx -= patternlength
            if i[posx+x] == "#":
                trees += 1
                #print("Hit tree at line ", index, "position ", posx+x)   
            posx += x

    if tree_prod == 0:
        tree_prod = trees
    else:
        tree_prod *= trees

    pp(trees, "total encountered trees")

pp(tree_prod, "product of total encountered trees")




