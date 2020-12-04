# You make a map (your puzzle input) of the open squares (.) and trees (#) you can see.
# The same pattern repeats to the right many times.
# The toboggan can only follow a few specific slopes:
# start by counting all the trees you would encounter for the slope right 3, down 1

import json

with open( 'advent_03_input.json', "r" ) as f:
    data = json.load(f)

toboggan_trees = data["toboggan_trees"]


# how many trees would you encounter?
def find_trees_in_path():
    x = 0
    trees = 0

    for row in toboggan_trees:
        x %= 31  # length of a row is 31
        if row[x] == "#":
            trees += 1
        x += 3

    print("First part: ", trees)


# What do you get if you multiply together the number of trees encountered on each of the listed slopes?
def find_multiplied_trees():
    multiplied_trees = 1
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

    for slope in slopes:
        x = 0
        trees = 0
        step = slope[1]
        for row in range(0, len(toboggan_trees), step):
            x %= 31
            if toboggan_trees[row][x] == "#":
                trees += 1
            # print(str(x) + " " + str(row) + " " + toboggan_trees[row][x] + " " + str(trees))
            x += slope[0]

        multiplied_trees *= trees

    print("Second part: ", multiplied_trees)


find_trees_in_path()
find_multiplied_trees()
