# https://adventofcode.com/2020/day/9
import os
import sys

with open(os.path.join(sys.path[0], "Inputs/advent_09_input.txt"), "r") as raw_input:
    INPUT = raw_input.read().splitlines()
    INPUT = [int(i) for i in INPUT]  # preamble 25
PREAMBLE = 25
# Test values:
TEST_INPUT = [35, 20, 15, 25, 47, 40, 62, 55, 65, 95, 102, 117, 150, 182, 127, 219, 299, 277, 309, 576]
TEST_PREAMBLE = 5


def get_preamble(nr_list, preamble, i):
    """Given a list, an number and an index: [0, 1, 2, 3], 2, 3
    returns: [2, 1] (2 elements prior to index 3 on the list)"""
    preamble_list = []

    if i >= preamble:
        for j in range(preamble):
            preamble_list.append(nr_list[i-j-1])

    return preamble_list


def find_sum(nr, preamble_list):
    """Finds 2 numbers in the list that add up to the number(nr) given.
    If found a match, returns True and a tuple containing the two elements of the sum."""
    for a in preamble_list:
        for b in preamble_list:
            if preamble_list.index(a) != preamble_list.index(b):
                if a + b == nr:
                    return True, (a, b)

    return False, (0, 0)


# What is the first number that is not the sum of two of the 25 numbers before it?
def find_first_outlier(nr_list, preamble):
    for i in range(len(nr_list)):
        if i < preamble:
            pass
        else:
            preamble_list = get_preamble(nr_list, preamble, i)
            check, _sum = find_sum(nr_list[i], preamble_list)
            if not check:
                return nr_list[i]


# Find contiguous numbers on the list that add up to the "first outlier".
# Return the sum of the smallest and the largest numbers on the contiguous range.
def find_contiguous_sum(nr_list, target):
    temp_sum = 0
    temp_sum_i = []

    for i in range(len(nr_list)):
        j = i
        while temp_sum < target:
            temp_sum_i.append(nr_list[j])
            temp_sum += nr_list[j]
            j += 1
        if temp_sum == target:
            temp_sum_i.sort()
            return temp_sum_i[0] + temp_sum_i[-1]
        elif temp_sum > target:
            temp_sum = 0
            temp_sum_i = []


first_outlier = find_first_outlier(INPUT, PREAMBLE)
print("First Part:", first_outlier)  # 105950735
print("Second Part:", find_contiguous_sum(INPUT, first_outlier))  # 13826915
