import os
import sys
import itertools

INPUT_TXT = "../Input/10_AdapterArray.txt"
TEST_INPUT_TXT = "../Input/10_AdapterArray_TestInput.txt"


def get_input(txt):
    with open(os.path.join(sys.path[0], txt), "r") as my_input:
        return [int(line) for line in my_input.read().splitlines()]


def combination_is_valid(combination):
    for i, num in enumerate(combination[1:]):
        if num - combination[i] > 3:
            return False

    return True


def part_one(numbers):
    numbers.append(0)
    numbers.sort()
    numbers.append(numbers[-1] + 3)

    one_jolt_diffs = 0
    three_jolt_diffs = 0
    for i, num in enumerate(numbers[1:]):
        diff = num - numbers[i]
        if diff == 1:
            one_jolt_diffs += 1
        elif diff == 3:
            three_jolt_diffs += 1

    print("*"*96)
    print("PART ONE")
    print("{} 1-jolt differences and {} 3-jolt differences found. "
          "The product of both is {}".format(one_jolt_diffs, three_jolt_diffs, one_jolt_diffs*three_jolt_diffs))


def part_two(numbers):
    numbers.append(0)
    numbers.sort()
    numbers.append(numbers[-1] + 3)

    consecutive_nums = 0
    total_permutations = 1

    for i, num in enumerate(numbers[1:]):
        # Check for consecutive numbers
        if num - numbers[i] == 1:
            consecutive_nums += 1

        # Check for a set of 3 or more consecutive numbers (zero-indexed)
        elif consecutive_nums >= 2:
            # Get the number of possible permutations for this set, valid and invalid
            valid_traversals = pow(2, consecutive_nums - 1)

            # If this set is larger than the max jump (3) we do some shit to eliminate invalid traversals
            # this will always be the number of consecutive ints (eg 2,3,4,5,6 == 5) minus 4 times 2
            # and finally minus 1 (eg 5:1, 6:3, 7:5, 8:7 etc). I have idea why this works.
            if consecutive_nums > 3:
                num_invalid_traversals = ((consecutive_nums - 3) * 2) - 1
                valid_traversals -= num_invalid_traversals

            total_permutations *= valid_traversals
            consecutive_nums = 0
        else:
            consecutive_nums = 0

    print("*"*96)
    print("PART TWO")
    print("{} valid adapter setups to achieve desired joltage.".format(total_permutations))


if __name__ == "__main__":
    part_one(get_input(INPUT_TXT))
    part_two(get_input(INPUT_TXT))
