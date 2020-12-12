# https://adventofcode.com/2020/day/10
import os
import sys
import pprint
import time
import datetime as dt

# region -------- Preparing Inputs --------
with open(os.path.join(sys.path[0], "Inputs/advent_10_input.txt"), "r") as raw_input:
    INPUT = raw_input.read().splitlines()
    INPUT = [int(i) for i in INPUT]
    INPUT.sort()
    INPUT = [0] + INPUT
# Test values (First part): 22 differences of 1 jolt and 10 differences of 3 jolts. 22 x 10 = 220
# Test values (Second part): 19208 distinct arrangements
TEST_INPUT = [28, 33, 18, 42, 31, 14, 46, 20, 48, 47, 24, 23, 49, 45, 19,
              38, 39, 11, 1, 32, 25, 35, 8, 17, 7, 9, 4, 2, 34, 10, 3]
TEST_INPUT.sort()
TEST_INPUT = [0] + TEST_INPUT

# Simple values (First part): 7 differences of 1 jolt and 5 differences of 3 jolts. 7 x 5 = 35
# Simple values (Second part): 8 distinct arrangements
SIMPLE_INPUT = [16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]
SIMPLE_INPUT.sort()
SIMPLE_INPUT = [0] + SIMPLE_INPUT
# endregion -------------------------------


# Find a chain that uses all of your adapters
# What is the number of 1-jolt differences multiplied by the number of 3-jolt differences?
def first_part(my_ordered_list):
    # initiate counters depending on the lowest-joltage connector available
    one_counter = 0
    three_counter = 1

    for i in range(len(my_ordered_list)-1):
        if my_ordered_list[i+1] - my_ordered_list[i] == 1:
            one_counter += 1
        elif my_ordered_list[i+1] - my_ordered_list[i] == 3:
            three_counter += 1

    return one_counter * three_counter


def find_deletion_candidates(my_ordered_list):
    """Returns a list with indices of elements that can be deleted from the input"""
    bool_list = [False] * len(my_ordered_list)
    for i in range(len(my_ordered_list)-2):
        i += 1
        if my_ordered_list[i+1] - my_ordered_list[i-1] <= 3:
            bool_list[i] = True
    deletion_candidates = [i for i, val in enumerate(bool_list) if val]
    if deletion_candidates:
        return True, deletion_candidates
    else:
        # print("no candidates")
        return False, []


def get_combinations(my_ordered_list, debug):
    """This works with any input but it's tremendously time consuming."""
    permutations_to_check : list = [ tuple(my_ordered_list) ]
    permutations_checked = {}

    if debug:
        t = dt.datetime.now()
        print(time.strftime("%H:%M:%S", time.gmtime(time.time())))

    while len(permutations_to_check) > 0:
        i : tuple = permutations_to_check.pop()
        permutations_checked[hash(i)] = 0
        found, deletion_candidates = find_deletion_candidates(i)
        if debug: print(i, deletion_candidates)
        for j in deletion_candidates:
            p = list(i)
            p.pop(j)
            p = tuple(p)
            if hash(p) not in permutations_checked:
                permutations_to_check.append(p)

        if debug:
            delta = dt.datetime.now()-t
            if delta.seconds >= 60:
                print(time.strftime("%H:%M:%S", time.gmtime(time.time())), len(permutations_checked))
                t = dt.datetime.now()

    combinations = len(permutations_checked)

    return combinations


def second_part(my_ordered_list, debug):
    """This works because the input list does not have jumps of 2, only 1 and 3"""
    total = 1
    counter = 1
    counter_list = []
    corresponding_dict = { 0:1, 1:1, 2:1, 3:2, 4:4, 5:7, 6:13, 7:24 }
        # Hardcoded possible combinations given the amount of consecutive numbers
        # I used get_combinations to find these numbers

    for i in range(len(my_ordered_list)):
        if my_ordered_list[i] - my_ordered_list[i-1] == 1:
            counter += 1
        elif my_ordered_list[i] - my_ordered_list[i-1] == 3:
            total *= corresponding_dict[counter]
            counter_list.append(counter)
            counter = 1

    return total


print("First part:", first_part(INPUT))  # 2100

# print("Second part:", get_combinations(TEST_INPUT, False))  # first solution I did, takes FOREVER
INPUT.append(INPUT[-1]+3) # add the last element to the list, so the second solution works
print("Second part:", second_part(INPUT, False))  # 16198260678656


# region ------------------ second part dev -------------------
def second_part1(my_ordered_list, debug):  # 42 sec with TEST_INPUT
    permutations = 0
    _found, deletion_candidates = find_deletion_candidates(my_ordered_list)
    permutations_dic = { tuple( my_ordered_list.copy() ): deletion_candidates }

    permutations_checked = []  # list(permutations_dic.keys())

    while len(permutations_dic) != len(permutations_checked):                           # while I haven't checked all stored permutations
        for i in list(permutations_dic.keys()):                                         # for every key in the dict
            if i not in permutations_checked:                                           # as long as that key is not checked
                permutations_checked.append(i)                                          # check it:
                deletion_candidates = permutations_dic[i]                               # find deletion candidates for it
                for j in deletion_candidates:                                           # and for every deletion candidate
                    p = list(i)                                                         # create a copy of the permutation
                    p.pop(j)                                                            # delete the deletion candidate
                    new_found, new_deletion_candidates = find_deletion_candidates(p)    # find its deletion candidates
                    permutations_dic[tuple(p)] = new_deletion_candidates                # and add that permutation to the dic

    permutations += len(permutations_dic)

    if debug: pprint.pprint(permutations_dic)
    if debug: print(permutations)

    return permutations


def second_part2(my_ordered_list, debug):  # mre than 2 min with TEST_INPUT
    permutations = 0
    _found, deletion_candidates = find_deletion_candidates(my_ordered_list)
    permutations_dic = { tuple( my_ordered_list.copy() ): deletion_candidates }

    permutations_to_check = list(permutations_dic.keys())  # list(permutations_dic.keys())

    while len(permutations_to_check) > 0:
        i = permutations_to_check.pop()
        deletion_candidates = permutations_dic[tuple(i)]
        if debug: print(i, deletion_candidates)
        for j in deletion_candidates:
            p = list(i)
            p.pop(j)
            new_found, new_deletion_candidates = find_deletion_candidates(p)
            permutations_dic[tuple(p)] = new_deletion_candidates
            if p not in permutations_to_check:
                permutations_to_check.append(p)

    permutations += len(permutations_dic)
    # if debug: pprint.pprint(permutations_dic)
    # if debug: print(permutations)

    return permutations


def second_part3(my_ordered_list, debug):  # 33 sec with TEST_INPUT

    permutations_to_check : list = [ tuple(my_ordered_list) ]
    permutations_checked = []

    while len(permutations_to_check) > 0:
        i : tuple = permutations_to_check.pop()
        if hash(i) not in permutations_checked:
            permutations_checked.append(hash(i))
            found, deletion_candidates = find_deletion_candidates(i)
            if debug: print(hash(i), i, deletion_candidates)
            for j in deletion_candidates:
                p = list(i)
                p.pop(j)
                p = tuple(p)
                if hash(p) not in permutations_checked:
                    permutations_to_check.append(p)

    permutations = len(permutations_checked)
    # if debug: pprint.pprint(permutations_dic)
    # if debug: print(permutations)

    return permutations
# endregion --------------------------------------------------------
