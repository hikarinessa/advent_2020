# https://adventofcode.com/2020/day/21
from copy import deepcopy as deep

debug = True
printit = False
part2 = False

def p(text = "", override = False): #prints as string 
    if debug or printit or override:
        print(text, flush=True)
def pp(subject, name = "", override = False): #prints anything with a name as string 
    if debug or printit or override:
        #print("\n", name, ": ", subject)
        #   print()
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
def pppp(subject, name = "", override = False, isDictionary=False): #prints list's list entries
    if debug or printit or override:
        #print("\n", name, ": ", subject)
        print()
        print(name, ": ")
        for item in subject:
            if isDictionary:
                print(item, ":", end="")
                print(subject[item])
            else:
                for tile in item:
                    print()
                    for line in tile: 
                        print(line)

print("\n----------------------------------")   # reading file

data = """mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)"""


if not debug:
    file = "advent_2020_ludwig/AOC20/data_aoc20_21.txt"
    with open(file) as f:
        data = f.read()

data = [s[:-1].split(" (contains ") for s in data.split("\n")]
ppp(data)
FOOD = {}
for line in data:
    FOOD[line[0]] = [line[0].split(), line[1].split(", ")]
ppp(FOOD, "food dict", False, True)