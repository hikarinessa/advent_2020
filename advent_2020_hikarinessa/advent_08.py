import re

with open('advent_08_input.txt', 'r') as raw_input:
    INPUT = raw_input.read().splitlines()  # ['nop +81', 'acc -17', 'jmp +1', 'acc +31', ...]


# Immediately before any instruction is executed a second time, what value is in the accumulator?
def is_infinite_and_accumulator(instructions):
    accumulator = 0
    instr_index = 0
    instruction_list =[]

    while instr_index not in instruction_list:
        if instr_index >= len(instructions):
            return False, accumulator
        instruction_list.append(instr_index)
        instruction, _space, instruction_number = instructions[instr_index].partition(' ')
        if instruction == 'nop':
            instr_index += 1
        elif instruction == 'acc':
            accumulator += int(instruction_number)
            instr_index += 1
        elif instruction == 'jmp':
            instr_index += int(instruction_number)

    return True, accumulator


def swap_jmp_nop(instruction):
    """Gets an instruction and swaps jmp for nop or nop for jmp"""
    if instruction[:3] == 'jmp':
        return 'nop' + instruction[3:]
    elif instruction[:3] == 'nop':
        return 'jmp' + instruction[3:]
    else:
        return instruction


# Fix the program so that it terminates normally by changing exactly one jmp (to nop) or nop (to jmp).
# What is the value of the accumulator after the program terminates?
def correct_permutation(instructions):
    jumps_and_nops = []
    for i in range(len(instructions)):
        if instructions[i][:3] != 'acc':
            jumps_and_nops.append(i)

    is_infinite = True
    accumulator = 0
    while is_infinite and len(jumps_and_nops) != 0:
        p = jumps_and_nops.pop()
        instructions_permutation = instructions.copy()
        instructions_permutation[p] = swap_jmp_nop(instructions[p])
        is_infinite, accumulator = is_infinite_and_accumulator(instructions_permutation)

    return accumulator  # 1 returns the accumulator


print("First Part:", is_infinite_and_accumulator(INPUT)[1])  # 1553
print("Second Part:", correct_permutation(INPUT))  # 1877
