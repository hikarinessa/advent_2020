# https://adventofcode.com/2020/day/15
from utilities import *
import pprint
import re
from Inputs.advent_16_input import ticket_fields, your_ticket, nearby_tickets
ticket_fields = ticket_fields.splitlines()

# region ---------------- test inputs ----------------
# Test fields part 1
# test_ticket_fields = """class: 1-3 or 5-7
# row: 6-11 or 33-44
# seat: 13-40 or 45-50"""
# ticket_fields = test_ticket_fields.splitlines()
# your_ticket = [7, 1, 14]
# nearby_tickets = [[7, 3, 47], [40, 4, 50], [55, 2, 20], [38, 6, 12]]

# Test fields part 2
# test_ticket_fields = """class: 0-1 or 4-19
# row: 0-5 or 8-19
# seat: 0-13 or 16-19"""
# ticket_fields = test_ticket_fields.splitlines()
# your_ticket = [11, 12, 13]
# nearby_tickets = [[3, 9, 18],
#                   [15, 1, 5],
#                   [5, 14, 9],
#                   [11, 12, 13]]
# endregion ------------------------------------------


def build_valid_values():
    valid_dict = {}
    for i in range(1000):
        valid_dict[i] = False

    for field in ticket_fields:
        parse = re.search(r"(.+): (\d+)-(\d+) or (\d+)-(\d+)", field)
        min1 = int(parse.group(2))
        max1 = int(parse.group(3))
        min2 = int(parse.group(4))
        max2 = int(parse.group(5))
        for i in range(min1, max1+1):
            valid_dict[i] = True
        for i in range(min2, max2+1):
            valid_dict[i] = True

    return valid_dict


def first_part():
    valid_dict = build_valid_values()
    counter = 0

    for ticket in nearby_tickets:
        for i in ticket:
            if not valid_dict[i]:
                counter += i

    return counter


def build_dicts(valid_tickets):
    my_dict = {}
    for field in ticket_fields:
        parse = re.search(r"(.+): (\d+)-(\d+) or (\d+)-(\d+)", field)
        field_name = parse.group(1)
        min1 = int(parse.group(2))
        max1 = int(parse.group(3))
        min2 = int(parse.group(4))
        max2 = int(parse.group(5))

        possible_columns = []
        for col in range(len(valid_tickets[0])):
            possible_column = 0
            for row in range(len(valid_tickets)):
                if min1 <= valid_tickets[row][col] <= max1 or min2 <= valid_tickets[row][col] <= max2:
                    # print(field_name, "/ row:", row, "col:", col, valid_tickets[row][col])
                    possible_column += 1
            if len(valid_tickets) == possible_column:
                possible_columns.append(col)
        my_dict[field_name] = possible_columns

    bob = 1
    checked_values = []
    while bob <= len(my_dict.keys()):
        for key, val in my_dict.items():
            if len(val) == bob:
                if bob == 1:
                    checked_values.append(val[0])
                else:
                    for i in checked_values:
                        if i in val:
                            val.remove(i)
                    checked_values.append(val[0])
                bob += 1

    for key, val in my_dict.items():
        my_dict[key] = int(val[0])

    return my_dict


def second_part():
    valid_dict = build_valid_values()
    nearby_valid_tickets = nearby_tickets.copy()

    for i, ticket in enumerate(nearby_tickets):
        for num in ticket:
            if not valid_dict[num]:
                nearby_valid_tickets[i] = None
    nearby_valid_tickets = [i for i in nearby_valid_tickets if i]
    field_coluns = build_dicts(nearby_valid_tickets)

    counter = 1
    for key, val in field_coluns.items():
        if "departure" in key:
            counter *= your_ticket[val]

    return counter


if __name__ == "__main__":
    print("First part:", first_part())  # 21956
    print("Second part:", second_part())  # 3709435214239

