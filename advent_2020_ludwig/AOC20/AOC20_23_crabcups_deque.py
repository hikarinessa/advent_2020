# https://adventofcode.com/2020/day/23

from copy import deepcopy as deep
from collections import deque
from time import perf_counter

debug = False
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
                #print(item, ":", end="")
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

DATA = "389125467"

if not debug:
    DATA = "942387615"

DATA = "389125467"

_CIRCLE = [int(c) for c in DATA]
_CUPS = {}

if part2:
    for i in range(len(_CIRCLE)+1, 1000000+1):
        _CIRCLE.append(i)

_CURRENT_CUP = _CIRCLE[0]
_DESTINATION_CUP = None
_TURNS_TODO = 10

if part2:
    _TURNS_TODO = 10000000

_LENGTH = len(_CIRCLE)
_MAX = max(_CIRCLE)

def dest(value):
    if value <= 0:
        return (value + _MAX)
    else:
        return value

turn = 0
_CIRCLE = deque(_CIRCLE)  # converting input list to a deque
turn_big = 0

while turn < _TURNS_TODO: 
    # deque approach is faster and feels less clunky than using list 
    # but part 2 would still take ~1 day to finish...

    turn += 1
    if turn_big + 1000 == turn:  # ---- print only every 1000 turns..
        turn_big = turn
        pp(turn_big, "Turn", True)

    next_current = _CIRCLE[4]
    _CIRCLE.rotate(-4)
    
    pickup = [_CIRCLE.pop() for i in range(3)]
    pickup.reverse()
    
    destination = dest(_CURRENT_CUP-1)
    while destination in pickup:   # --- faster calculating the destination from pickup (obvs..)
        destination = dest(destination-1)

    destination_index = _CIRCLE.index(destination) # -- bad slow for part 2 as it could not be near the start/end
    
    # trying to reduce the amount of rotation needed to get the destination
    # to the end for appending the pickup, still end up huge :(, especially for
    # the first million turns
    interval = _LENGTH-4-destination_index
    if interval > _LENGTH // 2:  
        interval = _LENGTH-interval  
                                     
    _CIRCLE.rotate(interval)

    for x in pickup:
        _CIRCLE.append(x)
    
    _CIRCLE.rotate(-interval)
    _CURRENT_CUP = next_current
  
    pp("-")

stars = None

while _CIRCLE[0] != 1:
    _CIRCLE.rotate(-1)

stars = _CIRCLE[1] * _CIRCLE[2]
        

if not part2:
    result = "".join([str(c) for c in list(_CIRCLE)[1:]])
    pp(result, "result", True)
else:
    pp(stars, "the factor of the labels on the cups next to 1", True)
    

        


    
    


