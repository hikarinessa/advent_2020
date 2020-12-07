# https://adventofcode.com/2020/day/5
from advent_05_input import boarding_pass_list
from advent_05_input import bp_list_test
MAX_ROW = 127  # 0 to 127
MAX_COL = 7  # 0 to 7


def split (lo, hi):
    half = (hi - lo)/2
    return int(lo), int((lo + half)), int((lo + half + 0.5)), int(hi)

def recursive_partition(string, slo, shi, mx:int):
    x = 0
    y = mx
    result = 0
    for i in string:
        a, b, c, d = split(x, y)
        if i == slo:
            x = a
            y = b
            result = a
        if i == shi:
            x = c
            y = d
            result = d
    return result


class BoardingPass:
    def __init__(self, code):
        self.code = code  # Format: BFBFFFFRLR
        self.row = self.decode_row()
        self.col = self.decode_col()
        self.seat_id = self.get_seat_id()


    def decode_row(self):
        row_code = self.code[:7]  # BFBFFFF where F lo and B hi
        return recursive_partition(row_code, "F", "B", MAX_ROW)


    def decode_col(self):
        col_code = self.code[-3:]  # RLR where L lo and R hi
        return recursive_partition(col_code, "L", "R", MAX_COL)


    def get_seat_id(self):
        return self.row * 8 + self.col


def list_to_objects(my_list):
    boarding_objects = []
    split_lines = my_list[0].splitlines()
    for i in split_lines:
        bp = BoardingPass(i)
        boarding_objects.append(bp)
    return boarding_objects


bp_list = list_to_objects(boarding_pass_list)
# for j in bp_list:
#     print(j.code, j.row, j.col, j.seat_id)


# optional stuff
def find_my_boarding_pass(boarding_list):
    my_row_dict = {}
    my_row : int
    my_col : int
    my_boarding_pass  = ""

    for entry in boarding_list:
        my_row = entry.row
        if my_row in my_row_dict:
            my_row_dict[my_row].append(entry.col)
        else:
            my_row_dict[my_row] = [entry.col]
    for key in my_row_dict:
        if len(my_row_dict[key]) != 8:
            for i in range(0, 8):
                if i not in my_row_dict[key]:
                    if key * 8 + i == 599:  # using the solution for the second star
                        my_row = key
                        my_col = i
                        print(my_row, my_col)
    current_max_row = MAX_ROW
    current_max_col = MAX_COL
    while len(my_boarding_pass) < 8:
        if my_row > current_max_row/2:
            my_boarding_pass += "B"
            current_max_row = current_max_row + current_max_row/2
        else:
            my_boarding_pass += "F"
            current_max_row /= 2
    while len(my_boarding_pass) < 11:
        if my_col > current_max_col/2:
            my_boarding_pass += "R"
            current_max_col = current_max_col + current_max_col/2
        else:
            my_boarding_pass += "L"
            current_max_col /= 2
    print(my_boarding_pass)



id_list = [k.seat_id for k in bp_list]
id_list.sort()

print("First part: ", id_list[-1])  # 850

for index in range(len(id_list)-1):
    if id_list[index] + 1 != id_list[index+1]:
        print("Second part: ", id_list[index] + 1)  # 599

find_my_boarding_pass(bp_list)

test = BoardingPass("BFBBFBFBRRL")
print(test.row, test.col, test.seat_id)