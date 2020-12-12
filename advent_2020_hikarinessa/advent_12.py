# https://adventofcode.com/2020/day/12
import os
import sys

with open(os.path.join(sys.path[0], "Inputs/advent_12_input.txt"), "r") as raw_input:
    INPUT = raw_input.read().splitlines()
CLOCKWISE_CARDINALS = ("N", "E", "S", "W")
TEST_INPUT = ["F10", "N3", "F7", "R90", "F11"]


def turn(direction, amount, current_orientation):
    co_index = CLOCKWISE_CARDINALS.index(current_orientation)
    angle = int(amount / 90)

    if direction == "R":
        new_orientation = (co_index + angle) % 4
    elif direction == "L":
        new_orientation = (co_index - angle) % 4
    else:
        new_orientation = ""

    return CLOCKWISE_CARDINALS[new_orientation]


def first_part(my_input):
    current_orientation = "E"
    dicc_coords = {"N": 0, "E": 0, "S": 0, "W": 0}

    for i, val in enumerate(my_input):
        instruction = val[:1]
        amount = int(val[1:])
        if instruction in "LR":
            current_orientation = turn(instruction, amount, current_orientation)
        elif instruction == "F":
            dicc_coords[current_orientation] += amount
        elif instruction in dicc_coords.keys():
            dicc_coords[instruction] += amount
    x = dicc_coords["E"] - dicc_coords["W"]
    y = dicc_coords["N"] - dicc_coords["S"]

    return abs(x) + abs(y)


def turn_waypoint(direction, amount, x, y):
    angle = int(amount / 90)  # 1, 2, 3

    for i in range (0, angle):
        if direction == "L":
            new_x = -y
            new_y = x
            print("performing rotation", new_x, new_y)
        elif direction == "R":
            new_x = y
            new_y = -x
            print("performing rotation", new_x, new_y)
        x = new_x
        y = new_y

    return new_x, new_y


def second_part(my_input, debug):
    way_x = 10
    way_y = 1
    x = 0
    y = 0

    for i, val in enumerate(my_input):
        # if debug: print(x, y, "/", way_x, way_y, "/", val)
        instruction = val[:1]
        amount = int(val[1:])

        if instruction in "LR":
            way_x, way_y = turn_waypoint(instruction, amount, way_x, way_y)
        elif instruction == "F":
            x += way_x * amount
            y += way_y * amount
        elif instruction == "N":
            way_y += amount
        elif instruction == "S":
            way_y -= amount
        elif instruction == "E":
            way_x += amount
        elif instruction == "W":
            way_x -= amount
        if debug: print(x, y, "/", way_x, way_y, "/", val, "/ performed")
        if debug: print("*"*29)

    return abs(x) + abs(y)


print("First part:", first_part(INPUT))  # 439
print("Second part:", second_part(INPUT, True))  # 12385
