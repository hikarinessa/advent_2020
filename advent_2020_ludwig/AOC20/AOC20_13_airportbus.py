# https://adventofcode.com/2020/day/13

data = """939
7,13,x,x,59,x,31,19"""

from operator import itemgetter

debug = False
printit = False
def pp(subject, name = "", override = False): #prints anything with a name as string 
    if debug or printit or override:
        #print("\n", name, ": ", subject)
        print(name, ": ", subject)

print("\n----------------------------------")   # reading file

file = "advent_2020_ludwig/AOC20/data_aoc20_12.txt"

if not debug:
    data = """1000507
29,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,37,x,x,x,x,x,631,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,13,19,x,x,x,23,x,x,x,x,x,x,x,383,x,x,x,x,x,x,x,x,x,41,x,x,x,x,x,x,17"""

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
    if busindex > 0:
        while (time + busindex) % busid != 0:  # apparently easy with math \_[##]_/
            time += timestep
        timestep *= busid
    else:
        firstbustime = bustime

pp(time, "final time", True)

'''# ------Graveyard of the brute force approach.. Ran for an hour, and not even close to figuring it out.
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




