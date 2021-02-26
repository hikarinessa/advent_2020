# https://adventofcode.com/2020/day/19

data = """0: 4 1 5
1: 2 3 | 3 2
2: 4 4 | 5 5
3: 4 5 | 5 4
4: "a"
5: "b"

ababbb
bababa
abbbab
aaabbb
aaaabbb"""

import re
debug = False
printit = False
part2 = True


def pp(subject, name = "", override = False): #prints anything with a name as string 
    if debug or printit or override:
        #print("\n", name, ": ", subject)
        print()
        print(name, ": ", subject)
def ppp(subject, name = "", override = False, isDictionary=False): #prints list entries
    if debug or printit or override:
        #print("\n", name, ": ", subject)
        print()
        print(name, ": ")
        for item in subject:
            if isDictionary:
                print(item, ":", end="")
                print(subject[item])
            else:
                print(item)

print("\n----------------------------------")   # reading file
if part2 and debug:
    file = "advent_2020_ludwig/AOC20/data_aoc20_19_b.txt"

file = "advent_2020_ludwig/AOC20/data_aoc20_19.txt"
if not debug:
    with open(file) as f:
        data = f.read()

if part2:
    data = data.replace("8: 42", "8: 42 | 42 8")
    data = data.replace("11: 42 31", "11: 42 31 | 42 11 31")
data = [s.split("\n") for s in data.split("\n\n")]
rulesint = []
for i in data[0]:
    rulesint.append(i.split(": "))
for index, i in enumerate(rulesint):
    rulesint[index] = int(rulesint[index][0])

drules = {}
rulestemp = data[0]
messages = data[1]
rules = []

for i, rule in enumerate(rulestemp):
    rules.append([])

    if "|" in rule:
        rules[i] = (rule[3:].split("|"))

        for j in range(2):
            rules[i][j] = rules[i][j].split()

        if ":" in rules[i][0]:
            del rules[i][0][0]

        for j in range(2):
            rules[i][j] = list(map(int, rules[i][j]))  # -- good way to get ints
    
    else:
        rules[i] = rule[3:].split()

        if ":" in rules[i]:
            del rules[i][0]
        
        if rules[i][0].startswith("\""):
            rules[i][0] = rules[i][0].replace("\"", "")
        else:
            rules[i] = list(map(int, rules[i]))
            
        rules[i] = [rules[i]]
        
    drules[rulesint[i]] = rules[i]


srules = {}
def solve():
    for i in drules:
        rule = drules[i]
        pp(i), pp(rule)
        string = ""

        for block_index, block in enumerate(rule):
            solved = 0

            if block_index == 1:
                string += "|"

            for ref_index, ref in enumerate(block):
                if ref in srules:
                    ref = srules[ref]
                    
                    if "a" or "b" in ref and len(ref) > 0:
                        string += ref
                        solved += 1
                    
                        
                elif ref == "a" or ref == "b":
                    if i in srules:
                        string += ref 
                    else:
                        string += ref 
           
        if len(string) > 0:
            if string.endswith(("|", ",")):
                string = string[:-1]

            if len(string) > 1:
                string = "(" + string + ")"   

            srules[i] = string        
        
        if i in srules:
            pp(srules[i], "srules entry")
    

runs = 0
while runs <= len(drules):
    solve()
    runs += 1

pp(srules[0], "rule 0 result", True)

zero = re.compile("^" + srules[0] + "$")
matches = 0
for message in data[1]:
    zeromatch = zero.match(message)
    if zeromatch is not None:
        matches += 1
pp(matches, "matches", True)
