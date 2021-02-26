# https://adventofcode.com/2020/day/7

data = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags."""

debug = False
part2 = True 
printit = True

if debug and part2:
    data = """shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags."""

def pp(subject, name = ""): #prints anything with a name as string 
    if debug or printit:
        #print("\n", name, ": ", subject)
        print(name, ": ", subject)

print("\n----------------------------------")   # reading file

file = "advent_2020_ludwig/AOC20/data_aoc20_7.txt"
if not debug:
    with open(file) as f:
        data = f.read()
data = [[i.rstrip(".,") for i in s.split() if "no" not in s] for s in data.split("\n")]

pp(len(data), "number of data lines excluding no lines")

datajoined = []

for index, s in enumerate(data):
    toremove = ["bag", "bags", "contain"]
    for x in toremove:
        while x in s:
            s.remove(x)
    if len(s) > 0:
        datajoined.append([(" ").join(s[:2])])
    else:
        datajoined.append([])
    k = 2
    while k < len(s):   
        datajoined[index].append(int(s[k]))
        k += 3
        datajoined[index].append((" ").join(s[k-2:k]))

# pp(datajoined)    

def checkcolor(colors, debugprint = False):
    holdingcolors = []
    for color in colors:
        for rule in datajoined:
            if len(rule) > 0 and color != rule[0]:
                if color in rule:
                    holdingcolors.append(rule[0])
    return list(dict.fromkeys(holdingcolors))

def checkcolorpart2(colors, debugprint = False):
    global bags_within_shiny_gold
    heldcolors = []
    for color in colors:
        for rule in datajoined:
            if len(rule) > 0 and color[0] == rule[0]:
                i = 2
                while i <= len(rule):
                    heldcolors.append([rule[i],rule[i-1]*color[1]])
                    i += 2
    return heldcolors

colors_shiny_gold_holds = []
colors_holding_shiny_gold = []
bags_within_shiny_gold = 0
allcolors = []

for rule in datajoined:
    if len(rule) > 0:
        allcolors.append(rule[0])
        if not part2:
            if rule[0] != "shiny gold":
                if "shiny gold" in rule:
                    colors_holding_shiny_gold.append(rule[0])
        else:
            if rule[0] == "shiny gold":
                i = 2
                while i <= len(rule):
                    colors_shiny_gold_holds.append([rule[i], rule[i-1]])
                    i += 2

if not part2:
    pp(colors_holding_shiny_gold, "colors holding shiny gold directly")
pp(colors_shiny_gold_holds, "colors shiny gold contains")
allcolors = list(dict.fromkeys(allcolors))
pp(len(allcolors), "total number of colors")

if not part2:
    numberoffoundcolors = len(colors_holding_shiny_gold)
    othercolors = colors_holding_shiny_gold
else:
    numberoffoundcolors = len(colors_shiny_gold_holds)
    othercolors = colors_shiny_gold_holds

while numberoffoundcolors > 0:
    pp(othercolors, "before checking")
    numberoffoundcolors = len(othercolors)
    pp(numberoffoundcolors, "number of colors to check")
    if not part2:
        othercolors = checkcolor(othercolors, True)
    else:
        othercolors = checkcolorpart2(othercolors, True)
        #bags_within_shiny_gold += len(othercolors)
    pp(othercolors, "after checking")
    for color in othercolors:
        if not part2:
            colors_holding_shiny_gold.append(color)
        else:
            colors_shiny_gold_holds.append(color)

colors_holding_shiny_gold = list(dict.fromkeys(colors_holding_shiny_gold))
pp(colors_holding_shiny_gold, "all colors holding shiny gold")

for color in colors_shiny_gold_holds:
    bags_within_shiny_gold += color[1]

pp(colors_shiny_gold_holds, "all colors shiny gold holds")

if not part2:
    pp(len(colors_holding_shiny_gold), "number of colors holding shiny gold directly or indirectly")
pp(len(colors_shiny_gold_holds), "number of colors contained in shiny gold bag directly or indirectly")
pp(bags_within_shiny_gold, "Total number of individual bags in the shiny gold bag")

