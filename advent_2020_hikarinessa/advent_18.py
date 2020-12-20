# https://adventofcode.com/2020/day/18
from utilities import *
import os
import sys
import re
import pyparsing

with open(os.path.join(sys.path[0], "Inputs/advent_18_input.txt"), "r") as raw_input:
    INPUT = raw_input.read().splitlines()

TEST_INPUT = ['1 + 2 * 3 + 4 * 5 + 6',                              # 71
              '1 + (2 * 3) + (4 * (5 + 6))',                        # 51
              '2 * 3 + (4 * 5)',                                    # 26
              '5 + (8 * 3 + 9 + 3 * 4 * 3)',                        # 437
              '5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))',          # 12240
              '((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2']    # 13632


def parse_operations(my_input):
    """Receives a list of numbers and operators, without parenthesis"""
    operators = ['+', '*']
    operation = ''
    result = 0
    while len(my_input) > 0:
        item = my_input.pop(0)
        if item not in operators and operation is '':  # is the first number
            result = int(item)
        elif item in operators:
            operation = item
        elif item not in operators:  # is a number, but not the first
            if operation == '+':
                result += int(item)
            elif operation == '*':
                result *= int(item)
    return result


def prep_input(my_input):
    """Formats an initial string to a list of nested parenthesis"""
    content = pyparsing.Word(pyparsing.alphanums) | '+' | '*'
    nest = pyparsing.nestedExpr('(', ')', content=content)
    return nest.parseString("(" + my_input + ")")[0].asList()


def main(my_input, debug):
    result = 0
    while len(my_input) > 0:
        temp_result = 0
        row = my_input.pop(0)
        row = prep_input(row)
        has_nest = True
        temp_result = 0
        if not any(isinstance(x, list) for x in row):
            temp_result += parse_operations(row)
            has_nest = False
        while has_nest:
            for i, val in enumerate(row):
                if isinstance(val, list):
                    if not any(isinstance(x, list) for x in val):
                        row[i] = parse_operations(val)
                    else:
                        for j, val2 in enumerate(val):
                            if isinstance(val2, list):
                                if not any(isinstance(x, list) for x in val2):
                                    val[j] = parse_operations(val2)
                                else:
                                    print("nested parenthesis")
            if not any(isinstance(x, list) for x in row):
                temp_result += parse_operations(row)
                has_nest = False
        if debug: print(temp_result)
        result += temp_result

    return result


if __name__ == "__main__":
    start_time = start_timer()
    print("First part:", main(INPUT, debug=False))  # 11004703763391
    print_elapsed_time(start_time)
    print("*"*96)
    start_time = start_timer()
    # print("Second part:", main(INPUT))
    print_elapsed_time(start_time)
