# https://adventofcode.com/2020/day/14

# The initialization program (your puzzle input) can either update the bitmask or write a value to memory. 
# Values and memory addresses are both 36-bit unsigned integers. For example, ignoring bitmasks for a moment, 
# a line like mem[8] = 11 would write the value 11 to memory address 8.

# The bitmask is always given as a string of 36 bits, written with the most significant bit (representing 2^35) 
# on the left and the least significant bit (2^0, that is, the 1s bit) on the right. The current bitmask is 
# applied to values immediately before they are written to memory: a 0 or 1 overwrites the corresponding bit 
# in the value, while an X leaves the bit in the value unchanged.

data = """mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0"""
part2 = True
if part2:
    data="""mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1"""

# To initialize your ferry's docking program, you need the sum of all values left in 
# memory after the initialization program completes. (The entire 36-bit address space begins 
# initialized to the value 0 at every address.) In the above example, only two values in memory are not zero - 
# 101 (at address 7) and 64 (at address 8) - producing a sum of 165.

# Execute the initialization program. What is the sum of all values left in memory 
# after it completes? (Do not truncate the sum to 36 bits.)

from itertools import product

debug = False
printit = False
def pp(subject, name = "", override = False): #prints anything with a name as string 
    if debug or printit or override:
        #print("\n", name, ": ", subject)
        print(name, ": ", subject)
def ppp(subject, name = "", override = False): #prints anything with a name as string 
    if debug or printit or override:
        #print("\n", name, ": ", subject)
        print(name, ": ")
        for item in subject:
            print(item)

print("\n----------------------------------")   # reading file

file = "AOC20/data_aoc20_14.txt"
if not debug:
    with open(file) as f:
        data = f.read()
data = [s.split(sep = " = ") for s in data.split("\n")]
datasplit = []
datamasked = []
ppp(data)
for s in data:
    if s[0] != "mask":
        s[0] = s[0][4:-1]
        s[1] = int(s[1])
    datasplit.append(s)
ppp(datasplit, "SPLIT DATA")

def bitmask(value, mask):
    final = ""
    value = bin(value)[2:].zfill(36)
    for i, c in enumerate(value):
        if mask[i] == "1":
            final += "1"
        elif mask[i] == "0":
            final += "0"
        else:
            final += c
    return int(final, 2)

memory = {}
mask = ""
for id, val in datasplit:
    if id == "mask":
        mask = val
    else:
        memory[id] = bitmask(val, mask)
    datamasked.append([id, val])

ppp(datamasked, "MASKED DATA")
pp(memory, "MEMORY DICT")

result = 0
for i in memory:
    result += memory[i]
pp(result, "RESULT PART I", True)

#------------------part2 



def bitmaskadd(id, mask):
    final = []
    finals = []
    addresses = []
    id = bin(int(id))[2:].zfill(36)
    pp(id, "id")
    for i, c in enumerate(id):
        if mask[i] == "1":
            final.append(["1"])
        elif mask[i] == "0":
            final.append([c])
        else:
            final.append(["0", "1"])
    
    finals = [''.join(c) for c in product(*final)] # das fucking sternchen !!!!!
    
    ppp(finals, "finals")
    for address in finals:
        addresses.append(int(address))

    return addresses

memorypart2 = {}

for id, val in datasplit:
    if id == "mask":
        mask = val
    else:
        value = val
        for address in bitmaskadd(id, mask):
            memorypart2[address] = val

result = 0
for i in memorypart2:
    result += memorypart2[i]
pp(result, "RESULT", True)

