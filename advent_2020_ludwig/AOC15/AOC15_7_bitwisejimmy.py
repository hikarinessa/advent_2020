# Each wire has an identifier (some lowercase letters) and can carry a 16-bit signal (a number from 0 to 65535). 
# A signal is provided to each wire by a gate, another wire, or some specific value. Each wire can only 
# get a signal from one source, but can provide its signal to multiple destinations. 
# A gate provides no signal until all of its inputs have a signal.

# The included instructions booklet describes how to connect the parts together: 
# x AND y -> z means to connect wires x and y to an AND gate, and then connect its output to wire z.

# For example:

# 123 -> x means that the signal 123 is provided to wire x.
# x AND y -> z means that the bitwise AND of wire x and wire y is provided to wire z.
# p LSHIFT 2 -> q means that the value from wire p is left-shifted by 2 and then provided to wire q.
# NOT e -> f means that the bitwise complement of the value from wire e is provided to wire f.
# Other possible gates include OR (bitwise OR) and RSHIFT (right-shift). If, for some reason, 
# you'd like to emulate the circuit instead, almost all programming languages 
# (for example, C, JavaScript, or Python) provide operators for these gates.

# For example, here is a simple circuit:
import operator

data ="""123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i"""

#After it is run, these are the signals on the wires:
# d: 72
# e: 507
# f: 492
# g: 114
# h: 65412
# i: 65079
# x: 123
# y: 456

# In little Bobby's kit's instructions booklet (provided as your puzzle input), what signal is ultimately provided to wire a?

#  Operator      Example	Meaning
#  &	         a & b	    Bitwise AND
#  |	         a | b   	Bitwise OR
#  ^	         a ^ b	    Bitwise XOR (exclusive OR)
#  ~	          ~a	    Bitwise NOT
#  <<	         a << n	    Bitwise left shift
#  >>	         a >> n	    Bitwise right shift

debug = False

def pp(subject, name): #prints anything with a name as string 
    if debug or True:
        print()
        print(f"{name}: {subject}")



print("\n----------------------------------")   # reading file
file = "advent_2020_ludwig/AOC15/littlejimmysbits.txt"
if not debug:
    with open(file) as f:
        data = f.read()
data = data.splitlines()
pp(data, "data")

ddd = {}
fff = []

for s in data:
    fff.append(s.split())

    #s, x = s.split(sep=" -> ")
    #ddd[x] = s

for l in fff:
    l.pop(-2)   

fff1, fff2 = [], []

for l in fff:
    if len(l[-1]) == 1:
        fff1.append(l)
    else:
        fff2.append(l)

fff1.sort(key=operator.itemgetter(-1))
fff2.sort(key=operator.itemgetter(-1))
fff = fff1
for i in fff2:    
    fff.append(i)

last = None

if "a" in fff[0]:
    last = fff[0]
    fff.pop(0)

pp(fff, "fff")
pp(last, "last")

def evaluate(i, round):
    #x = i.index()
    if len(i) == 2:
        ddd[i[-1]] = int(i[0])
        if round == "round2":
            if i[-1] == "b":
                ddd[i[-1]] = a
    elif len(i) == 3:
        ddd[i[-1]] = ~ddd[i[1]] & 0xffff
    elif i[1] == "RSHIFT":
        ddd[i[-1]] = ddd[i[0]] >> int(i[2])
    elif i[1] == "LSHIFT":
        ddd[i[-1]] = ddd[i[0]] << int(i[2])
    elif i[1] == "OR":
        ddd[i[-1]] = ddd[i[0]] | ddd[i[2]]
    elif i[1] == "AND":
        if i[0].isdigit():
            ddd[i[-1]] = int(i[0]) & ddd[i[2]]
        else:
            ddd[i[-1]] = ddd[i[0]] & ddd[i[2]]

for i in fff:
    evaluate(i, "round1")

pp(ddd, "ddd")

for i in fff:
    pp(i, "line")
    for x in i:
        if x in ddd:
            print(ddd[x], end=", ")

#ddd["a"] = ddd["lx"]
a = ddd["lx"]
print()
print("round1:")
pp(a, "a is")

for i in fff:
    evaluate(i, "round2")

pp(ddd, "ddd")

for i in fff:
    pp(i, "line")
    for x in i:
        if x in ddd:
            print(ddd[x], end=", ")

ddd["a"] = ddd["lx"]
print()
print("round2:")
pp(ddd["a"], "a is")
    

print()