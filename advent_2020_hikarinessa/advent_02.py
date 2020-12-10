# https://adventofcode.com/2020/day/2
import re
from advent_02_input import my_list


# The password policy indicates the lowest and highest number of times a given letter must appear for the password
# to be valid. For example, 1-3 a means that the password must contain a at least 1 time and at most 3 times.
# How many passwords are valid according to their policies?
def find_valid_pass(pass_list):

    valid_passwords = 0

    for entry in pass_list:
        parse = re.search(r"(\d+)-(\d+) (.): (.+)", entry)
        range_begin = int(parse.group(1))
        range_end = int(parse.group(2))
        key_letter = parse.group(3)
        password = parse.group(4)

        if range_begin <= password.count(key_letter) <= range_end:
            valid_passwords += 1

    print("First part: ", valid_passwords)


# Each policy actually describes two positions in the password, where 1 means the first character, 2 means the second
# character, and so on. (Be careful; TCP have no concept of "index zero"!) Exactly one of these positions must contain
# the given letter. Other occurrences of the letter are irrelevant for the purposes of policy enforcement.
# How many passwords are valid according to the new interpretation of the policies?
def find_correct_pass(pass_list):

    valid_passwords = 0

    for entry in pass_list:
        parse = re.search(r"(\d+)-(\d+) (.):(.+)", entry)
        first_index = int(parse.group(1)) - 1
        second_index = int(parse.group(2)) - 1
        key_letter = parse.group(3)
        password = parse.group(4)

        valid = False

        for num in [first_index, second_index]:
            if num < len(password):
                if password[num] == key_letter:
                    valid = not valid

        if valid:
            valid_passwords += 1

        # print(str(firstIndex) + ", " + str(secondIndex) + ", " + keyLetter + ", " + password)

    print("Second part: ", valid_passwords)


find_valid_pass(my_list)  # 467
find_correct_pass(my_list)  # 401
