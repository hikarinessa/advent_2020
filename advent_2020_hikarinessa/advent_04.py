# https://adventofcode.com/2020/day/4
import advent_04_input  # contains: my_input , test_valid, test_invalid
import re


class Passport:
    def __init__(self, number):
        self.number = number
        self.byr = ""  # (Birth Year)
        self.iyr = ""  # (Issue Year)
        self.eyr = ""  # (Expiration Year)
        self.hgt = ""  # (Height)
        self.hcl = ""  # (Hair Color)
        self.ecl = ""  # (Eye Color)
        self.pid = ""  # (Passport ID)
        self.cid = ""  # (Country ID)

    def valid_fields(self, debug):
        """Returns True if all fields follow the guidelines. Ignores CID."""
        valid = True
        if debug: print(self.number)

        # validate years if not empty and no different than 4 chars and in between ranges
        if self.byr is "" or len(self.byr) != 4 or not 1920 <= int(self.byr) <= 2002:
            valid = False
            if debug: print(self.byr, "is an invalid birth year")
        if self.iyr is "" or len(self.iyr) != 4 or not 2010 <= int(self.iyr) <= 2020:
            valid = False
            if debug: print(self.iyr, "is an invalid issue year")
        if self.eyr is "" or len(self.eyr) != 4 or not 2020 <= int(self.eyr) <= 2030:
            valid = False
            if debug: print(self.eyr, "is an invalid expiration year")

        # validate height with the correct metric for each
        if self.hgt[-2:] == "cm":
            height_cm = re.sub("cm", "", self.hgt)
            if height_cm is "" or not 150 <= int(height_cm) <= 193:
                valid = False
                if debug: print(self.hgt, "is an invalid height in cm")
        elif self.hgt[-2:] == "in":
            height_in = re.sub("in", "", self.hgt)
            if height_in is "" or not 59 <= int(height_in) <= 76:
                valid = False
                if debug: print(self.hgt, "is an invalid height in in")
        else:
            valid = False
            if debug: print(self.hgt, "is an invalid height")

        # hair colour has to have a hash in the beginning
        if self.hcl is "" or self.hcl[0] is not "#":
            valid = False
            if debug: print(self.hcl, "is an invalid hair color, missing the hash")
        # regex checks for exactly {6} chars within: abcdef ABCDEF 0123456789
        elif re.match("^[a-fA-F0-9]{6}$", self.hcl[1:]) is None:
            valid = False
            if debug: print(self.hcl, "is an invalid hair color")

        # eye colour check if not empty and if the string is within the valid strings
        valid_eye_col = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
        if self.ecl is "" or self.ecl not in valid_eye_col:
            valid = False
            if debug: print(self.ecl, "is an invalid eye color")

        # validates passport id
        # if not (self.pid.isnumeric() and len(self.pid) == 9):
        # alternative: Regex checks for exactly {9} numbers \d
        # ^ and $ delimit the string, without them this would match >9 numbers
        if re.match("^\d{9}$", self.pid) is None:
            valid = False
            if debug: print(self.pid, "is an invalid passport ID")

        return valid


def data_to_passports(raw_data):
    """Converts raw input into a list of Passport objects."""
    passports = []

    # remove unnecessary returns
    one_string_per_pass = raw_data.replace("\n", " ")
    # split items on double spaces (previously double returns)
    one_string_per_pass = one_string_per_pass.split("  ")

    for i in range(len(one_string_per_pass)):
        parsed_entry = re.split("[: ]", one_string_per_pass[i])
        new_pass = Passport(i)
        for j in range(0, len(parsed_entry), 2):
            setattr(new_pass, parsed_entry[j], parsed_entry[j+1])
        passports.append(new_pass)

    return passports


# part 1
def check_passports(passports):
    valid_pass = 0

    for passport in passports:
        is_valid = True
        for var in vars(passport):
            if getattr(passport, var) == "":
                if var != "cid":
                    is_valid = False
        if is_valid:
            valid_pass += 1

    return valid_pass


# part 2
def check_valid_passports(passports):
    valid_pass = 0

    for passport in passports:
        if passport.valid_fields(debug=False):
            valid_pass += 1

    return valid_pass


my_passports = data_to_passports(advent_04_input.my_input)
my_passports_test = data_to_passports(advent_04_input.test_invalid)

print("First part: ", check_passports(my_passports))  # answer is 226
print("Second part: ", check_valid_passports(my_passports))  # answer is 160
