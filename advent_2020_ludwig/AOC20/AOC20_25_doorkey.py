# https://adventofcode.com/2020/day/25

debug = False
printit = False

def p(text = "", override = False): #prints as string 
    if debug or printit or override:
        print(text, flush=True)
def pp(subject, name = "", override = False): #prints anything with a name as string 
    if debug or printit or override:
        #print("\n", name, ": ", subject)
        #   print()
        print(name, ": ", subject)
def ppp(subject, name = "", override = False, isDictionary=False): #prints list entries
    if debug or printit or override:
        #print("\n", name, ": ", subject)
        print()
        print(name, ": ")
        for item in subject:
            if isDictionary:
                print(item, ":", end="")
                print(subject[item])
            else:
                print(item)
def pppp(subject, name = "", override = False, isDictionary=False): #prints list's list entries without linebreak
    if debug or printit or override:
        #print("\n", name, ": ", subject)
        print()
        print(name, ": ")
        for item in subject:
            print()
            if isDictionary:
                print(item, ":", end="")
                print(subject[item])
            else:
                for tile in item:
                    
                    print(tile, end="")

print("\n----------------------------------")   # reading file

DATA = """5764801
17807724"""

if not debug: 
    DATA = """13135480
8821721"""   
    

DATA = [int(line) for line in DATA.split("\n")]

card_public_key = DATA[0]
door_public_key = DATA[1]

pp(card_public_key, "card's publick key")
pp(door_public_key, "doors public key")

subject_number = 7

# Set the value to itself multiplied by the subject number.
# Set the value to the remainder after dividing the value by 20201227.

card_value = 1
door_value = 1
card_loop_size = 0
door_loop_size = 0

def loop_size (value, subject, public_key):
    loop_size = 0
    while value != public_key:
        loop_size += 1
        #pp(loop_size, "current loop size")
        value *= subject
        #pp(value, "value after multiplying by subject number")
        value = value % 20201227
        #pp(value, "value after setting to remainder")

    return(loop_size)    

def encryption_key (value, public_key, loop_size):
    loop = 0
    subject = public_key
    while loop < loop_size:
        
        pp(loop, "Loop")
        value *= subject
        pp(value, "value after multiplying by subject number")
        value = value % 20201227
        pp(value, "value after setting to remainder")
        loop += 1
    p()

    return(value)  
    
card_loop_size = loop_size(card_value, subject_number, card_public_key)
pp(card_loop_size, "\nThe card's loop size\n")
door_loop_size = loop_size(door_value, subject_number, door_public_key)
pp(door_loop_size, "\nThe door's loop size\n")

card_encryption_key = encryption_key(card_value, door_public_key, card_loop_size)
door_encryption_key = encryption_key(door_value, card_public_key, door_loop_size)

if card_encryption_key == door_encryption_key:
    p(f"Handshake success with encryption key {card_encryption_key}", True)
else:
    p(f"Handshake failed. Card key: {card_encryption_key}, Door: {door_encryption_key}", True)
