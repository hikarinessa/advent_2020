# https://adventofcode.com/2020/day/20
from copy import deepcopy as deep
from math import sqrt, factorial as fac

debug = False
printit = False
part2 = True

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
def pppp(subject, name = "", override = False, isDictionary=False): #prints list entries
    if debug or printit or override:
        #print("\n", name, ": ", subject)
        print()
        print(name, ": ")
        for item in subject:
            if isDictionary:
                print(item, ":", end="")
                print(subject[item])
            else:
                for tile in item:
                    print()
                    for line in tile: 
                        print(line)

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
    #p("--solving tile...")
    #pp(row_index, "--row")
    #pp(col_index, "--col")
    for next_id in TILEPOSITIONS:
        #pp(next_id, "--trying tile")
        if TILEPOSITIONS[next_id] == None:
            #p("--still available")
            next_tile = TILES[next_id]
            #p("--trying variations...")
            for next_variation in tile_variations(next_tile):
                if test_position(row_index, col_index, next_variation):
                    #p("--fitting variation found!")
                    TILEMAP[row_index][col_index] = next_id
                    IMAGE[row_index][col_index] = next_variation
                    TILEPOSITIONS[next_id] = [row_index, col_index]
                    return True
                else:
                    #p("--variation doesn't fit")
                    pass
        else:
            #ppp(TILEPOSITIONS, "", False, True)
            #p("--already in use")
            pass
    #p("--tile can't be solved")
    return False
    
def iterate_tilemap():
    #p("iterating tilemap...")
    solved = 1
    row_index, col_index = 0, 1
    while solved < len(TILES):
        #p(str(row_index) + ", " + str(col_index))
        if True:
            if solve_tile(row_index, col_index):
                solved += 1
                #pp(solved, "number of solved tiles")
                if col_index == arraysize-1:
                    col_index = 0
                    row_index += 1
                else:
                    col_index += 1
            else:
                #p("solver iteration failed")
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
    #p("selecting starting tile...")
    for id in TILES: 
        if not debug and part2:
            id = "3643" # <------------ hard coded solution for part 2
        start_tile = TILES[id]
        
        pp(id, "trying this tile as starting", True)
        for variation in tile_variations(start_tile):
            #p("--trying variation")
            TILEMAP = deep(TILEMAP_clear)
            TILEPOSITIONS = deep(TILEPOSITIONS_clear)
            TILEMAP[0][0] = id
            IMAGE[0][0] = variation
            TILEPOSITIONS[id] = [0, 0]
            #ppp(TILEMAP, "current tilemap")

            if iterate_tilemap():
                #p("Sucess iterating")
                return True
                break
            else:
                pass

    #p("Didn't work with ANY starting tile")
    return False

def transform_image(image):
    image_as_list = [[c for c in s] for s in image.split("\n")]
    #ppp(image_list)
    transformed_images = tile_variations(image_as_list)
    #ppp(transformed_images)
    str_image_list = []

    for image in transformed_images:
        
        str_image = ""
        for row in image:
            str_image += "".join(row) + "\n"
        
        str_image_list.append(str_image[:-1])
    
    return(str_image_list)

def crop_image(image):
    output = ""
    #output = []
    for r, row in enumerate(image):
        #pp(row, "row")
        tile = row[0]
        #pp(tile, "tile")
        for i in range(len(tile)-2):
            i += 1
            #pp(i, "line number")
            for j in range(len(row)):
                #pp(j, "tile number")
                line = "".join(image[r][j][i][1:-1])
                #line = image[0][j][i][1:-1]
                
                output += line
                #output.append(line)
                
            output += "\n"
            #pp(line, "joined line")
            #ppp(output, "current output")
    return output[:-1]

def check_for_seamonsters(image):
    sea_monster_positions = []
    sea_monster_count = 0
    image_as_list = [[c for c in s] for s in image.split("\n")]
    ppp(image_as_list)
    sea_monster_length = 20
    sea_monster_height = 3
    #pp(len(image_as_list))
    top_positions = [18]
    middle_positions = [0,5,6,11,12,17,18,19]
    bottom_positions = [1,4,7,10,13,16]
    monster_valid = "###############"
    for row_index in range(len(image_as_list)-sea_monster_height+1):
        row = image_as_list[row_index]
        
        for col_index in range(len(row)-sea_monster_length+1):
            monster = ""
            pixel = row[col_index]
            top = image_as_list[row_index][col_index:col_index+sea_monster_length]
            middle = image_as_list[row_index+1][col_index:col_index+sea_monster_length]
            bottom = image_as_list[row_index+2][col_index:col_index+sea_monster_length]
            #pp(top), pp(middle), pp(bottom)
            for top_pos in top_positions:
                monster += top[top_pos]
                if top[top_pos] == "#":
                    top[top_pos] = "Ö"
            
            for middle_pos in middle_positions:
                monster += middle[middle_pos]
                if middle[middle_pos] == "#":
                    middle[middle_pos] = "Ö"
            
            for bottom_pos in bottom_positions:
                monster += bottom[bottom_pos]
                if bottom[bottom_pos] == "#":
                    bottom[bottom_pos] = "Ö"
            
            pp(monster, "monster pattern in current water patch")
            if monster == monster_valid:
                print("sea monster found!")
                sea_monster_count += 1
                pp("".join(top))
                pp("".join(middle))
                pp("".join(bottom))

            '''
            .#...#.###...#.##.O#   line 1: 18
            O.##.OO#.#.OO.##.OOO   line 2: 0, 5, 6, 11, 12, 17, 18, 19
            #O.#O#.O##O..O.#O##.   line 3: 1, 4, 7, 10, 13, 16
            '''
    return sea_monster_count

def count_hashes(image):
    hash_count = 0
    image_as_list = [[c for c in s] for s in image.split("\n")]
    for row in image_as_list:
        for col in row:
            if col == "#":
                hash_count += 1
    pp(hash_count, "total number of hashes in image")
    return hash_count
    

if select_starting_tile():
    solution_found = True
    ppp(TILEMAP, "", True)
    #pppp(IMAGE, "image")
    p("Solution found!", True)
    p("product of corners:", True)
    result = (int(TILEMAP[0][0]) * int(TILEMAP[0][arraysize-1]) 
            * int(TILEMAP[arraysize-1][0]) * int(TILEMAP[arraysize-1][arraysize-1]))
    pp(result, " = ", True)
    if part2:
        final_image = crop_image(IMAGE)
        print(final_image)
        image_variations = transform_image(final_image)
        for img_variation in image_variations:
            sea_monsters_found = check_for_seamonsters(img_variation)
            if sea_monsters_found > 0:
                pp(sea_monsters_found, "number of sea monsters", True)
                roughness = count_hashes(final_image) - sea_monsters_found * 15
                pp(roughness, "roughness of water", True)
                break
        
else:
    ppp(TILEMAP, "", True)
    p("fail", True)
'''
sea monster

length 20, height 3, check each block of this size
.#...#.###...#.##.O#   line 1: 18
O.##.OO#.#.OO.##.OOO   line 2: 0, 5, 6, 11, 12, 17, 18, 19
#O.#O#.O##O..O.#O##.   line 3: 1, 4, 7, 10, 13, 16
'''
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


