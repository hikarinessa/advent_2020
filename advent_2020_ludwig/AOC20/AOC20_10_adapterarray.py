# https://adventofcode.com/2020/day/10

data = """16
10
15
5
1
11
7
19
6
12
4"""

from more_itertools import consecutive_groups

debug = False
printit = True
def pp(subject, name = "", override = False): #prints anything with a name as string 
    if debug or printit or override:
        #print("\n", name, ": ", subject)
        print(name, ": ", subject)

print("\n----------------------------------")   # reading file

file = "advent_2020_ludwig/AOC20/data_aoc20_10.txt"
if not debug:
    with open(file) as f:
        data = f.read()
data = [int(s) for s in data.split("\n")]

data.append(0)
data = sorted(data)
device_joltage = data[-1] + 3
data.append(device_joltage)
pp(data)

ones, twos, threes = [], [], []
pp(len(data[1:]), "length of data")

for i in range(len(data[1:])):
    current = data[i+1]
    #pp(current, "current")
    previous = data[i]
    #pp(previous, "previous")
    difference = current - previous
    #pp(difference, "difference")
    if difference == 1:
        ones.append(current)
    elif difference == 2:
        twos.append(current)
    elif difference == 3:
        threes.append(current)
    else:
        print("somethings wrong")
        break
        
pp(len(ones), "number of 1 jolt differences", True)
pp(len(twos), "number of 2 jolt differences", True)
pp(len(threes), "number of 3 jolt differences", True)

pp(len(ones)*len(threes), "product of numbers of 1 and 3 jolt differences", True)

skippables = []
tripleones, doubleones, onetwos, twoones = 0,0,0,0
permutations = 1

for index, n in enumerate(data[1:-1], start=1):
    if n in threes:
        pass
    elif n in twos:
        if data[index+1] in ones:
            skippables.append(n)
            twoones+=1
    elif n in ones:
        if data[index+1] in ones:
            doubleones+=1
            skippables.append(n)
        elif data[index+1] in twos:
                skippables.append(n)
                twoones+=1

#skippables = list(dict.fromkeys(skippables))
#permutations = 2 ** len(skippables)
pp(doubleones, "double ones")
pp(tripleones, "triple ones")
pp(skippables, "skippables")
pp(len(skippables), "number of skippables")

skippable_sections = []
sections_index = 0

for group in consecutive_groups(skippables):
    skippable_sections.append(list(group))

for section in skippable_sections:
    x = len(section)
    if x == 5:       # --------hardcoded solutions :DDDD
        y = 19
    if x == 4:
        y = 14
    if x == 3:
        y = 7
    if x == 2:
        y = 4
    if x == 1:
        y = 2
    permutations *= y

pp(skippable_sections, "array of ones sections")
pp(permutations, "permutations")
'''
123
1
2
3
12
13
23

1234
12
1 3
1  4
123
12 4
1 34
 2
 23
 2 4
 234
  3
  34
   4

12345
1  45
1 3 5
12  5
1  4
1 34
12 4
1 3
123
 23
 234
 2345
 2  5
 2 45
 23 5
  3
  34
  345
  3 5

'''

helper = 19208
helper = 2**(5-1)-5
helper = 7*7*4*2*7*7

pp(helper, "helper")
'''
0123
023
013
03

012345 
02345
01345
01245
01235
0145
0245
0345
0125
0135
035
025

'''
# (0), 1, 4, 5, 6, 7, 10, 11, 12, 15, 16, 19, (22)
# (0), 1, 4, 5, 6, 7, 10, 12, 15, 16, 19, (22)
# (0), 1, 4, 5, 7, 10, 11, 12, 15, 16, 19, (22)
# (0), 1, 4, 5, 7, 10, 12, 15, 16, 19, (22)
# (0), 1, 4, 6, 7, 10, 11, 12, 15, 16, 19, (22)
# (0), 1, 4, 6, 7, 10, 12, 15, 16, 19, (22)
# (0), 1, 4, 7, 10, 11, 12, 15, 16, 19, (22)
# (0), 1, 4, 7, 10, 12, 15, 16, 19, (22)
        
# 8 -- 3
# 19208 -- 15

# 2**13