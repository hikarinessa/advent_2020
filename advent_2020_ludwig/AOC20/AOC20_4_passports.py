# https://adventofcode.com/2020/day/4
# https://www.reddit.com/r/adventofcode/comments/k52psu/2020_day_04_solutions/
# The automatic passport scanners are slow because they're having trouble detecting which 
# passports have all required fields. The expected fields are as follows:

# byr (Birth Year)
# iyr (Issue Year)
# eyr (Expiration Year)
# hgt (Height)
# hcl (Hair Color)
# ecl (Eye Color)
# pid (Passport ID)
# cid (Country ID)
# Passport data is validated in batch files (your puzzle input). Each passport is 
# represented as a sequence of key:value pairs separated by spaces or newlines. Passports are separated by blank lines.

# Here is an example batch file containing four passports:

data = """ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in"""

# The first passport is valid - all eight fields are present. The second passport is invalid - 
# it is missing hgt (the Height field).

# The third passport is interesting; the only missing field is cid, so it looks like data 
# from North Pole Credentials, not a passport at all! Surely, nobody would mind if you made 
# he system temporarily ignore missing cid fields. Treat this "passport" as valid.

# The fourth passport is missing two fields, cid and byr. Missing cid is fine, but 
# missing any other field is not, so this passport is invalid.

# According to the above rules, your improved system would report 2 valid passports.

# Count the number of valid passports - those that have all required fields. 
# Treat cid as optional. In your batch file, how many passports are valid?

# Part 2:
# You can continue to ignore the cid field, but each other field has strict rules about what values are valid for automatic validation:

# byr (Birth Year) - four digits; at least 1920 and at most 2002.
# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
# hgt (Height) - a number followed by either cm or in:
# If cm, the number must be at least 150 and at most 193.
# If in, the number must be at least 59 and at most 76.
# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
# pid (Passport ID) - a nine-digit number, including leading zeroes.
# cid (Country ID) - ignored, missing or not.
import re
debug = False 
printit = True
def pp(subject, name): #prints anything with a name as string 
    if debug or printit:
        #print()
        print(name, ": ", subject)

print("\n----------------------------------")   # reading file

file = "advent_2020_ludwig/AOC20/data_aoc20_4.txt"
if not debug:
    with open(file) as f:
        data = f.read()
# for regex
datareg = [s.replace("\n", " ") for s in data.split("\n\n")]
# for dumb
data = [sorted(s.replace("\n", " ").split()) for s in data.split("\n\n")]


def checkpassport(i):
    valid = False
    if re.search(r"byr:19[2-9]\d|byr:200[0-2]", i) and \
    re.search(r"iyr:201\d|iyr:2020", i) and \
    re.search(r"eyr:202\d|eyr:2030", i) and \
    re.search(r"hgt:1[5-8]\dcm|hgt:19[0-3]cm|hgt:59in|hgt:6\din|hgt:7[0-6]in", i) and \
    re.search(r"hcl:#[0-9a-f]{6}", i) and \
    re.search(r"ecl:(amb|blu|brn|gry|grn|hzl|oth)", i) and \
    re.search(r"pid:[0-9]{9}\b", i):
        valid = True
        # pp(i, "valid passport according to regex")
    return valid

regvalids = 0
for p in datareg:
    #print(p)
    if checkpassport(p):
        regvalids += 1

pp(regvalids, "part 2 valids with regex method")


passports = []
#data = [[k.split(":") for k in j] for j in data ]
data = [j for j in data]
# data - list of passports, data[x] - passport fields, data[x][y] - pair of field and value


for line in data:
    passport = {}
    for field in line:
        x, y = field.split(":")
        passport[x] = y
    passports.append(passport)

# print(passports)
def checkfields(i, debugprint = False):
    if debugprint:
        print(i)
    valid = False
    points = 0

    if 1920 <= int(i["byr"]) <= 2002:
            points += 1
            if debugprint:    
                print("birthyear correct", end=" ")

    x = i["ecl"]
    for color in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
        if x == color:
            points += 1
            if debugprint:
                print("eye color correct", end=" ")

    if 2020 <= int(i["eyr"]) <= 2030:
            points += 1
            if debugprint:
                print("expiration year correct", end=" ")

    x = i["hcl"]
    if x[0] == "#":
        if len(x) == 7:
            counter = 0
            for c in x[1:]:
                if c in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]:
                    counter += 1
            if counter == 6:
                points += 1
                if debugprint:
                    print("hair color correct", end=" ")

    x = i["hgt"]
    if x[0].isdigit():
        if debugprint:
            print()
            print("is digit")
            print(x)
        if "cm" in x:
            if debugprint:
                print("is cm")
                print(x[:-2])
            if 150 <= int(x[:-2]) <= 193:
                points += 1
                if debugprint:
                    print("centimeter height correct", end=" ")
        elif "in" in x:
            if debugprint:
                print("is in")
                print(x[:-3])
            if 59 <= int(x[:-2]) <= 76:
                points += 1
                if debugprint:
                    print("inch height correct", end=" ")
    else:
        if debugprint:
            print("height digit check failed")

    if 2010 <= int(i["iyr"]) <= 2020:
            points += 1
            if debugprint:
                print("issue year correct", end=" ")
    
    x = i["pid"]
    digits = 0
    for n in x:
        if n.isdigit():
            digits+=1
    if digits == 9 and len(x) == 9:
        points+=1
        if debugprint:
            print("passport id correct", end=" ")
    if debugprint:
        pp(points, "\npoints")
    if points == 7:
        valid = True

    return valid


valids = 0
truevalids = 0
for p in passports:

    if "cid" in p:
        
        if len(p) == 8:
            
            valids += 1
            if checkfields(p, False):
                
                truevalids += 1


    else:
        if len(p) >= 7:
            if checkfields(p, False):
                truevalids += 1
            valids += 1
    
  


pp(valids, "number of valid passports")
pp(truevalids, "number of true valid passports")
pp(len(passports), "nr of passports")

