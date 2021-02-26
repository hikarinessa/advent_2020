# https://adventofcode.com/2020/day/16

data = """class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12"""

debug = False
printit = False
part2 = True

if part2:
    data = """class: 0-1 or 4-19
row: 0-5 or 8-19
seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
3,9,18
15,1,5
5,14,9"""

import copy

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

file = "advent_2020_ludwig/AOC20/data_aoc20_16.txt"
if not debug:
    with open(file) as f:
        data = f.read()

data = [s for s in data.split("\n\n")]
rules = [s for s in data[0].split("\n")]
# ppp(rules, "rules")
myticket = [s.split(",") for s in data[1].split("\n")][1]
pp(myticket, "my ticket")
nearby_tickets = [[int(t) for t in s.split(",")] for s in data[2].split("\n")[1:]]
# ppp(nearby_tickets, "nearby tickets")

for index, line in enumerate(rules):
    split = [s for s in line.split(": ")]
    rules[index] = [split[0]]  
    for pair in [s.split("-") for s in split[1].split(" or ")]:
        pair = [int(x) for x in pair]
        rules[index].append(pair) 
ppp(rules, "rules", True)

# ----- Part 1 ------

invalids = []
valid_tickets = []
for ticket in nearby_tickets:
    #pp(ticket, "ticket")
    ticket_valid = True
    for index, entry in enumerate(ticket):
        strikes = 0
        for rule in rules:
            min1, max1, min2, max2 = rule[1][0], rule[1][1], rule[2][0], rule[2][1]
            if entry not in range(min1, max1+1):
                if entry not in range(min2, max2+1):
                    strikes += 1
        if strikes == len(rules):            
            pp(entry, "invalid entry")
            invalids.append(entry)
            ticket_valid = False
    if ticket_valid:
        valid_tickets.append(ticket) # -- list of valid tickets for part 2

error_rate = sum(invalids)
pp(error_rate, "error rate", True)

# ----- Part 2 -------

#ppp(valid_tickets, "valid tickets", True)
rule_positions = {}
possible_positions = len(rules)
number_of_tickets = len(valid_tickets)

for rule in rules:
    rule_positions[rule[0]] = []
    #pp(rule, "rule", True)
    min1, max1, min2, max2 = rule[1][0], rule[1][1], rule[2][0], rule[2][1]
    position = 0
    match_found = False
    for position in range(possible_positions):
        #pp(position, "--position to check", True)
        matches = 0
        
        for ticket in valid_tickets:
            entry = ticket[position]
            if entry in range(min1, max1+1) or entry in range(min2, max2+1):
                matches += 1

        if matches == number_of_tickets:
            rule_positions[rule[0]].append(position)
            #print("match found!!!")
            match_found = True


        
pp(possible_positions, "count of possible positions", True)            
pp(number_of_tickets, "number of tickets", True)
ppp(rule_positions, "rule positions", True, True)

rule_pos_temp = copy.deepcopy(rule_positions)
rule_positions_final = {}
solution_found = False
loop_count = 0
while loop_count < 20:
    rule_position = 0
    for rule in rule_positions:
        positions = rule_positions[rule]
        if rule not in rule_positions_final:
            if len(positions) == 1:
                rule_position = positions[0]
                rule_positions_final[rule] = positions[0]
    #rule_pos_temp = {}
    for rule in rule_positions:
        if rule not in rule_positions_final:
            positions_list = []
            for position in rule_positions[rule]:
                if position != rule_position:
                    positions_list.append(position)
            rule_positions[rule] = positions_list
    
    if len(rule_positions_final) == 19:
        solution_found = True
    
    loop_count += 1

ppp(rule_positions_final, "rule positions solved", True, True)
pp(myticket, "my ticket", True)
result = 1
departure_positions = []
for key in rule_positions_final:
    if key.startswith("departure"):
        departure_positions.append(rule_positions_final[key])
        result *= int(myticket[rule_positions_final[key]])
pp(departure_positions, "positions of values named departure", True)
pp(result, "result", True)
    
