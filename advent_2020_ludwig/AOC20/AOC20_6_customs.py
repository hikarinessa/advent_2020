# https://adventofcode.com/2020/day/6

data = """abcx
abcy
abcz

abc

a
b
c

ab
ac

a
a
a
a

b"""

debug = False 
printit = True
def pp(subject, name = ""): #prints anything with a name as string 
    if debug or printit:
        print(name, ": ", subject)

print("\n----------------------------------")   # reading file

file = "advent_2020_ludwig/AOC20/data_aoc20_6.txt"
if not debug:
    with open(file) as f:
        data = f.read()
data = [s.replace("\n", " ") for s in data.split("\n\n")]
pp(data)
sumofyesses = 0
sumofunanimousyesses = 0

for i in data:
    peopleingroup = i.count(" ")+1
    pp(peopleingroup, "people in group")
    i = i.replace(" ", "")
    sumofyesses += len(set(i))
    group = [i]
    group.append(set(i))
    group.append(peopleingroup)
    x = 0
    for c in group[1]:
        pp(c, "-character in set")
        answercount = group[0].count(c)
        pp(answercount, "occurence of character")
        if answercount == peopleingroup:
            sumofunanimousyesses += 1
            
    pp(sumofunanimousyesses, "sum")
    pp(group, "group")

print(sumofunanimousyesses, "total unanimous yesses")
print(sumofyesses, "total yesses")


