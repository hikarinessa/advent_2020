# https://adventofcode.com/2020/day/19
import re
import os
import sys
import itertools
from utilities import *

with open(os.path.join(sys.path[0], "Inputs/advent_19_input.txt"), "r") as raw_input:
    INPUT = raw_input.read().split("\n\n")
INPUT_INSTR = INPUT[0].splitlines()
INPUT_MSGS = INPUT[1].splitlines()

TEST_INSTR = ['0: 4 1 5',
              '1: 2 3 | 3 2',
              '4: "a"',
              '2: 4 4 | 5 5',
              '3: 4 5 | 5 4',
              '5: "b"',
              '6: 2 4 | 5 3']
TEST_MSGS = ['ababbb',
             'bababa',
             'abbbab',
             'aaabbb',
             'aaaabbb']


class Instruction:
    def __init__(self, instruction):
        self.raw = re.match('(\d+): ["]?([0-9a-b\|\s]+)', instruction)
        self.number = int(self.raw.group(1))
        self.content = self.raw.group(2)
        self.is_ready = self.content == 'a' or self.content == 'b'
        self.values = self.content if self.is_ready else []                      # ['ab', 'ba']
        self.all_ref = list(set([int(i) for i in re.findall('(\d+)', self.content)]))  # ['4', '5']
        self.references = [] if self.is_ready else self.list_references()              # [['4', '5'], ['5', '4']]

    def list_references( self ):
        split = self.content.split(" ")
        ref_list = []
        temp_list = []
        while len(split) > 0:
            i = split.pop(0)
            if i != "|":
                temp_list.append(int(i))
            else:
                ref_list.append(temp_list)
                temp_list = []
        ref_list.append(temp_list)
        return ref_list

    def replace_reference( self , ref, val):
        for i, reference in enumerate(self.references):
            if isinstance(reference, list):
                for j, reference2 in enumerate(reference):
                    if reference2 == ref:
                        self.references[i][j] = val
            else:
                self.references[i] = val

    def update_values( self ):
        for reference in self.references:
            if not any(isinstance(x, list) for x in reference):
                self.values.append(''.join([str(elem) for elem in reference]))
            elif all(isinstance(x, list) for x in reference) and len(reference) == 1:
                self.values = reference[0]
            elif all(isinstance(x, list) for x in reference):
                a = reference[0]
                b = reference[1]
                permutations = list(map(''.join, itertools.chain(itertools.product(a, b), itertools.product(b, a))))
                self.values = list(set(permutations))
            elif len(reference) == 3 and isinstance(reference[0], str) and isinstance(reference[1], list):
                for i in reference[1]:
                    self.values.append(reference[0] + i + reference[2])
            elif isinstance(reference[0], str) and isinstance(reference[1], list):
                for i in reference[1]:
                    self.values.append(reference[0] + i)
            elif isinstance(reference[1], str) and isinstance(reference[0], list):
                for i in reference[0]:
                    self.values.append(i + reference[1])
            else:
                print("#"*90)

        # print(self.number, "updating values", self.values)


    # region -------------------- sample Instructions --------------------
    # 3: 4 5 | 5 4
    # {'raw': <re.Match object; span=(0, 12), match='3: 4 5 | 5 4'>,
    #  'number': 3,
    #  'content': '4 5 | 5 4',
    #  'is_ready': False,
    #  'values': []}
    #  'all_ref': [4, 5],
    #  'references': [[4, 5], [5, 4]],
    # 4: "a"
    # {'raw': <re.Match object; span=(0, 5), match='4: "a'>,
    #  'number': 4,
    #  'content': 'a',
    #  'is_ready': True,
    #  'values': ['a']}
    #  'all_ref': [],
    #  'references': [],
    # endregion ----------------------------------------------------------


def first_part(my_instr, my_msgs):
    my_dict = {}
    for line in my_instr:
        new_instr = Instruction(line)
        my_dict[new_instr.number] = new_instr

    while not my_dict[0].is_ready:  # if instruction 0 is ready means it's populated with all possibilities
        for rule in my_dict.keys():  # the current object
            if not my_dict[rule].all_ref:
                my_dict[rule].is_ready = True
                if not my_dict[rule].values:
                    my_dict[rule].update_values()
            else:
                for ref in my_dict[rule].all_ref:
                    if my_dict[ref].is_ready:
                        my_dict[rule].all_ref.remove(ref)
                        my_dict[rule].replace_reference(my_dict[ref].number, my_dict[ref].values)

    zero_dict = {i: 0 for i in my_dict[0].values}
    counter = 0
    for message in my_msgs:
        if message in zero_dict.keys():
            counter += 1
    return counter


if __name__ == "__main__":
    start_time = start_timer()
    print("First part:", first_part(INPUT_INSTR, INPUT_MSGS))  #
    # print("First part:", first_part(TEST_INSTR, TEST_MSGS, debug=False))  #
    print_elapsed_time(start_time)
    # print("*"*96)
    # start_time = start_timer()
    # print("Second part:", main(INPUT))
    # print_elapsed_time(start_time)