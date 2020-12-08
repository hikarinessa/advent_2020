import os
import sys

INPUT_TXT = "../Input/08_HandheldHalting.txt"
TEST_INPUT_TXT = "../Input/08_HandheldHalting_TestInput.txt"
CMD_ACCUMULATE = "acc"
CMD_JUMP = "jmp"
CMD_NO_OPERATION = "nop"


def get_input():
    with open(os.path.join(sys.path[0], INPUT_TXT), "r") as my_input:
        return my_input.read().splitlines()


def get_test_input():
    with open(os.path.join(sys.path[0], TEST_INPUT_TXT), "r") as my_input:
        return my_input.read().splitlines()


def execute(line, acc, i):
    cmd, _space, num = line.partition(" ")
    if cmd == CMD_ACCUMULATE:
        acc += int(num)
        return acc, i+1
    elif cmd == CMD_JUMP:
        return acc, i+int(num)
    elif cmd == CMD_NO_OPERATION:
        return acc, i+1
    else:
        return False, False


def run_program(program):
    i = 0
    acc = 0
    lines_executed = list()
    while True:
        if i == len(program) or i == -1:
            return True, acc  # Exited successfully, return True

        if i not in lines_executed:
            lines_executed.append(i)
        else:
            return False, acc  # Infinite loop detected, return False

        acc, i = execute(program[i], acc, i)


def part_one(program):
    _success, acc = run_program(program)
    print("*"*96)
    print("PART ONE")
    print("Infinite loop detected, acc = {}".format(acc))


def part_two(program: list):
    acc = 0
    flip_index = 0
    success = False
    while success is False:
        new_program = program.copy()
        line_to_edit = new_program[flip_index]

        cmd = line_to_edit.partition(" ")[0]
        if cmd == CMD_JUMP:
            new_program[flip_index] = line_to_edit.replace(CMD_JUMP, CMD_NO_OPERATION)
        elif cmd == CMD_NO_OPERATION:
            new_program[flip_index] = line_to_edit.replace(CMD_NO_OPERATION, CMD_JUMP)
        else:
            flip_index += 1
            continue

        success, acc = run_program(new_program)
        flip_index += 1

    print("*"*96)
    print("PART TWO")
    print("Program exited successfully, acc = {}".format(acc))


if __name__ == "__main__":
    part_one(get_input())
    part_two(get_input())
