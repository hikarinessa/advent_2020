#To do this, he needs to find MD5 hashes which, in hexadecimal, start with at least five zeroes. 
# The input to the MD5 hash is some secret key (your puzzle input, given below) followed by a 
# number in decimal. To mine AdventCoins, you must find Santa the lowest positive number 
# (no leading zeroes: 1, 2, 3, ...) that produces such a hash.

#For example:

#If your secret key is abcdef, the answer is 609043, because the MD5 hash of abcdef609043 
# starts with five zeroes (000001dbbfa...), and it is the lowest such number to do so.
#If your secret key is pqrstuv, the lowest number it combines with to make an MD5 hash 
# starting with five zeroes is 1048970; that is, the MD5 hash of pqrstuv1048970 looks like 000006136ef....
#Your puzzle input is bgvyzdsv.

import hashlib

inputstr = "bgvyzdsv"
inputnr = 1

input = inputstr + str(inputnr)
print("input is right now:")
print(input)

input_encoded = input.encode()
print("encoded input is:")
print(input_encoded)

input_hashed = hashlib.md5(input_encoded)
print(f"\nhashed input is: {input_hashed}, \ndigested: {input_hashed.digest()}, \nhexdigested: {input_hashed.hexdigest()}")
print()

tries = 10000000

for i in range(tries):
    numberofzeroes = 0
    inputnr = i + 1
    input = inputstr + str(inputnr)
    input_hashed = hashlib.md5(input.encode())
    inputhex = input_hashed.hexdigest()
    inputhex_string = str(inputhex)

    #replace with 5 for part 1
    for i in range(6): 
        #print(".", end="", flush=True)
        if inputhex_string[i] == "0":
            numberofzeroes += 1
    #print()

    #replace with 5 for part 1
    if numberofzeroes == 6:
        break

print("winning inputnr:")
print(inputnr)
print("winning hash:")
print(inputhex)    



