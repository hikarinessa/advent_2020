# https://adventofcode.com/2020/day/18

data = """1 + 2 * 3 + 4 * 5 + 6
1 + (2 * 3) + (4 * (5 + 6))
2 * 3 + (4 * 5)
5 + (8 * 3 + 9 + 3 * 4 * 3)
5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))
((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"""

data = "4 + (5 + (5 * 5 + 3 + 2) + (6 + 4 * 9 * 2 * 8) * 6 + (7 * 5 * 2) * (2 * 8 * 2)) + (8 * 7 + 7) * 6 * 9 * (5 + 9)"

import re
debug = True
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

file = "advent_2020_ludwig/AOC20/data_aoc20_18.txt"
if not debug:
    with open(file) as f:
        data = f.read()
data = [s.replace(" ", "") for s in data.split("\n")]
ppp(data)
# a 71 b 51
result = 0
inner = re.compile(r"[(](?:\d+[+*])+\d+[)]") # pattern to find the innermost parentheses
plus = re.compile(r"\D*(\d+[+]\d+)\D*") # pattern to find groups of additions to solve first for part 2
pork = inner.findall(data[0])
if part2:
    pork = plus.findall(data[0])
pp(pork, "test of elements matching the regex", True)


def calc(equation, returnString):
    result = ""
    parentheses = 0
    equation = equation.replace("(", "")
    equation = equation.replace(")", "") # delete original parentheses

    if part2:
        while "+" in equation:
            plus_match = plus.search(equation) # search the inner group for additions
            pp(plus_match.group(1), "plusses")
            equation = (equation[:plus_match.start(1)] 
                            + str(eval(plus_match.group(1)))    # insert the result of the addition back in
                            + equation[plus_match.end(1):])     # this over time eliminates all plusses from the equation
            pp(equation, "equation after plusses fix") 
            
    for c in equation:
        if not c.isdigit(): # add closing parenthesis before every operator
            result += ")" 
            parentheses += 1
        result += c

    openening_parentheses = "(" * parentheses # add matching number of opening parentheses
    result = openening_parentheses + result
    pp(result, "calc result")

    value = eval(result)
    pp(value, "value")

    if returnString:
        return str(value)
    else:
        return(value)

results = []
for equation in data:
    pp(equation, "eq")
    e = equation

    while "(" in e:
        inners = inner.findall(e)
        pp(inners, "inn")

        for group in inners:
            e = e.replace(group, calc(group, True), 1)  #insert solved inner group into original equation as long as
                                                        # there are parentheses present
            pp(e, "repl")

    results.append(calc(e, False))

pp(results, "Results")
pp(sum(results), "Solution", True)

#part 2

