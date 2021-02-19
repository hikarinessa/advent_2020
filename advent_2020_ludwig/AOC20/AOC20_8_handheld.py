# https://adventofcode.com/2020/day/8
# https://www.reddit.com/r/adventofcode/comments/k52psu/2020_day_08_solutions/

# The boot code is represented as a text file with one instruction per line of text. 
# Each instruction consists of an operation (acc, jmp, or nop) and an argument (a signed number like +4 or -20).
# acc increases or decreases a single global value called the accumulator by the value given in the argument. 
# For example, acc +7 would increase the accumulator by 7. The accumulator starts at 0. After an acc instruction, 
# the instruction immediately below it is executed next.
# jmp jumps to a new instruction relative to itself. The next instruction to execute is found using the 
# argument as an offset from the jmp instruction; for example, jmp +2 would skip the next instruction, 
# jmp +1 would continue to the instruction immediately below it, and jmp -20 would cause the instruction 20 lines 
# above to be executed next.
# nop stands for No OPeration - it does nothing. The instruction immediately below it is executed next.
# For example, consider the following program:

data = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6"""

# These instructions are visited in this order:
# nop +0  | 1
# acc +1  | 2, 8(!)
# jmp +4  | 3
# acc +3  | 6
# jmp -3  | 7
# acc -99 |
# acc +1  | 4
# jmp -4  | 5
# acc +6  |
# First, the nop +0 does nothing. Then, the accumulator is increased from 0 to 1 (acc +1) 
# and jmp +4 sets the next instruction to the other acc +1 near the bottom. 
# After it increases the accumulator from 1 to 2, jmp -4 executes, setting the next 
# instruction to the only acc +3. It sets the accumulator to 5, and jmp -3 causes the program to 
# continue back at the first acc +1.

# This is an infinite loop: with this sequence of jumps, the program will run forever. The moment the 
# program tries to run any instruction a second time, you know it will never terminate.
# Immediately before the program would run an instruction a second time, the value in the accumulator is 5.
# Run your copy of the boot code. Immediately before any instruction is executed a second time, what value is in the accumulator?

import copy
from os import error

debug = False
printit = False
def pp(subject, name = "", override = False): #prints anything with a name as string 
    if debug or printit or override:
        #print("\n", name, ": ", subject)
        print(name, ": ", subject)

print("\n----------------------------------")   # reading file

file = "advent_2020_ludwig/AOC20/data_aoc20_8.txt"
if not debug:
    with open(file) as f:
        data = f.read()
data = [[t for t in s.split()] for s in data.split("\n")]
for index, s in enumerate(data):
    data[index][1] = int(data[index][1]) 

pp(data)

# instructions = []
# index = 0
accumulator = 0
part2 = True

def checkboot(bootcode):
    global accumulator
    print("checking...")
    accumulator = 0
    instructions = []
    abletoterminate = False
    index = 0
    #accumulator = 0
    while index not in instructions:
        instructions.append(index)
        try:
            d = bootcode[index]
        except IndexError:
            abletoterminate = True
            break
        pp(d, "current instruction")
        if d[0] == "acc":
            accumulator += d[1]
            pp(accumulator, "instruction is acc, accumulator increased to")
            index += 1
        if d[0] == "nop":
            pp(d[0], "is nop, moving on...")
            index += 1
        if d[0] == "jmp":
            pp(d[1], "instruction is jump. jumping to")
            index = index + d[1]
        
        pp(instructions, "list of visited instructions")
    if index == len(bootcode)-1 or abletoterminate:
        return True
    else:
        return False

checkboot(data)
pp(accumulator, "The accumulator's value is", True)
print("-------------------------- part 2")

if part2:
    for index, s in enumerate(data):
        datatemp = copy.deepcopy(data)
        pp(datatemp, "data reset")
        pp(s, "current line to check")
        solutionfound = False
        if s[0] == "jmp":
            pp(s[0], "line has jump, changing to nop")
            datatemp[index][0] = "nop"
            pp(datatemp, "changed data")
            if checkboot(datatemp):
                
                solutionfound = True
                pp(solutionfound, "Solution found!")
        elif s[0] == "nop":
            pp(s[0], "line has nop, changing to jump")
            datatemp[index][0] = "jmp"
            pp(datatemp, "changed data")
            if checkboot(datatemp):
                solutionfound = True
                pp(solutionfound, "Solution found!")
        if solutionfound:
            break

pp(accumulator, "The accumulator's value is", True)
