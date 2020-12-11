# https://adventofcode.com/2020/day/11
import os
import sys
import pprint

with open(os.path.join(sys.path[0], "Inputs/advent_11_input.txt"), "r") as raw_input:
    INPUT = raw_input.read().splitlines()

TEST_INPUT = ["L.LL.LL.LL", "LLLLLLL.LL", "L.L.L..L..", "LLLL.LL.LL", "L.LL.LL.LL",
              "L.LLLLL.LL", "..L.L.....", "LLLLLLLLLL", "L.LLLLLL.L", "L.LLLLL.LL"]

TEST_INPUT2 = ["#.#L.L#.##", "#LLL#LL.L#", "L.#.L..#..", "#L##.##.L#", "#.#L.LL.LL",
               "#.#L#L#.##", "..L.L.....", "#L#L##L#L#", "#.LLLLLL.L", "#.#L#L#.##"]


def prep_input(my_input : list):
    """dict where keys are (row, column) and value is the string item"""
    my_dict = {}
    for row, col_item in enumerate(my_input):
        for col, item in enumerate(col_item):
            my_dict[row,col] = item
    return my_dict


def get_direction_slot(direction, row, col, n):
    direction_list = [(row-n, col-n), (row-n, col), (row-n, col+n),
                       (row, col-n),                 (row, col+n),
                      (row+n, col-n), (row+n, col), (row+n, col+n)]
    return direction_list[direction]


def get_viewed(my_dict : dict, row, col):
    viewed = 0
    n = 1

    for i in range(0, 8):
        while True:
            direction = my_dict.get(get_direction_slot(i, row, col, n))
            if direction == ".":
                n += 1
            elif direction == "#":
                viewed += 1
                n = 1
                break
            else:
                n = 1
                break

    return viewed


def change_seats_2(my_input : list, max_seats : int):
    """Runs one iteration of seat-changing."""
    changes = 0
    output = my_input.copy()
    my_dict = prep_input(my_input)

    for row, col_item in enumerate(my_input):
        for col, item in enumerate(col_item):
            adjacency = get_viewed(my_dict, row, col)
            if item == "L" and adjacency == 0:
                output[row] = output[row][:col] + "#" + output[row][col + 1:]
                changes += 1
            if item == "#" and adjacency >= max_seats:
                output[row] = output[row][:col] + "L" + output[row][col + 1:]
                changes += 1

    if changes == 0:
        return False, output
    return True, output


def second_part(my_input, debug):
    nr_occupied_seats = 0

    changes, output = change_seats_2(my_input, 5)
    while changes:
        if debug: pprint.pprint(output)
        if debug: print("*"*29)
        changes, output = change_seats_2(output, 5)

    for row in output:
        nr_occupied_seats += row.count("#")

    return nr_occupied_seats


# region ------- grid printing -------
# def f(s):
#     m = s[0]
#     for i in s[1:]:
#         m += '  ' + i
#     return m
#
# for i in TEST_INPUT:
#     print(f(i))

#      L  .  L  L  .  L  L  .  L  L
#      L  L  L  L  L  L  L  .  L  L
#      L  .  L  .  L  .  .  L  .  .
#      L  L  L  L  .  L  L  .  L  L
#      L  .  L  L  .  L  L  .  L  L
#      L  .  L  L  L  L  L  .  L  L
#      .  .  L  .  L  .  .  .  .  .
#      L  L  L  L  L  L  L  L  L  L
#      L  .  L  L  L  L  L  L  .  L
#      L  .  L  L  L  L  L  .  L  L
# endregion --------------------------


print("Second part:", second_part(INPUT, False))  # 1937
# print(get_viewed(prep_input(TEST_INPUT2), 3, 7))