# https://adventofcode.com/2020/day/15

import time

data = 0,3,6

debug = False
printit = False

tic = time.perf_counter()

def pp(subject, name = "", override = False): #prints anything with a name as string
    if debug or printit or override:
        #print("\n", name, ": ", subject)
        print(name, ": ", subject)


def ppp(subject, name = "", override = False): #prints list entries
    if debug or printit or override:
        #print("\n", name, ": ", subject)
        print(name, ": ")
        for item in subject:
            print(item, end="")
            print(subject[item])


print("\n----------------------------------")  

if not debug:
    data = 2,0,1,9,5,19
pp(data)

turn_count = 0
turns = []
numbers = {} # dict of numbers and the turn they were last spoken (dynamic)
# number : [0 times spoken, 1 turn last spoken, 2 turn spoken before, 3 age(diff between)]
for turn_spoken, starting_number in enumerate(data):
    turn_count += 1
    turns.append(starting_number)
    numbers[starting_number] = [1, turn_spoken+1, turn_spoken+1, 0] # len(data)-turn_spoken]
    
# while turn_count <= 2022:
while turn_count <= 30000000:  # part 2
    number_spoken_before = turns[turn_count-1]
    turn_count += 1
    #pp(number_spoken_before, "number spoken before")
    if numbers[number_spoken_before][0] == 1: # times spoken
        this_turn_number = 0
    else: 
        this_turn_number = numbers[number_spoken_before][3]  # age
    if this_turn_number in numbers:
        numbers[this_turn_number][0] += 1
        numbers[this_turn_number][2] = numbers[this_turn_number][1]
        numbers[this_turn_number][1] = turn_count
        numbers[this_turn_number][3] = numbers[this_turn_number][1] - numbers[this_turn_number][2]
    else:
        numbers[this_turn_number] = [1, turn_count, turn_count, 0]
    turns.append(this_turn_number)


#pp(turns, "turns", True)
#ppp(numbers, "numbers register", True)
print(f"Part 1: The number spoken on turn 2020 is {turns[2019]}")
print(f"Part 1: The number spoken on turn 30000000 is {turns[30000000-1]}")

toc = time.perf_counter()
print(f"This took {toc-tic} seconds")  # ooof
