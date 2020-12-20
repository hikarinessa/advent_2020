# https://adventofcode.com/2020/day/17
from utilities import *

INPUT = ['..##.#.#',
         '##....#.',
         '....####',
         '#..##...',
         '#..#.##.',
         '.#..#...',
         '##...##.',
         '.#...#..']
TEST_INPUT = ['.#.',
              '..#',
              '###']


def init_dict(my_input: list, is_part_two: bool):
    my_dict = {}
    for y, val in enumerate(my_input):
        for x in range(len(val)):
            if is_part_two:
                my_dict[x, y, 0, 0] = (val[x] == '#')
            else:
                my_dict[x, y, 0] = (val[x] == '#')
    # making an expanded space so that it can be iterated through
    expanded = my_dict.copy()
    for key, val in my_dict.items():
        expand, _adj = find_adjacency(my_dict, key, is_part_two)
        for key2, val2 in expand.items():
            expanded[key2] = val2
    return expanded


def find_adjacency(status: dict, coord: tuple, is_part_two: bool):
    active = 0
    new_status = {}
    for x in range(-1, 2):
        for y in range(-1, 2):
            for z in range(-1, 2):
                if is_part_two:
                    for w in range(-1, 2):
                        is_active = False
                        new_coord = (coord[0] + x, coord[1] + y, coord[2] + z, coord[3] + w)
                        if new_coord in status.keys():
                            is_active = status[new_coord]
                        else:
                            new_status[new_coord] = False  # adding to the dict new empty values
                        if is_active and new_coord != coord:
                            active += 1
                else:
                    is_active = False
                    new_coord = (coord[0] + x, coord[1] + y, coord[2] + z)
                    if new_coord in status.keys():
                        is_active = status[new_coord]
                    else:
                        new_status[new_coord] = False  # adding to the dict new empty values
                    if is_active and new_coord != coord:
                        active += 1
    return new_status, active


def print_status(status: dict, layer):
    """Prints like the input the current status of a layer. Only done with Part 1 in mind."""
    OFFSET = 7
    GRID = 23
    graphic = []
    for i in range(GRID):
        row = '.'*GRID
        graphic.append(row)
    for key, val in status.items():
        if val:
            if key[2] == layer:
                row = graphic[key[1]+OFFSET]
                _temp_status, adjacents = find_adjacency(status, key, False)
                if adjacents < 10: adj = str(adjacents)
                else: adj = '#'
                graphic[key[1]+OFFSET] = row[:key[0]+OFFSET] + adj + row[key[0]+OFFSET+1:]
    print("z =", layer)
    for i in graphic:
        print(i)


def main(my_input, is_part_two: bool):
    status = init_dict(my_input, is_part_two)
    if not is_part_two: print_status(status, 0)

    new_status = status.copy()
    for i in range(6):
        for key, val in status.items():
            temp_status, adjacents = find_adjacency(status, key, is_part_two)
            for key2, val2 in temp_status.items():
                new_status[key2] = val2
            if val and not 2 <= adjacents <= 3:
                new_status[key] = False
            if not val and adjacents == 3:
                new_status[key] = True
        status = new_status.copy()
        # if not is_part_two:  # debug prints
        #     print("*"*30)
        #     print_status(status, -1)
        #     print_status(status, 0)
        #     print_status(status, 1)

    counter = 0
    for val in status.values():
        if val:
            counter += 1

    return counter


if __name__ == "__main__":
    start_time = start_timer()
    print("First part:", main(INPUT, False))  # 202
    print_elapsed_time(start_time)
    print("*"*96)
    start_time = start_timer()
    print("Second part:", main(INPUT, True))  # 2028
    print_elapsed_time(start_time)
