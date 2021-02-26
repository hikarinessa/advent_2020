# https://adventofcode.com/2020/day/9

data = """35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576"""

debug = False
printit = True
def pp(subject, name = "", override = False): #prints anything with a name as string 
    if debug or printit or override:
        #print("\n", name, ": ", subject)
        print(name, ": ", subject)

print("\n----------------------------------")   # reading file

file = "advent_2020_ludwig/AOC20/data_aoc20_9.txt"
if not debug:
    with open(file) as f:
        data = f.read()
data = [int(s) for s in data.split("\n")]

preamble = 25
if debug:
    preamble = 5

pp(data)
weakness_found = False
weakness = None
i = preamble
while i < len(data):
    settocheck = [n for n in data[i-preamble:i]]
    #pp(settocheck, "set to check")
    currentnr = data[i]
    #pp(data[i], "current number")
    valids = 0
    for index, n in enumerate(settocheck):
        if currentnr - n in settocheck:
            valids += 1
            break
    if valids == 0:
        weakness_found = True
        weakness = currentnr
        break
    i += 1

pp(weakness, "first number with no two numbers adding up to it in the set before:")
print("-------Part II---------")

for index, n in enumerate(data):
    stoplooking = False
    settocheck = [n]
    sumset = 0
    i = index
    while sumset <= weakness:
        settocheck.append(data[i+1])
        sumset = sum(settocheck)
        if sumset == weakness:
            stoplooking = True
            break
        i += 1
    if stoplooking:
        break

settocheck = sorted(settocheck)
encryption_weakness = settocheck[0] + settocheck[-1]
pp(settocheck, "contiguous numbers adding up to weakness")
pp(encryption_weakness, "some of first and last of the contiguous numbers adding up to weakness")



