import os
import sys
import math
with open(os.path.join(sys.path[0], "../Inputs/input_day_5.txt"), "r") as my_input:
    _INPUT_1 = my_input.read()
    _INPUT_1 = _INPUT_1.strip().split("\n")
    #print(_INPUT_1)

_FB_RANGE = [0, 127]
_LR_RANGE = [0, 7]

def get_new_range(letter, range):
    middle = math.floor(range[1] / 2)
    if letter == "F":
        range = [range[0], middle]
    elif letter == "B":
        range = [middle + 1, range[1]]
    else:
        print("Invalid Letter")
    return range

#for entry in _INPUT_1:
entry = "FBBBBFBRLL"

new_range = _FB_RANGE

for letter in entry:
    new_range = get_new_range(letter, new_range)
    #print(new_range)



#print(get_new_range("F", [0, 63]))