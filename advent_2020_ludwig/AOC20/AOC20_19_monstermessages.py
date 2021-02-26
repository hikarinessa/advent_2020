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
part2 = False

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

dict_of_rules = {}
rules_temp = data[0]
messages = data[1]
rules = []

for i, rule in enumerate(rules_temp): # painful deciphering of the input..
    rules.append([])

    if "|" in rule:
        rules[i] = (rule[3:].split("|"))

        for j in range(2):
            rules[i][j] = rules[i][j].split()

        if ":" in rules[i][0]:  # getting of leading :s in higher rule indices
            del rules[i][0][0]

        for j in range(2):
            rules[i][j] = list(map(int, rules[i][j]))  # -- good way to get ints
    
    else:
        rules[i] = rule[3:].split()

        if ":" in rules[i]:
            del rules[i][0]
        
        if rules[i][0].startswith("\""):
            rules[i][0] = rules[i][0].replace("\"", "") # getting rid of the \s in a and b entries
        else:
            rules[i] = list(map(int, rules[i]))
            
        rules[i] = [rules[i]]
        
    dict_of_rules[rulesint[i]] = rules[i]

solved_rules = {}

def solve():  # converts the rule to a string with every number replaced by the related letters (if they exist)
    for i in dict_of_rules:
        rule = dict_of_rules[i]
        pp(i), pp(rule)
        string = ""

        for block_index, block in enumerate(rule):
            solved = 0

            if block_index == 1:
                string += "|"   # inserting pipe back (needed to delete when generating the rules list)

            for ref_index, ref in enumerate(block):
                if ref in solved_rules:
                    ref = solved_rules[ref]
                    
                    if "a" or "b" in ref and len(ref) > 0:
                        string += ref
                        solved += 1
                    
                elif ref == "a" or ref == "b":
                    string += ref 
           
        if len(string) > 0:
            if string.endswith(("|", ",")):
                string = string[:-1]

            if len(string) > 1:
                string = "(" + string + ")"  #wrapping the resulting group in parentheses to use as regex

            solved_rules[i] = string # saving deciphered rule to solved.        
        
        if i in solved_rules:
            pp(solved_rules[i], "solved_rules entry")
    

runs = 0
while runs <= len(dict_of_rules):
    solve()
    runs += 1

pp(solved_rules[0], "rule 0 result", True)

zero = re.compile("^" + solved_rules[0] + "$")
matches = 0
for message in messages:
    zeromatch = zero.match(message)
    if zeromatch is not None:
        matches += 1
pp(matches, "matches", True)
