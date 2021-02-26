
# https://adventofcode.com/2020/day/3

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
    if debug or printit:
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




