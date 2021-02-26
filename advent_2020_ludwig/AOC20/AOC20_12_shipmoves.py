# https://adventofcode.com/2020/day/12

data = """F10
N3
F7
R90
F11"""

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
        if num == 90: #... looks a bit tedious here
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

pp(manhattandist, "manhattan part 1")