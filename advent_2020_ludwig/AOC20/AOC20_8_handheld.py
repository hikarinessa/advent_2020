# https://adventofcode.com/2020/day/8

data = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6"""

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
        except IndexError:  # read somewhere later using exceptions for flow control is not very posh 
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
        datatemp = copy.deepcopy(data) # keep running into this copy trap...
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
