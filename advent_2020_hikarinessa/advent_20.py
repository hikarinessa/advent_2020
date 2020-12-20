# https://adventofcode.com/2020/day/20
from utilities import *
import os
import sys

with open(os.path.join(sys.path[0], "Inputs/advent_19_input.txt"), "r") as raw_input:
    INPUT = raw_input.read().split("\n\n")


def main():
    pass


if __name__ == "__main__":
    start_time = start_timer()
    # print("First part:", main(INPUT))
    print_elapsed_time(start_time)
    print("*"*96)
    start_time = start_timer()
    # print("Second part:", main(INPUT))
    print_elapsed_time(start_time)
