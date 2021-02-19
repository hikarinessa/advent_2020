# Lights in your grid are numbered from 0 to 999 in each direction; 
# the lights at each corner are at 0,0, 0,999, 999,999, and 999,0. 
# The instructions include whether to turn on, turn off, or toggle various 
# inclusive ranges given as coordinate pairs. Each coordinate pair 
# represents opposite corners of a rectangle, inclusive; a coordinate 
# pair like 0,0 through 2,2 therefore refers to 9 lights in a 3x3 square. The lights all start turned off.

# To defeat your neighbors this year, all you have to do is set up your 
# lights by doing the instructions Santa sent you in order.

# For example:

# turn on 0,0 through 999,999 would turn on (or leave on) every light.
# toggle 0,0 through 999,0 would toggle the first line of 1000 lights, turning off the ones that were on, 
# and turning on the ones that were off.
# turn off 499,499 through 500,500 would turn off (or leave off) the middle four lights.
# After following the instructions, how many lights are lit?

#Part II
# The phrase turn on actually means that you should increase the brightness of those lights by 1.
# The phrase turn off actually means that you should decrease the brightness of those lights by 1, to a minimum of zero.
# The phrase toggle actually means that you should increase the brightness of those lights by 2.
# What is the total brightness of all lights combined after following Santa's instructions?

print("----------------------------------------------------------")

#import bookmarks as bm
#file = bm.FileBookmark("lightsfile").path
file = "advent_2020_ludwig/AOC15/lightsdata.txt"
with open(file) as f:
    data = f.read().splitlines()

#data = ["turn on 212,957 through 490,987", "toggle 171,31 through 688,88", "turn off 991,989 through 994,998"]
#data = ["turn on 0,0 through 999,999", "toggle 0,0 through 999,0", "turn off 499,499 through 500,500"]
#data = ["turn on 0,0 through 1,1", "toggle 0,0 through 2,0", "turn off 2,2 through 3,3"]

part2 = True

for i in range(len(data)):
    data[i] = data[i].replace(",", " ")

grid_size = 1000
debug = False
lights = []
for x in range(grid_size):
    lights.append([])
    for y in range(grid_size):
        lights[x].append(0)

if debug:  
    for i in lights:
        print(i)

def switch (instruction, coordinates):
    bulbs_on = 0
    bulbs_off = 0
    bulbs_toggled = 0
    c = coordinates
    rangex = len(lights[c[0]:c[2]])
    rangey = len(lights[c[1]:c[3]])
    offset = 1
    print("range x: " + str(rangex))
    print("range y: " + str(rangey))
    print(f"supposed to {instruction} {(rangex+offset) * (rangey+offset)}")
    for i in range(c[0], c[2]+1):
        if debug:
            print(f"i is {i}")
        for j in range(c[1], c[3]+1):
            if debug:
                print(f"j is {j}")
            if instruction == "turn on":
                if part2:
                    lights[i][j] += 1
                else:
                    lights[i][j] = 1
                if debug:
                    print(f"turned on lights[{i}][{j}]")
                    print(lights)
                bulbs_on += 1
            elif instruction == "toggle":
                if part2:
                    lights[i][j] += 2
                else:
                    lights[i][j] = (lights[i][j] + 1 ) % 2
                bulbs_toggled += 1
            elif instruction == "turn off":
                if part2:
                    if lights[i][j] > 0:
                        lights[i][j] -= 1
                else:
                    lights[i][j] = 0
                bulbs_off += 1
                if debug:
                    print(f"turned off lights[{i}][{j}]")

    print(f"bulbs switched on: {bulbs_on}, switched off: {bulbs_off}, toggled: {bulbs_toggled}")
    return

for s in data:
    print("\n" + s)
    s = s.split()
    if debug:
        print(s)
    if s[1] == "on":
        b = [2,3,5,6]
        coords = [int(s[i]) for i in b]
        if debug:
            print(coords)
        switch("turn on", coords)    
    elif s[1] == "off":
        b = [2,3,5,6]
        coords = [int(s[i]) for i in b]
        if debug:
            print(coords)
        switch("turn off", coords)
    elif s[0] == "toggle":
        b = [1,2,4,5]
        coords = [int(s[i]) for i in b]
        if debug:
            print(coords)
        switch("toggle", coords)
    if debug:
        print(lights)
        for r in lights:
            for c in r:
                print(c,end = " ")
            print()
        for i in range(len(lights)):
            print(f"lights[{i}]: {lights[i]}")
     
    
    
lightson = 0
brightness = 0

for i in range(len(lights)):
    for j in range(len(lights[i])):
        if part2:
            brightness += lights[i][j]
        elif lights[i][j] == 1:
            lightson += 1
            
#print(sum(sum(light) for i in lights))

if not part2:
    print(f"{lightson} lights are still on!!")
else:
    print(f"{brightness} is the total brightness!!")
print(len(data))

 