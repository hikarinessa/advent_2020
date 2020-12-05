import os
import sys

_INPUT =  open(os.path.join(sys.path[0], "input_day1_1.txt"), "r")
_NUMBERS = []
_OUTPUT = 0

for line in _INPUT:
    number = int(line)
    _NUMBERS.append(number)

for num in range(0, len(_NUMBERS)):
    remaining_numbers = _NUMBERS[num:]

    for comparer in range(0, len(remaining_numbers)):
        remaining_numbers_2 = remaining_numbers[comparer:]

        for comparer_2 in remaining_numbers_2:

            if int(_NUMBERS[num]) + int(remaining_numbers[comparer]) + int(comparer_2)== 2020: 
                print(_NUMBERS[num], remaining_numbers[comparer], comparer_2, "woop")
                _OUTPUT = _NUMBERS[num] * remaining_numbers[comparer] * comparer_2

print(_OUTPUT)
    