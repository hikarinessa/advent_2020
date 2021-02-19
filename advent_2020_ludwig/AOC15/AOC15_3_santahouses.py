# Santa is delivering presents to an infinite two-dimensional grid of houses.
# He begins by delivering a present to the house at his starting location, 
# and then an elf at the North Pole calls him via radio and tells him where to move next. 
# Moves are always exactly one house to the north (^), south (v), east (>), or west (<). 
# After each move, he delivers another present to the house at his new location.
# However, the elf back at the north pole has had a little too much eggnog, 
# and so his directions are a little off, and Santa ends up visiting some houses more than once. 
# How many houses receive at least one present?
# For example:
# > delivers presents to 2 houses: one at the starting location, and one to the east.
# ^>v< delivers presents to 4 houses in a square, including twice to the house at his starting/ending location.
# ^v^v^v^v^v delivers a bunch of presents to some very lucky children at only 2 houses.

with open("advent_2020_ludwig/AOC15/santatravels.txt") as f:
    data = f.read()

print(data)

print(f"number of moves: {len(data)}")

visitedpos = ["0,0"]
posx, posy = 0, 0

for i in range(len(data)):
    character = data[i]
    if character == "^":
        # x[0][+1]
        posy += 1
    elif character == "v":
        # x[0][-1]
        posy -= 1
    elif character == "<":
        # x[-1][0]
        posx -= 1
    else:
        # x[+1][0]
        posx += 1
    
    visitedpos.append(str(posx) + "," + str(posy))

uniquehouses = len(set(visitedpos))

print(f"length of unedited visitedpos: {len(visitedpos)}")
print(f"number of unique houses: {uniquehouses}")
    
print(f"_____\n\nPART 2\n_____")

# Santa and Robo-Santa start at the same location (delivering two presents to the same starting house), 
# then take turns moving based on instructions from the elf, who is eggnoggedly reading from the same 
# script as the previous year.
posx, posy, posx2, posy2 = 0, 0, 0, 0 
visitedpos2 = ["0,0", "0,0"]

for i in range(len(data)):
    character = data[i]
    if i % 2 == 0:
        if character == "^":
            # x[0][+1]
            posy2 += 1
        elif character == "v":
            # x[0][-1]
            posy2 -= 1
        elif character == "<":
            # x[-1][0]
            posx2 -= 1
        else:
            # x[+1][0]
            posx2 += 1
        visitedpos2.append(str(posx2) + "," + str(posy2))
    else:
        if character == "^":
            # x[0][+1]
            posy += 1
        elif character == "v":
            # x[0][-1]
            posy -= 1
        elif character == "<":
            # x[-1][0]
            posx -= 1
        else:
            # x[+1][0]
            posx += 1
        visitedpos2.append(str(posx) + "," + str(posy))


uniquehouses2 = len(set(visitedpos2))

print(f"length of unedited visitedpos2: {len(visitedpos2)}")
print(f"number of unique houses: {uniquehouses2}")

