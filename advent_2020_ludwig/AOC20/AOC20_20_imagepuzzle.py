# https://adventofcode.com/2020/day/20
from copy import deepcopy as deep
from math import sqrt, factorial as fac
debug = False
printit = False
part2 = False

def p(text = "", override = False): #prints as string 
    if debug or printit or override:
        print(text, flush=True)
def pp(subject, name = "", override = False): #prints anything with a name as string 
    if debug or printit or override:
        #print("\n", name, ": ", subject)
        print()
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

print("\n----------------------------------")   # reading file

file = "advent_2020_ludwig/AOC20/data_aoc20_20_b.txt"
if not debug:
    file = "advent_2020_ludwig/AOC20/data_aoc20_20.txt"

with open(file) as f:
    data = f.read()


data = [s.split("\n") for s in data.split("\n\n")]

TILES = {}
for tile in data:
    TILES[tile[0][5:-1]] = [[n for n in c] for c in tile[1:]]

def flip(tile):

    newtile = deep(tile)
    width = len(tile)

    for line in range(width):
        for pixel in range(width):
            newtile[line][pixel] = tile[line][width-1-pixel]
                
    return newtile


def rotate(tile, degrees):
    
    if degrees == 0:
        return tile

    newtile = deep(tile)
    width = len(tile)

    turns = degrees // 90
    for i in range(turns):
        for line in range(width):
            for pixel in range(width):
                #if degrees == 90:
                newtile[line][pixel] = tile[width-1-pixel][line]
        tile = deep(newtile)

    return newtile


pp(fac(len(TILES)))
arraysize = int(sqrt(len(TILES)))
pp(arraysize)

def checkneighbor(tile, neighbor, direction): 
    size = len(tile)
    if direction == "north":
        border_self = "".join(tile[0])
        border_neighbor = "".join(neighbor[size-1])
    elif direction == "west":
        border_self = "".join([tile[i][0] for i in range(size)])
        border_neighbor = "".join([neighbor[i][size-1] for i in range(size)])
    else:
        print("checkneighbor error: invalid direction given")
        return None
    
    
    #ppp(tile)
    #pp(border_self)
    #pp(border_neighbor)
    fit = border_self == border_neighbor
    return fit

TILEMAP = [[] for i in range(arraysize)]
pp(TILEMAP)
TILEPOSITIONS = {}
for index, i in enumerate(TILES):
    TILEPOSITIONS[i] = None
    TILEMAP[index//arraysize].append(None)
IMAGE = deep(TILEMAP)
TILEMAP_clear = deep(TILEMAP)
TILEPOSITIONS_clear = deep(TILEPOSITIONS)
ppp(TILEMAP)   
ppp(TILEPOSITIONS, "tile positions dict", False, True)

def test_position(row, col, tile): # tests fit of a tile at a position (>0,0), BOOL
    if row == 0 and col > 0:
        neighbor = IMAGE[row][col-1] 
        if checkneighbor(tile, neighbor, "west"):
            return True
        else:
            return False
    elif col == 0 and row > 0:
        neighbor = IMAGE[row-1][col] 
        if checkneighbor(tile, neighbor, "north"):
            return True
        else:
            return False
    elif col > 0 and row > 0:
        neighbor_west, neighbor_north = IMAGE[row][col-1], IMAGE[row-1][col] 
        if (checkneighbor(tile, neighbor_north, "north") and
                checkneighbor(tile, neighbor_west, "west")):
            return True
        else:
            return False
    else:
        return None

def tile_variations(tile): # generates and returns a LIST of all flips and rots of a tile
    variations = []
    variations.append(tile)
    variations.append(rotate(tile, 90))
    variations.append(rotate(tile, 180))
    variations.append(rotate(tile, 270))
    variations.append(flip(tile))
    variations.append(flip(rotate(tile, 90)))
    variations.append(flip(rotate(tile, 180)))
    variations.append(flip(rotate(tile, 270)))
    return variations

tiles_solved = 0
solution_found = False

def solve_tile(row_index, col_index):
    global TILEMAP, TILEPOSITIONS, IMAGE  
    p("--solving tile...")
    pp(row_index, "--row")
    pp(col_index, "--col")
    for next_id in TILEPOSITIONS:
        pp(next_id, "--trying tile")
        if TILEPOSITIONS[next_id] == None:
            p("--still available")
            next_tile = TILES[next_id]
            p("--trying variations...")
            for next_variation in tile_variations(next_tile):
                if test_position(row_index, col_index, next_variation):
                    p("--fitting variation found!")
                    TILEMAP[row_index][col_index] = next_id
                    IMAGE[row_index][col_index] = next_variation
                    TILEPOSITIONS[next_id] = [row_index, col_index]
                    return True
                else:
                    p("--variation doesn't fit")
        else:
            #ppp(TILEPOSITIONS, "", False, True)
            p("--already in use")
    p("--tile can't be solved")
    return False
    

def iterate_tilemap():
    p("iterating tilemap...")
    solved = 1
    row_index, col_index = 0, 1
    while solved < len(TILES):
        p(str(row_index) + ", " + str(col_index))
        if True:
            if solve_tile(row_index, col_index):
                solved += 1
                pp(solved, "number of solved tiles")
                if col_index == arraysize-1:
                    col_index = 0
                    row_index += 1
                else:
                    col_index += 1
            else:
                p("solver iteration failed")
                return False
                break
        else:
            p("col is not None")
            return False
            break

        if solved == len(TILES):
            return True
            break

                
def select_starting_tile():
    global TILEMAP, TILEPOSITIONS, IMAGE  
    p("selecting starting tile...")
    for id in TILES: 
        id = "3643" # <------------ hard coded solution for part 2
        start_tile = TILES[id]
        
        pp(id, "trying this tile as starting", True)
        for variation in tile_variations(start_tile):
            p("--trying variation")
            TILEMAP = deep(TILEMAP_clear)
            TILEPOSITIONS = deep(TILEPOSITIONS_clear)
            TILEMAP[0][0] = id
            IMAGE[0][0] = variation
            TILEPOSITIONS[id] = [0, 0]
            ppp(TILEMAP, "current tilemap")

            if iterate_tilemap():
                p("Sucess iterating")
                return True
                break
            else:
                pass

    p("Didn't work with ANY starting tile")
    return False



if select_starting_tile():
    solution_found = True
    ppp(TILEMAP, "", True)
    #ppp(IMAGE, "image", True)
    p("Solution found!", True)
    p("product of corners:", True)
    result = (int(TILEMAP[0][0]) * int(TILEMAP[0][arraysize-1]) 
            * int(TILEMAP[arraysize-1][0]) * int(TILEMAP[arraysize-1][arraysize-1]))
    pp(result, " = ", True)
else:
    ppp(TILEMAP, "", True)
    p("fail", True)


# STARTING TILE FOR SOLUTION: 3643




#ppp(TILEMAP)   
#ppp(TILEPOSITIONS, "tile positions dict", False, True)


'''
every tile has 8 variations 
(normal 0, normal 90, normal 180, normal 270
flipped 0, 90, 180, 270

for position 0,0
try tile -> position +0,+1 until length row-> try match west of every variation 
of every other tile -> if none is found, go back to start with different start tile
if row is full try with position +1,+0 match north
if column is full as well, repeat at position 1,1 -> check north & west

'''


