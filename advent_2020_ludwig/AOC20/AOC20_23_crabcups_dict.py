# https://adventofcode.com/2020/day/23

debug = False
printit = False
# ----------- ONLY WORKS FOR PART 2 --------------------
# Rewritten based on a hint from the internet to use
# a "linked list". Here it's the dictionary _CUPS that contains
# for each cup the name of the next cup. This makes it possible
# to only track the tiny changes instead of manipulating the whole list
# every turn. 

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

_CIRCLE = [int(c) for c in DATA]
_CUPS = {}

for i in range(len(_CIRCLE)+1, 1000000+1):
    _CIRCLE.append(i)
        
_CURRENT_CUP = _CIRCLE[0]
_DESTINATION_CUP = None
_TURNS_TODO = 100
if not debug:
    _TURNS_TODO = 10000000
_LENGTH = len(_CIRCLE)
_MAX = max(_CIRCLE)


def wrap(index):
    if index >= _LENGTH:
        return (index - _LENGTH)
    else:
        return index

def update_cups(item):  # --- only used once to write the inital dictionary
    global _CUPS
    if item == "all":
        for i, cup in enumerate(_CIRCLE):
            _CUPS[cup] = _CIRCLE[wrap(i+1)]
    else:
        _CUPS[item] = _CIRCLE[wrap(i+1)]

def dest(value):
    if value <= 0:
        return (value + _MAX)
    else:
        return value


update_cups("all")

turn = 0
turn_big = 0

while turn < _TURNS_TODO: 
    turn += 1
    
    #if turn_big + 1000 == turn:
    #    turn_big = turn
    #    pp(turn_big, "Turn", True)

    pp(_CURRENT_CUP, "current cup")
    
    pickup = [_CUPS[_CURRENT_CUP]] # picking up the cup after the current cup
    pickup.append(_CUPS[pickup[0]]) # picking up the cup after that one
    pickup.append(_CUPS[pickup[1]]) # picking up the cup after that one
    
    pp(pickup, "picked up")
    pp(_CUPS, "current cups dict")
   
    destination = dest(_CURRENT_CUP-1)
    while destination in pickup:
        destination = dest(destination-1) # calculating destination from pickup if necessary

    next_cup = _CUPS[pickup[2]]             # the cup to the right of the pickup is the current cup of next turn
    _CUPS[pickup[2]] = _CUPS[destination]   # the cup next to the last one picked up is the one next to the destination cup
    _CUPS[destination] = pickup[0]          # the cup next to the destination cup is the first one picked up
    _CUPS[_CURRENT_CUP] = next_cup          # the cup to the right of the pickup is now next to the current cup
    _CURRENT_CUP = next_cup                 # and thus becomes the next current cup
    pp(_CUPS, "current cups dict")
    pp("-")

stars = None

stars = _CUPS[1] * _CUPS[_CUPS[1]]

pp(stars, "the factor of the labels on the cups next to 1", True)
    

        


    
    


