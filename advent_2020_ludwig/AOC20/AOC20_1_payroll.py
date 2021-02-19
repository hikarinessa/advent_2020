# https://adventofcode.com/2020/day/1
# https://www.reddit.com/r/adventofcode/comments/k4e4lm/2020_day_1_solutions/
# Specifically, they need you to find the two entries that sum to 2020 
# and then multiply those two numbers together.

# For example, suppose your expense report contained the following:

# In this list, the two entries that sum to 2020 are 1721 and 299. Multiplying them 
# together produces 1721 * 299 = 514579, so the correct answer is 514579.

from itertools import combinations
import time
debug = False
steps = 0
a, b, c = 0, 0, 0

def pp(subject, name): #prints anything with a name as string 
    if debug or True:
        #print()
        print(f"{name}: {subject}")

print("\n----------------------------------")   # reading file
file = "advent_2020_ludwig/AOC20/data_aoc20_1.txt"



if debug:
    data = [1721, 979, 366, 299, 675, 1456]
else:
    with open(file) as f:
        data = f.read()
    data = [int(x) for x in data.splitlines()]
pp(len(data), "Items in data")

#ombs = 
tic = time.perf_counter()
print([c for c in combinations(data, 2) if sum(c) == 2020])
toc = time.perf_counter()
print("This took ", toc-tic, "seconds")
tic = time.perf_counter()
print([c for c in combinations(data, 3) if sum(c) == 2020])
toc = time.perf_counter()
print("This took ", toc-tic, "seconds")
# part1
tic = time.perf_counter()
running = True
for i in data:
    for j in data:
        steps += 1
        if i + j == 2020:
            running = False
            a, b = i, j
            break
    if not running:
       break
toc = time.perf_counter()
print("Part1: The numbers adding up to 2020 are: ", a, " and ", b) 
print("Their product is: ", a*b, " Calculation took ", steps, " steps.")
print("This took ", toc-tic, "seconds")

#part2
tic = time.perf_counter()
steps = 0   
running = True
for i in data:
    for j in data:
        for k in data:
            steps += 1
            if i + j + k == 2020:
                running = False
                a, b, c = i, j, k
                break
        if not running:
            break
    if not running:
        break    
toc = time.perf_counter()

print("Part2: The numbers adding up to 2020 are: ", a, ", ", b, " and ", c) 
print("Their product is: ", a*b*c, " Calculation took ", steps, " steps.")
print("This took ", toc-tic, "seconds")