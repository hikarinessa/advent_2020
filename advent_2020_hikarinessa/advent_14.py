# https://adventofcode.com/2020/day/14
import os
import sys
import re
from utilities import *

with open(os.path.join(sys.path[0], "Inputs/advent_14_input.txt"), "r") as raw_input:
    INPUT = raw_input.read().splitlines()


def prep_input(my_input):
    """Returns a list with all the masks, and a list of lists (one per mask) with the instructions"""
    mask_list = []
    instruction_list = []
    temp_key = -1

    for row in my_input:
        if row[:4] == "mask":
            mask_list.append(row[7:])
            temp_key += 1
        else:
            if len(instruction_list) <= temp_key:
                instruction_list.append([row])
            else:
                instruction_list[temp_key].append(row)

    return mask_list, instruction_list


# Part 1 ---------------------------------------------------------------------------------------
def parse_instruction_val(instruction):
    instr = re.search("\[(\d+)\] = (\d+)", instruction)
    mem = int(instr.group(1))
    val = str(bin(int(instr.group(2))))[2:]
    while len(val) < 36:
        val = '0' + val

    return mem, val


def mask_and_write_val(dic, mask, mem, val):
    for i, char in enumerate(mask):
        if char == '0' or char == '1':
            value = val[:i] + char + val[i + 1:]

    dic[mem] = value


def first_part(my_input):
    mask_list, instruction_list = prep_input(my_input)
    mem_dict = {}
    for i, mask in enumerate(mask_list):
        for instr in instruction_list[i]:
            mem, val = parse_instruction_val(instr)
            mask_and_write_val(mem_dict, mask, mem, val)

    added_values = 0
    for val in mem_dict.values():
        added_values += int(val, 2)

    return added_values


# Part 2 ---------------------------------------------------------------------------------------
# TODO Cleanup and optimize the code
def parse_instruction_mem(instruction):
    instr = re.search("\[(\d+)\] = (\d+)", instruction)
    val = int(instr.group(2))
    mem = str(bin(int(instr.group(1))))[2:]
    while len(mem) < 36:
        mem = '0' + mem

    return mem, val


def mask_mem(mask, mem):
    for i, char in enumerate(mask):
        if char == 'X' or char == '1':
            mem = mem[:i] + char + mem[i + 1:]
    return mem


def store_val(mem_dict, mem, val):
    var = '1'*(mem.count("X"))
    var = int(var, 2)
    for i in range(var+1):
        bina = str(bin(i)[2:])
        while len(bina) < len(bin(var)[2:]):
            bina = '0' + bina
        bina_count = 0
        new_mem = mem
        for i, char in enumerate(mem):
            if char == 'X':
                new_mem = new_mem[:i] + bina[bina_count] + new_mem[i + 1:]
                bina_count += 1
        mem_dict[new_mem] = val
        # print(mem, new_mem)


def second_part(my_input):
    mask_list, instruction_list = prep_input(my_input)
    mem_dict = {}

    for i, mask in enumerate(mask_list):
        for instr in instruction_list[i]:
            mem, val = parse_instruction_mem(instr)
            mem = mask_mem(mask, mem)
            store_val(mem_dict, mem, val)

    added_values = 0
    for val in mem_dict.values():
        added_values += val

    return added_values

if __name__ == "__main__":
    start_time = start_timer()
    print("First part:", first_part(INPUT))  # 14954914379452
    print_elapsed_time(start_time)
    print("*"*96)
    start_time = start_timer()
    print("Second part:", second_part(INPUT))  # 3415488160714
    print_elapsed_time(start_time)

