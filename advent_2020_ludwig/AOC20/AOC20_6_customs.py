# https://adventofcode.com/2020/day/6
# https://www.reddit.com/r/adventofcode/comments/k52psu/2020_day_06_solutions/
# 
# The form asks a series of 26 yes-or-no questions marked a through z. 
# All you need to do is identify the questions for which anyone in your group answers "yes".

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
# This list represents answers from six groups:

# That top group there are 6 questions to which anyone answered "yes": a, b, c, x, y, and z. 
# (Duplicate answers to the same question don't count extra; each question counts at most once.)
# The first group contains one person who answered "yes" to 3 questions: a, b, and c.
# The second group contains three people; combined, they answered "yes" to 3 questions: a, b, and c.
# The third group contains two people; combined, they answered "yes" to 3 questions: a, b, and c.
# The fourth group contains four people; combined, they answered "yes" to only 1 question, a.
# The last group contains one person who answered "yes" to only 1 question, b.
# In this example, the sum of these counts is 6 + 3 + 3 + 3 + 1 + 1 = 17.

# For each group, count the number of questions to which anyone answered "yes". What is the sum of those counts?
# Part 2
# For each group, count the number of questions to which everyone answered "yes". What is the sum of those counts?
# 3 + 3 + 0 + 1 + 1 + 1 = 15

# import operator

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


