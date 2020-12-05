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

id_list = [k.seat_id for k in bp_list]
id_list.sort()

print("First part: ", id_list[-1])  # 850

for index in range(len(id_list)-1):
    if id_list[index] + 1 != id_list[index+1]:
        print("Second part: ", id_list[index] + 1)

