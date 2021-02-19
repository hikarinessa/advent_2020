# https://adventofcode.com/2020/day/12

# Action N means to move north by the given value.
# Action S means to move south by the given value.
# Action E means to move east by the given value.
# Action W means to move west by the given value.
# Action L means to turn left the given number of degrees.
# Action R means to turn right the given number of degrees.
# Action F means to move forward by the given value in the direction the ship is currently facing.
# The ship starts by facing east. Only the L and R actions change the direction the ship is facing. 
# (That is, if the ship is facing east and the next instruction is N10, the ship would 
# move north 10 units, but would still move east if the following action were F.)

data = """F10
N3
F7
R90
F11"""

# F10 would move the ship 10 units east (because the ship starts by facing east) to east 10, north 0.
# N3 would move the ship 3 units north to east 10, north 3.
# F7 would move the ship another 7 units east (because the ship is still facing east) to east 17, north 3.
# R90 would cause the ship to turn right by 90 degrees and face south; it remains at east 17, north 3.
# F11 would move the ship 11 units south to east 17, south 8.
# 
# At the end of these instructions, the ship's Manhattan distance (sum of the absolute values 
# of its east/west position and its north/south position) from its starting position is 17 + 8 = 25.
# Figure out where the navigation instructions lead. What is the Manhattan distance between 
# that location and the ship's starting position?


debug = False
printit = True
def pp(subject, name = "", override = False): #prints anything with a name as string 
    if debug or printit or override:
        #print("\n", name, ": ", subject)
        print(name, ": ", subject)

print("\n----------------------------------")   # reading file

file = "advent_2020_ludwig/AOC20/data_aoc20_12.txt"
if not debug:
    with open(file) as f:
        data = f.read()
data = [s for s in data.split("\n")]
datarot = []
datadir = []
datarotdir = []
for i, s in enumerate(data):
    data[i] = [s[0], int(s[1:])]
    if s[0] in ("L","R","F"):
        datarot.append(data[i])
    else:
        datadir.append(data[i])

#part2
westeast = 0
southnorth = 0
waypoint_westeast = 10
waypoint_southnorth = 1
for s in data:
    dir = s[0]
    num = s[1]
    print(f"waypoint position: WE {waypoint_westeast}, SN {waypoint_southnorth}")
    print(f"ship position: WE {westeast}, SN {southnorth}")
    wp_we_mem = waypoint_westeast
    wp_sn_mem = waypoint_southnorth
    if dir == "F":
        westeast += waypoint_westeast * num
        southnorth += waypoint_southnorth * num
    elif dir == "E":
        waypoint_westeast += num
    elif dir == "W":
        waypoint_westeast -= num
    elif dir == "N":
        waypoint_southnorth += num
    elif dir == "S":
        waypoint_southnorth -= num
    elif dir == "L":
        if num == 90:
            waypoint_westeast = -wp_sn_mem
            waypoint_southnorth = wp_we_mem
        elif num == 180:
            waypoint_westeast = -wp_we_mem
            waypoint_southnorth = -wp_sn_mem
        elif num == 270:
            waypoint_westeast = wp_sn_mem
            waypoint_southnorth = -wp_we_mem
    elif dir == "R":
        if num == 270:
            waypoint_westeast = -wp_sn_mem
            waypoint_southnorth = wp_we_mem
        elif num == 180:
            waypoint_westeast = -wp_we_mem
            waypoint_southnorth = -wp_sn_mem
        elif num == 90:
            waypoint_westeast = wp_sn_mem
            waypoint_southnorth = -wp_we_mem

westeast = abs(westeast)
southnorth = abs(southnorth)

manhattandist = westeast + southnorth

pp(manhattandist, "Manhattan Distance Part 2")


'''
pp(data, "data")
print()
pp(datarot, "datarot")
print()
pp(datadir, "datadir")
'''
ship_facing = "East"
ship_rot_deg = 0

for s in datarot:
    while ship_rot_deg >= 360:
        ship_rot_deg -= 360
    while ship_rot_deg < 0:
        ship_rot_deg += 360
    if s[0] == "F":
        if ship_rot_deg == 0:
            datarotdir.append(["E", s[1]])
        elif ship_rot_deg == 90:
            datarotdir.append(["S", s[1]])
        elif ship_rot_deg == 180:
            datarotdir.append(["W", s[1]])
        elif ship_rot_deg == 270:
            datarotdir.append(["N", s[1]])
    elif s[0] == "L":
        ship_rot_deg -= s[1]
    elif s[0] == "R":
        ship_rot_deg += s[1]

for s in datarotdir:
    datadir.append(s)
'''
print()
pp(datarotdir, "datarotdir")
print()
pp(datadir, "datadir")
'''
westeast = 0
southnorth = 0
for move in datadir:
    if move[0] == "E":
        westeast += move[1]
    if move[0] == "W":
        westeast -= move[1]
    if move[0] == "S":
        southnorth -= move[1]
    if move[0] == "N":
        southnorth += move[1]

westeast = abs(westeast)
southnorth = abs(southnorth)

manhattandist = westeast + southnorth

pp(manhattandist, "mamhattat")