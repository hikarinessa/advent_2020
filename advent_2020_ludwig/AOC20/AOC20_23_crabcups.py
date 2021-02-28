# https://adventofcode.com/2020/day/23

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

def update_cups():
    global _CUPS
    for i, cup in enumerate(_CIRCLE):
        _CUPS[cup] = i

update_cups()
pp(_CIRCLE)

def update_pickups(pu):
    global _CUPS
    for p in pu:
        _CUPS[p] = None

_CURRENT_CUP = _CIRCLE[0]
_DESTINATION_CUP = None
_TURNS_TODO = 10

_LENGTH = len(_CIRCLE)
_MAX = max(_CIRCLE)
turn_memory = {}

def wrap(index):  # ---- ensure circular lookup by wrapping the index around if it's too large
    if index >= _LENGTH:
        return (index - _LENGTH)
    else:
        return index

def dest(value): # ----- circular lookup for destination when it's <= 0
    if value <= 0:
        return (value + _MAX)
    else:
        return value

def rotate(n, direction):
    if direction == "left":
        return _CIRCLE[n:] + _CIRCLE[:n]
    else:
        return _CIRCLE[-n:] + _CIRCLE[:-n]

def leng():
    global _LENGTH
    _LENGTH = len(_CIRCLE)

turn = 0

while turn < _TURNS_TODO:
    turn += 1
    pp(turn, "Turn", True)
    pp(_CIRCLE)
    pp(_CURRENT_CUP, "current cup")
    
    current_cup_index = _CUPS[_CURRENT_CUP]

    pickup_indices = [wrap(current_cup_index+1), wrap(current_cup_index+2), wrap(current_cup_index+3)]
    pickup = [_CIRCLE[it] for it in pickup_indices]

    for pi in pickup:
        _CIRCLE.remove(pi) # --- way to slow for part 2
    pp(pickup, "picked up")
   
    pp(_CIRCLE, "circle after pickup")
    update_cups() # --- loops over the whole list to update indices :(
    update_pickups(pickup)

    leng() # --- updates global length variable for the circle

    destination_cup_found = False
    destination = dest(_CURRENT_CUP-1)

    while _CUPS[destination] is None:
        destination = dest(destination-1)

    _DESTINATION_CUP = destination
    
    pp(_DESTINATION_CUP, "destination cup")
    destination_index = _CUPS[_DESTINATION_CUP]

    for ip, p in enumerate(pickup):
        if destination_index == _LENGTH - 1:
            _CIRCLE.append(p)
        else:
            _CIRCLE.insert(destination_index+1+ip, p) # --- way to slow for part 2

    update_cups()
    leng()
    pp(_CIRCLE)

    _CURRENT_CUP = _CIRCLE[wrap(_CUPS[_CURRENT_CUP]+1)]
    pp("-")


result = "".join([str(c) for c in _CIRCLE[1:]])
pp(result, "result", True)

        
'''
##### GRAVEYARD ####

for i, cup in enumerate(_CIRCLE): # ---- first try dumb loops
        if cup == _CURRENT_CUP:
            pickup_indices = [wrap(i+1), wrap(i+2), wrap(i+3)]
            pickup = [_CIRCLE[it] for it in pickup_indices]
            for pi in pickup:
                _CIRCLE.remove(pi)
            pp(pickup, "picked up")
            pp(_CIRCLE, "circle after pickup")
            break

destination_index = None
while not destination_cup_found: 
        for dest_i, cup in enumerate(_CIRCLE):
            if cup == destination:
                _DESTINATION_CUP = cup
                destination_index = dest_i
                pp(cup, "destination cup")
                destination_cup_found = True
                
                for ip, p in enumerate(pickup):
                    if destination_index == _LENGTH - 1:
                        _CIRCLE.append(p)
                    else:
                        _CIRCLE.insert(destination_index+1+ip, p)
                break
        destination = dest(destination-1)

turn_mem = str(turn_mem)   # --- tried for a while to save content of turns to find patterns at huge loop numbers...
    if turn_mem in turn_memory:
        turn_memory[turn_mem] += 1
    else:
        turn_memory[turn_mem] = 1

for i, cup in enumerate(_CIRCLE):
        if cup == _CURRENT_CUP:
            _CURRENT_CUP = _CIRCLE[wrap(i+1)]
            break

'''
    


