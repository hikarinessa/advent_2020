# https://adventofcode.com/2020/day/12

# Bus schedules are defined based on a timestamp that measures the number of minutes since some fixed 
# reference point in the past. At timestamp 0, every bus simultaneously departed from the sea port. 
# After that, each bus travels to the airport, then various other locations, and finally returns 
# to the sea port to repeat its journey forever.

# The time this loop takes a particular bus is also its ID number: the bus with ID 5 departs from the sea port 
# at timestamps 0, 5, 10, 15, and so on. The bus with ID 11 departs at 0, 11, 22, 33, and so on. If you are 
# there when the bus departs, you can ride that bus to the airport!

# Your notes (your puzzle input) consist of two lines. The first line is your estimate of the earliest 
# timestamp you could depart on a bus. The second line lists the bus IDs that are in service according to 
# the shuttle company; entries that show x must be out of service, so you decide to ignore them.

# To save time once you arrive, your goal is to figure out the earliest bus you can take to the airport. 
# (There will be exactly one such bus.)

data = """939
7,13,x,x,59,x,31,19"""

# Here, the earliest timestamp you could depart is 939, and the bus IDs in service are 7, 13, 59, 31, and 19. 

# The earliest bus you could take is bus ID 59. It doesn't depart until timestamp 944, so you would need 
# to wait 944 - 939 = 5 minutes before it departs. 
# Multiplying the bus ID by the number of minutes you'd need to wait gives 295.
# 
# What is the ID of the earliest bus you can take to the airport multiplied by 
# the number of minutes you'll need to wait for that bus?

# PART 2 ----------




# The shuttle company is running a contest: one gold coin for anyone that can find the earliest 
# timestamp such that the first bus ID departs at that time and each subsequent listed bus ID 
# departs at that subsequent minute. (The first line in your input is no longer relevant.)

# An x in the schedule means there are no constraints on what bus IDs must depart at that time.

# This means you are looking for the earliest timestamp (called t) such that:

# Bus ID 7 departs at timestamp t.
# Bus ID 13 departs one minute after timestamp t.
# There are no requirements or restrictions on departures at two or three minutes after timestamp t.
# Bus ID 59 departs four minutes after timestamp t.
# There are no requirements or restrictions on departures at five minutes after timestamp t.
# Bus ID 31 departs six minutes after timestamp t.
# Bus ID 19 departs seven minutes after timestamp t.
# The only bus departures that matter are the listed bus IDs at their specific offsets from t. Those bus IDs can depart at other times, and other bus IDs can depart at those times. For example, in the list above, because bus ID 19 must depart seven minutes after the timestamp at which bus ID 7 departs, bus ID 7 will always also be departing with bus ID 19 at seven minutes after timestamp t.

# In this example, the earliest timestamp at which this occurs is 1068781

from operator import itemgetter
debug = False
printit = False
def pp(subject, name = "", override = False): #prints anything with a name as string 
    if debug or printit or override:
        #print("\n", name, ": ", subject)
        print(name, ": ", subject)

print("\n----------------------------------")   # reading file

file = "AOC20/data_aoc20_12.txt"
''
if not debug:
    data = """1000507
29,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,37,x,x,x,x,x,631,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,13,19,x,x,x,23,x,x,x,x,x,x,x,383,x,x,x,x,x,x,x,x,x,41,x,x,x,x,x,x,17"""
''
data = [s for s in data.split("\n")]
earliestdeparture = int(data[0])
pp(earliestdeparture, "earliestdep")
data = data[1].split(",")
busses = []
for entry in data:
    if entry != "x":
        busses.append(int(entry))

pp(busses, "busses")
possibledepartures = []

for bus in busses:
    departure = bus
    while departure < earliestdeparture:
        departure += bus
    possibledepartures.append([bus, departure])

pp(possibledepartures, "possible departures unsorted")

possibledepartures = sorted(possibledepartures, key=itemgetter(-1))
pp(possibledepartures, "possible departures sorted")

earliestbus = possibledepartures[0]
pp(earliestbus, "earliest bus")

result = earliestbus[0] * (earliestbus[1]-earliestdeparture)
pp(result, "bus id multiplied by minutes to wait for bus")

# part 2
debug = False
#data = [17,"x",13,19] #3417
#data = [67,7,59,61] #754018
#data = [67,"x",7,59,61] #779210
#data = [67,7,"x",59,61] #1261476
#data = [1789,37,47,1889] #1202161486

time = 0
bussesp2 = []
for i, entry in enumerate(data):
    if entry != "x":
        bussesp2.append([int(entry), i, time])
        #bussesp2[int(entry)] = i

pp(bussesp2, "busses with their index", True)
#bussessp2[x] = [id, index, time]
solutionfound = False

numberofbusses = len(bussesp2)
pp(numberofbusses, "number of busses", True)
timestep = 0
for bus in bussesp2:
    if bus[0] > timestep:
        timestep = bus[0]

timestep = bussesp2[0][0]

pp(timestep, "time step", True)
firstbustime = 0
time2 = 15

for i, bus in enumerate(bussesp2):
    busid, busindex, bustime = bus[0], bus[1], bus[2]
    pp(bus, "--bus to check")
    #while bustime <= time:
        #   bustime += busid
        #  pp(bustime, "---increasing bustime")
    if busindex > 0:
        #busbeforetime = bussesp2[i-1][2]
        #while bustime < busbeforetime or bustime <= (firstbustime+busindex):
            #   bustime += busid
        while (time + busindex) % busid != 0:
            time += timestep
        timestep *= busid
    else:
        firstbustime = bustime

pp(time, "final time", True)

'''
while not solutionfound:
#while time2 != time:
#while time < 200000000000000:
    #        100000000000000
    pp(time, "-current time", True)
    for i, bus in enumerate(bussesp2):
        busid, busindex, bustime = bus[0], bus[1], bus[2]
        pp(bus, "--bus to check")
        #while bustime <= time:
         #   bustime += busid
          #  pp(bustime, "---increasing bustime")
        if busindex > 0:
            #busbeforetime = bussesp2[i-1][2]
            #while bustime < busbeforetime or bustime <= (firstbustime+busindex):
             #   bustime += busid
            while (time + busindex) % busid != 0:
                time += timestep
            timestep *= busid
        else:
            firstbustime = bustime
        bussesp2[i] = [busid, busindex, bustime] 
        pp(bussesp2[i], "--updated bus")
    matches = 0
    pp(numberofbusses, "-------------number of busses/matches needed")
    for i, bus in enumerate(bussesp2[1:]):
        pp(bus, "----bus to check match")
        pp(bussesp2[i-1], "----previous bus to check match")
        busindex, bustime = bus[1], bus[2]
        difference = bustime - firstbustime
        pp(difference, "-----difference between busses")
        if difference == busindex:
            matches += 1
            pp(matches, "--------matches increased!")
    #pp(bussesp2, "busses", True) 
    #pp(matches, "matches", True)   
    if matches == numberofbusses-1:
        solutionfound = True
        print("---------------------------SUCCESS")
        pp(bussesp2, "busses at moment of solution", True)
        pp(firstbustime, "departure time for first bus where every subsequent bus is departing at index minutes later", True)

    #time += timestep


'''




