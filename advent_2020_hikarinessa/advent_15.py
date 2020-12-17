# https://adventofcode.com/2020/day/15
from utilities import *

INPUT = [0, 5, 4, 1, 10, 14, 7]
TEST_INPUT = [0, 3, 6]


def number_at_index(my_list, index, debug):
    my_dict = {}

    for i in range(len(my_list)-1):
        my_dict[my_list[i]] = i

    number = my_list[-1]
    i = len(my_list) - 1
    while i < index - 1:
        if debug: print("Turn", i+1, "/ number", number)
        if number in my_dict.keys():
            j = my_dict[number]
            my_dict[number] = i
            number = i - j
        else:
            my_dict[number] = i
            number = 0
        i += 1

    if debug: print("Turn", i+1, "/ number", number)

    return number


if __name__ == "__main__":
    start_time = start_timer()
    print("First part:", number_at_index(INPUT, 2020, False))
    print_elapsed_time(start_time)
    print("*"*96)
    start_time = start_timer()
    print("Second part:", number_at_index(INPUT, 30000000, False))
    print_elapsed_time(start_time)
