# A nice string is one with all of the following properties:
# It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
# It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
# It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.
# How many strings are nice?

#part 2: 
# It contains a pair of any two letters that appears at least twice in the string without 
# overlapping, like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).
# 
# It contains at least one letter which repeats with exactly one letter between them, 
# like xyx, abcdefeghi (efe), or even aaa.

print()
with open("AOC15/nicenaughty.txt") as f:
    data = f.readlines()

# print(data)

truelength = len(data[1])-1

for i in range(len(data)-1):
    data[i] = data[i][:truelength]

# print(data)
print(f"Desired length of the strings is: {truelength}")

number_of_nice_strings = 0
print(f"Number of strings: {len(data)}")

def checkvowels (string_to_check_vowels):
    s = string_to_check_vowels
    vowelcount = 0
    nice_vowel = False
    for i in range(len(s)):
        if s[i] == "a" or s[i] == "e" or s[i] == "i" or s[i] == "o" or s[i] == "u":
            vowelcount += 1
        if vowelcount == 3:
            nice_vowel = True
            break
    return nice_vowel

def checkdoubles (string_to_check_doubles):
    s = string_to_check_doubles
    nice_double = False
    for i in range(len(s)-1):
        if s[i+1] == s[i]:
            nice_double = True
            break
    return nice_double

def checkcombos (string_to_check_combos):
    s = string_to_check_combos
    nice_combo = True
    for i in range(len(s)-1):
        if s[i] == "a" and s[i+1] == "b":
            nice_combo = False
            break
        elif s[i] == "c" and s[i+1] == "d":
            nice_combo = False
            break
        elif s[i] == "p" and s[i+1] == "q":
            nice_combo = False
            break
        elif s[i] == "x" and s[i+1] == "y":
            nice_combo = False
            break
    return nice_combo

def checkpairs (string_to_check_pairs, debug = False):
    #It contains a pair of any two letters that appears at least twice in the string without 
    # overlapping, like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).
    s = string_to_check_pairs
    nice_pair = False
    for i in range(len(s) - 3):
        sub = s[i: i + 2]
        if sub in s[i + 2:]:
            nice_pair = True
            print("{} is really nice and repeats with {}".format(s, sub))
    return nice_pair

def checksandwiches (string_to_check_sandwiches, debug = False):
    # It contains at least one letter which repeats with exactly one letter between them, 
    # like xyx, abcdefeghi (efe), or even aaa.
    s = string_to_check_sandwiches
    nice_sandwich = False
    for i in range(len(s)-2):
        if s[i] == s[i+2]:
            nice_sandwich = True
            if debug:
                print("{} is really nice and sandwiches with {}".format(s, s[i:i+3]))
    return nice_sandwich

for i in range(len(data)):
    if checkvowels(data[i]) and checkdoubles(data[i]) and checkcombos(data[i]):
        number_of_nice_strings += 1
print(f"Number of nice strings, Part 1: {number_of_nice_strings}")
number_of_nice_strings = 0

for i in range(len(data)):
    if checkpairs(data[i], True) and checksandwiches(data[i], True):
        number_of_nice_strings += 1

def testpart2 (s, debug = False):
    nice = False
    score = 0
    if checkpairs(s, True):
        print(f"{s} has non-overlapping pairs..")
        score += 1
    if checksandwiches(s, True):
        print(f"{s} has a nice sandwich..")
        score += 1
    if score >= 2:
        nice = True
        print(f"{s} is nice!")
    else:
        print(f"{s} is naughty!") 
    return nice

# For example:
# qjhvhtzxzqqjkmpb is nice because is has a pair that appears twice (qj) 
# and a letter that repeats with exactly one letter between them (zxz).

test = "qjhvhtzxzqqjkmpb"
print(f"\n{test} is supposed to be nice")
testpart2(test)

# xxyxx is nice because it has a pair that appears twice and a letter that 
# repeats with one between, even though the letters used by each rule overlap.

test = "xxyxx"
print(f"\n{test} is supposed to be nice")
testpart2(test)

# uurcxstgmygtbstg is naughty because it has a pair (tg) but no repeat with a single letter between them.

test = "uurcxstgmygtbstg"
print(f"\n{test} is supposed to be naughty")
testpart2(test)

# ieodomkazucvgmuy is naughty because it has a repeating letter with one between (odo), but no pair that appears twice.

test = "ieodomkazucvgmuy"
print(f"\n{test} is supposed to be naughty")
testpart2(test, True)

print(f"\nNumber of nice strings, Part 2: {number_of_nice_strings}")
    


        
