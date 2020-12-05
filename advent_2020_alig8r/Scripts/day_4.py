import re
import os
import sys 
with open(os.path.join(sys.path[0], "../Inputs/input_day_4.txt"), "r") as my_input:
    _INPUT_1 = my_input.read().replace(" ", "\n")
    _PASSPORT_List = _INPUT_1.split("\n\n")

validated_passports_count_1 = 0
validated_passports_count_2 = 0

class Passport:
    _VALID_EYE_COLORS = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

    def __init__(self):
        self.passes = 0
        self.status = False
        self.passport_dict = {
            "byr": None,
            "iyr": None,
            "eyr": None,
            "hgt": None,
            "hcl": None,
            "ecl": None,
            "pid": None, 
            "cid": None}


    def validate_passport(self, data):
        if len(data) >= 7:
            for entry in data:
                entry = entry.split(":")
                if entry[0] == "cid" and len(data) == 7:
                    self.status = False
                    break
                self.status = True
                         
                self.passport_dict[entry[0]] = entry[1]
            print(data)    





            self.__validate_passport__()
           
        
    def __validate_birth_year__(self):
        if self.passport_dict.get("byr") != None:
            self.birth_Year = int(self.passport_dict.get("byr"))
            if len(str(self.birth_Year)) == 4 and self.birth_Year > 1920 and self.birth_Year < 2002:
                self.passes += 1
                print("birth_Year", self.birth_Year) 
    

    def __validate_issue_year__(self):
        if self.passport_dict.get("iyr") != None:
            self.issue_year = int(self.passport_dict.get("iyr"))
            if len(str(self.issue_year)) == 4 and self.issue_year > 2010 and self.issue_year < 2020:
                self.passes += 1
                print("issue_year", self.issue_year) 
    

    def __validate_expiration_year__(self):
        if self.passport_dict.get("eyr") != None:
            self.expiration_year = int(self.passport_dict.get("eyr"))
            if len(str(self.expiration_year)) == 4 and self.expiration_year > 2020 and self.expiration_year < 2030:
                self.passes += 1
                print("expiration_year", self.expiration_year) 


    def __validate_height__(self):
        if self.passport_dict.get("hgt") != None:
            self.height = self.passport_dict.get("hgt")
            self.height = re.search(r"(\d+)(.+)", self.height)
            self.unit = self.height.group(2)
            self.measure = int(self.height.group(1))

            if self.unit == "cm" and self.measure > 150 and self.measure < 193:
                self.passes += 1
                print("height", self.unit, self.measure) 
            elif self.unit == "in" and self.measure > 59 and self.measure < 76:
                self.passes += 1
            
                print("height", self.unit, self.measure) 


    def __validate_hair_color__(self):
        if self.passport_dict.get("hcl") != None:
            self.hex_chars = "0123456789abcdef"
            self.hair_color = self.passport_dict.get("hcl")
            if self.hair_color[0] == "#" and len(self.hair_color[1:]) == 6:
                for self.char in self.hair_color[1:]:
                    if self.char not in self.hex_chars:
                        break
                print("hair_color", self.hair_color) 
                self.passes += 1             


    def __validate_eye_color__(self):
        if self.passport_dict.get("ecl") != None:
            self.eye_color = self.passport_dict.get("ecl")
            if any(self.eye_color in col for col in self._VALID_EYE_COLORS):
                print("eye_color", self.eye_color)
                self.passes += 1


    def __validate_passport_id__(self):
        if self.passport_dict.get("pid") != None:
            self.passport_id = self.passport_dict.get("pid")
            if len(self.passport_id) == 9:
                print("passport_id", self.passport_id) 
                self.passes += 1


    def __validate_passport__(self):
        self.__validate_birth_year__()
        self.__validate_issue_year__()
        self.__validate_expiration_year__()
        self.__validate_height__()
        self.__validate_hair_color__()
        self.__validate_eye_color__()
        self.__validate_passport_id__()


        print("Passes:", self.passes)
        print("#---------------------------#")
            

for passport_data in _PASSPORT_List:
    passport_data = passport_data.split("\n")
    _PASSPORT = Passport()
    _PASSPORT.validate_passport(passport_data)
    if _PASSPORT.status:
        validated_passports_count_1 += 1
    if _PASSPORT.passes == 7:
        validated_passports_count_2 += 1

print("Validated Part 1:", validated_passports_count_1)
print("Validated Part 2:", validated_passports_count_2)
