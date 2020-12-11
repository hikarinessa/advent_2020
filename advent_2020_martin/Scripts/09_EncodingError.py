import os
import sys

INPUT_TXT = "../Input/09_EncodingError.txt"
TEST_INPUT_TXT = "../Input/09_EncodingError_TestInput.txt"


def get_input(txt):
    with open(os.path.join(sys.path[0], txt), "r") as my_input:
        return [int(line) for line in my_input.read().splitlines()]


def num_is_valid(num: int, previous_nums: list):
    # This is ugly but it prevents adding a num to itself, without disqualifying duplicates
    for i, n1 in enumerate(previous_nums):
        for j, n2 in enumerate(previous_nums):
            if i == j:
                continue
            elif n1 + n2 == num:
                return True
    return False


def part_one(numbers: list, preamble_length: int):
    for i, num in enumerate(numbers[preamble_length:]):
        previous_nums = numbers[i:i+preamble_length]
        if not num_is_valid(num, previous_nums):
            print("*"*96)
            print("PART ONE")
            print("{} is not a valid entry!".format(num))
            return num


def part_two(numbers: list, target: int):
    for i, num in enumerate(numbers):
        num_acc, min_num, max_num = num, num, num
        for other_num in numbers[i+1:]:
            min_num = min(min_num, other_num)
            max_num = max(max_num, other_num)
            num_acc += other_num
            if num_acc == target:
                print("*"*96)
                print("PART TWO")
                print("Min: {}, Max: {}, Sum: {}".format(min_num, max_num, min_num+max_num))
            elif num_acc > target:
                break


if __name__ == "__main__":
    target = part_one(get_input(INPUT_TXT), 25)
    part_two(get_input(INPUT_TXT), target)
