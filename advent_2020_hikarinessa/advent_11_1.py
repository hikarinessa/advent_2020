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


def get_adjacency(my_dict : dict, row, col):
    """Given a list, row and column, returns number of empty seats around it"""
    adjacent = 0
    adjacent_list = [(row-1, col-1), (row-1, col), (row-1, col+1),
                      (row, col-1),                 (row, col+1),
                     (row+1, col-1), (row+1, col), (row+1, col+1)]

    for i in adjacent_list:
        if my_dict.get(i) == "#":
            adjacent +=1

    return adjacent


def change_seats(my_input : list, max_seats : int):
    """Runs one iteration of seat-changing."""
    changes = 0
    output = my_input.copy()
    my_dict = prep_input(my_input)
    for row, col_item in enumerate(my_input):
        for col, item in enumerate(col_item):
            adjacency = get_adjacency(my_dict, row, col)
            if item == "L" and adjacency == 0:
                output[row] = output[row][:col] + "#" + output[row][col + 1:]
                changes += 1
            if item == "#" and adjacency >= max_seats:
                output[row] = output[row][:col] + "L" + output[row][col + 1:]
                changes += 1
    if changes == 0:
        return False, output
    return True, output


def first_part(my_input, debug):
    nr_occupied_seats = 0

    changes, output = change_seats(my_input, 4)
    while changes:
        if debug: pprint.pprint(output)
        if debug: print("*"*29)
        changes, output = change_seats(output, 4)

    for row in output:
        nr_occupied_seats += row.count("#")

    return nr_occupied_seats


print("First part:", first_part(INPUT, False))  # 2152
