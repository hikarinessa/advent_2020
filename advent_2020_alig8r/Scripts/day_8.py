import os
import sys
with open(os.path.join(sys.path[0], "../Inputs/input_day_8.txt"), "r") as my_input:
    _INPUT_1 = my_input.read().split("\n")
    #print(_INPUT_1)

_OUTPUT_2 = 0
we_good = False


def cycle_until_loop(program_list, swapped):
    """[Go through input until you come upon same input value INDEX, or exceed the index]

    Params:
        program_list ([list]): [a list of operations]
        swapped ([bool]): [is an element of the list swapped]

    """
    _ACCUMULATOR = 0
    list_of_processed_values = []
    index = 0
    while index not in list_of_processed_values:

        if index >= len(program_list) and swapped == True:
            print("boop")
            print(_ACCUMULATOR)
            list_of_processed_values.append(index)
            return _ACCUMULATOR, True

        list_of_processed_values.append(index)
        current_pos = _INPUT_1[index]
        operation, argument = current_pos.split(" ")

        if operation == "acc":
            _ACCUMULATOR += int(argument)
            index += 1
        elif operation == "jmp":
            index += int(argument)
        elif operation == "nop":
            index += 1

    return _ACCUMULATOR, False

def swap_operator(operator):
    if operation == "jmp": 
        return "nop"
    if operation == "nop":
        return "jmp"
    else:
        return operator


for index in range(0, len(_INPUT_1)):

    curr_index = index
    new_list = _INPUT_1
    operation, argument = _INPUT_1[index].split(" ")

    print("1: ", operation)
    operation = swap_operator(operation)
    new_list[index] = operation + " " + argument
    _OUTPUT_2, we_good = cycle_until_loop(new_list, True)
    
    if we_good:
        print("LALA")
        break
    

    print("2: ", operation)




print(cycle_until_loop(0, False))
print(_OUTPUT_2)


    





