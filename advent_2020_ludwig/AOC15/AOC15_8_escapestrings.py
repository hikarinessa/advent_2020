# "" is 2 characters of code (the two double quotes), but the string contains zero characters.
# "abc" is 5 characters of code, but 3 characters in the string data.
# 
# "aaa\"aaa" is 10 characters of code, but the string itself contains 
# six "a" characters and a single, escaped quote character, for a total of 7 characters in the string data.
# 
# "\x27" is 6 characters of code, but the string itself contains 
# just one - an apostrophe ('), escaped using hexadecimal notation.
# 
# Santa's list is a file that contains many double-quoted string literals, 
# one on each line. The only escape sequences used are \\ (which represents 
# a single backslash), \" (which represents a lone double-quote character), 
# and \x plus two hexadecimal characters (which represents a single character with that ASCII code).

# Disregarding the whitespace in the file, what is the number of characters of code 
# for string literals minus the number of characters in memory for the values of 
# the strings in total for the entire file?

# For example, given the four strings above, the total number of characters of string 
# code (2 + 5 + 10 + 6 = 23) minus the total number of characters in memory 
# for string values (0 + 3 + 7 + 1 = 11) is 23 - 11 = 12.

debug = False

def pp(subject, name): #prints anything with a name as string 
    if debug or True:
        #print()
        print(f"{name}: {subject}")

print("\n----------------------------------")   # reading file
file = "AOC15/escapestrings.txt"
if debug:
    file = "AOC15/escapestringstest.txt"

with open(file) as f:
    data = f.read()
data = data.splitlines()
#pp(data, "data")

minus = 0
plus = 0
result = 0
testresult = 0

esc = r"\\\""
esc4 = r"\\\\"
escx = r"\\\x"
print(esc[0])
print(esc[3])

loopwhilemy = 0
loopslashmy = 0
loopslashxmy = 0
loopslashelsemy = 0
loopelsemy = 0

def counti(i):
    sub = 0
    x = 0
    i = i[1:-1]
    global loopwhilemy, loopslashmy, loopslashxmy, loopslashelsemy, loopelsemy
    while x < len(i):
        loopwhilemy += 1
        sub+=1
        if i[x] == "\\":
            loopslashmy +=1
            if i[x+1] == "x":
                loopslashxmy+=1
                x+=4
            else:
                loopslashelsemy+=1
                x+=2
        else:
            loopelsemy+=1
            x+=1
    return sub

for i in data:
    sub = 0
    add = len(i)
    sub = counti(i)
    # while x < len(i[1:-1]):
    #     loopwhilemy += 1
    #     sub+=1
    #     if i[x] == "\\":
    #         loopslashmy +=1
    #         if i[x+1] == "x":
    #             loopslashxmy+=1
    #             x+=4
    #         else:
    #             loopslashelsemy+=1
    #             x+=2
    #     else:
    #         loopelsemy+=1
    #         x+=1
        
    pp(i, "line")
    pp(add, "add")
    pp(sub, "sub")
    minus += sub
    plus += add

loopwhileyr = 0
loopslashyr = 0
loopslashxyr = 0
loopslashelseyr = 0
loopelseyr = 0

def count_characters(s):
    global loopwhileyr, loopslashyr, loopslashxyr, loopslashelseyr, loopelseyr
    s = s[1:-1]
    length = i = 0
    while i < len(s):
        loopwhileyr+=1
        length += 1
        if s[i] == "\\":
            loopslashyr+=1
            if s[i+1] == "x":
                loopslashxyr+=1
                i += 4
            else:
                loopslashelseyr+=1
                i += 2
        else:
            loopelseyr+=1
            i += 1
    return length

for x in data:
    testresult += count_characters(x)

testresult = plus - testresult

pp(testresult, "testresult")
    

result = plus - minus

print("total characters:")
pp(plus, "plus")
print("code chars to subtract:")
pp(minus, "minus")
print("result of subtraction:")
pp(result, "=")

pp(loopwhilemy, "loopwhilemy")
pp(loopwhileyr, "loopwhileyr")
pp(loopslashmy, "loopslashmy")
pp(loopslashyr, "loopslashyr")
pp(loopslashxmy, "loopslashxmy")
pp(loopslashxyr, "loopslashxyr")
pp(loopslashelsemy, "loopslashelsemy")
pp(loopslashelseyr, "loopslashelseyr")
pp(loopelsemy, "loopelsemy")
pp(loopelseyr, "loopelseyr")


            

        