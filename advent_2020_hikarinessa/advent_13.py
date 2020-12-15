# https://adventofcode.com/2020/day/13
import os
import sys
import time
import datetime as dt

with open(os.path.join(sys.path[0], "Inputs/advent_13_input.txt"), "r") as raw_input:
    INPUT = raw_input.read().replace("x", "0").splitlines()
TIMESTAMP = int(INPUT[0])
INPUT = INPUT[1].split(",")
INPUT_2 = [int(i) for i in INPUT]
INPUT_1 = [i for i in INPUT_2 if i != 0]

TEST_TIMESTAMP = 939
TEST_INPUT_1 = [7, 13, 59, 31, 19]  # ["7", "13", "x", "x", "59", "x", "31", "19"]
TEST_INPUT_2 = [7, 13, 0, 0, 59, 0, 31, 19]  # earliest_timestamp 1068781
TEST_INPUT_3 = [17, 0, 13, 19]  # earliest_timestamp 3417
TEST_INPUT_4 = [67, 0, 7, 59, 61]  # earliest_timestamp 779210
TEST_INPUT_5 = [1789, 37, 47, 1889]  # earliest_timestamp 1202161486 took 3m


def find_next_bus(bus_list, timestamp):
    next_bus = []
    for bus in bus_list:
        next_bus.append(bus - (timestamp % bus))
    min_time = min(next_bus)
    min_bus_index = next_bus.index(min_time)
    min_bus = bus_list[min_bus_index]
    return min_bus * min_time


def find_contest_timestamp_0(bus_list, start_time, debug):
    timestamp = start_time

    if debug:
        t = dt.datetime.now()
        print("Start:", time.strftime("%H:%M:%S", time.gmtime(time.time())))

    while True:  # 68,517,066 calc per min
        mismatch = True
        if timestamp % bus_list[0] == 0:
            for i, bus in enumerate(bus_list[1:]):
                if bus == 0:
                    continue
                # if debug: print(timestamp, i, bus, i-1==bus-(timestamp%bus))
                if i + 1 != bus - (timestamp % bus):
                    mismatch = False
                    break
            if mismatch:
                break

        if debug:
            delta = dt.datetime.now()-t
            if delta.seconds >= 60:
                print(time.strftime("%H:%M:%S", time.gmtime(time.time())), timestamp)
                t = dt.datetime.now()
        timestamp += 1

    return timestamp


def find_contest_timestamp_1(bus_list, debug):
    timestamp = 1
    step = 1
    step_i = 0

    if debug:
        t = dt.datetime.now()
        print("Start:", time.strftime("%H:%M:%S", time.gmtime(time.time())))

    while True:  # 1,108,758,709,241 calc per min
        mismatch = True

        if timestamp % bus_list[0] == 0:
            for i, bus in enumerate(bus_list[1:]):
                if bus == 0:
                    continue
                if i + 1 == bus - (timestamp % bus):
                    if step_i < i:
                        step_i = i
                        step *= bus
                        if debug: print("timestamp", timestamp, "/ step:", step,
                                        "/ step index , bus:", step_i+1, ",", bus)
                else:
                    mismatch = False
                    break
            if mismatch:
                break

        if debug:
            delta = dt.datetime.now()-t
            if delta.seconds >= 60:
                print(time.strftime("%H:%M:%S", time.gmtime(time.time())), timestamp)
                t = dt.datetime.now()

        timestamp += step

    return timestamp


def find_contest_timestamp_2(bus_list, debug):  # faster!
    timestamp = bus_list[0]
    step = timestamp
    bus_list_temp = bus_list.copy()
    bus_list_temp[0] = 0

    if debug:
        t = dt.datetime.now()
        print("Start:", time.strftime("%H:%M:%S", time.gmtime(time.time())))

    while True:  # 12,244,802,755,518 calc per min
        mismatch = True
        # if debug: print("While loop:", timestamp)
        for i, bus in enumerate(bus_list_temp):
            if bus == 0:
                continue
            if i == bus - (timestamp % bus):
                bus_list_temp[i] = 0
                step *= bus
                if debug: print("timestamp", timestamp, "/ step:", step, "/ bus:", bus)
            else:
                mismatch = False
                break
        if mismatch:
            break

        if debug:
            delta = dt.datetime.now()-t
            if delta.seconds >= 60:
                print(time.strftime("%H:%M:%S", time.gmtime(time.time())), timestamp)
                t = dt.datetime.now()

        timestamp += step

    return timestamp


def find_contest_timestamp(bus_list, debug):  # faster!
    timestamp = 3129186106711705417  # bus_list[0] # 1375613061977991312
    step = bus_list[0] # timestamp # 298798939
    bus_dict = {}
    for i, val in enumerate(bus_list[1:]):
        if val != 0:
            bus_dict[i + 1] = val
    print(bus_dict)

    if debug:
        t = dt.datetime.now()
        print("Start:", time.strftime("%H:%M:%S", time.gmtime(time.time())))

    while True:  # 34,551,871,871,485 calc per min
        mismatch = True
        # if debug: print("While loop:", timestamp)
        for i, bus in bus_dict.items():
            if bus is not None:
                if i == bus - (timestamp % bus):
                    bus_dict[i] = None
                    step *= bus
                    if debug: print("timestamp", timestamp, "/ step:", step, "/ bus:", bus)
                else:
                    mismatch = False
        if mismatch:
            break

        if debug:
            delta = dt.datetime.now()-t
            if delta.seconds >= 60:
                print(time.strftime("%H:%M:%S", time.gmtime(time.time())), timestamp)
                t = dt.datetime.now()

        timestamp += step

    return timestamp


print("First part:", find_next_bus(INPUT_1, TIMESTAMP))  # 261
print("Second part:", find_contest_timestamp(INPUT_2, True))  #

# 211,846,997,258,098
# 241,170,491,015,267
# 760,890,796,625,962
# 415,487,199,821,558,813
# 858,550,698,356,622,061
# 836,856,048,822,287

