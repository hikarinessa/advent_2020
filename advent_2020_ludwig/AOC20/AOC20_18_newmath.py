# https://adventofcode.com/2020/day/18

data = """1 + 2 * 3 + 4 * 5 + 6
1 + (2 * 3) + (4 * (5 + 6))
2 * 3 + (4 * 5)
5 + (8 * 3 + 9 + 3 * 4 * 3)
5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))
((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"""

data = "4 + (5 + (5 * 5 + 3 + 2) + (6 + 4 * 9 * 2 * 8) * 6 + (7 * 5 * 2) * (2 * 8 * 2)) + (8 * 7 + 7) * 6 * 9 * (5 + 9)"

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

file = "advent_2020_ludwig/AOC20/data_aoc20_18.txt"
if not debug:
    with open(file) as f:
        data = f.read()
data = [s.replace(" ", "") for s in data.split("\n")]
ppp(data)
# a 71 b 51
result = 0
inner = re.compile(r"[(](?:\d+[+*])+\d+[)]")
plus = re.compile(r"\D*(\d+[+]\d+)\D*")
pork = inner.findall(data[0])
pork = plus.findall(data[0])
pp(pork, "pork")
part2 = True

def calc(equation, returnString):
    result = ""
    parentheses = 0
    plusses = []
    equation = equation.replace("(", "")
    equation = equation.replace(")", "")
    if part2:
        while "+" in equation:
            plus_match = plus.search(equation)
            pp(plus_match.group(1), "plusses")
            equation = (equation[:plus_match.start(1)] 
                            + str(eval(plus_match.group(1))) 
                            + equation[plus_match.end(1):])
            pp(equation, "equation after plusses fix")
            #for group in plusses:
                #pp(group, "grp")
                #re.search(r"\D*" + group + r"\D*")
                #equation = re.sub(plus, str(eval(group)), equation, 1)

                #equation = equation.replace(group, str(eval(group)), 1)

                #pp(equation, "repl plusses")
    for c in equation:
        if not c.isdigit(): 
            result += ")"
            parentheses += 1
        result += c
    openening_parentheses = "(" * parentheses
    result = openening_parentheses + result
    pp(result, "calc result")
    value = eval(result)
    pp(value, "value")
    if returnString:
        return str(value)
    else:
        return(value)

#calc(data[0], False)
results = []
for equation in data:
    pp(equation, "eq")
    e = equation
    while "(" in e:
        inners = inner.findall(e)
        pp(inners, "inn")
        for group in inners:
            #pp(group, "grp")
            e.index #re.sub
            e = e.replace(group, calc(group, True), 1)
        
            pp(e, "repl")
    results.append(calc(e, False))

    
pp(results, "Results")
pp(sum(results), "Solution", True)

#part 2

