import os
import sys
import re

INPUT_TXT = "../Input/07_HandyHaversacks.txt"
MY_BAG = "shiny gold"


class Bag:
    def __init__(self, color):
        self.color = color
        self.parents = []  # Bags that this bag can be contained within
        self.children = {}  # Bags that this bag can contain : number contained

    def add_parent(self, new_parent):
        self.parents.append(new_parent)

    def add_child(self, new_child, count):
        self.children[new_child] = count


def get_input():  # Stealing Luz's idea of not pasting 5000 lines of input into the script
    with open(os.path.join(sys.path[0], INPUT_TXT), "r") as my_input:
        return my_input.read()


def create_bag_dict(rules):
    bag_dict = {}

    for rule in rules.splitlines():
        bag_name = rule.partition(" bag")[0]
        contents = re.findall(r"\d \w*\s\w*", rule)
        _register_bag(bag_dict, bag_name)

        for content in contents:
            child_count, _space, child_name = content.partition(" ")
            _register_bag(bag_dict, child_name)
            bag_dict[bag_name].add_child(child_name, int(child_count))
            bag_dict[child_name].add_parent(bag_name)

    return bag_dict


def part_one(rules):
    bag_dict = create_bag_dict(rules)
    valid_parents = list()
    parent_stack = bag_dict[MY_BAG].parents

    while len(parent_stack) > 0:
        p = parent_stack.pop()
        if p not in valid_parents:
            valid_parents.append(p)
        parent_stack.extend(bag_dict[p].parents)

    print("*"*96)
    print("PART ONE")
    print("{} different bags can eventually contain a shiny gold bag.".format(len(valid_parents)))


def part_two(rules):
    bag_dict = create_bag_dict(rules)
    child_count = 0
    child_stack = [bag_dict[MY_BAG]]
    while len(child_stack) > 0:
        child_count += 1
        c = child_stack.pop()
        for child, count in c.children.items():
            for i in range(count):
                child_stack.append(bag_dict[child])

    print("*" * 96)
    print("PART TWO")
    print("My shiny gold bag contains {} other bags!".format(child_count - 1))


def _register_bag(bag_dict, bag_name):
    if bag_name not in bag_dict.keys():
        bag_dict[bag_name] = Bag(bag_name)
        return True
    else:
        return False


if __name__ == "__main__":
    part_one(get_input())
    part_two(get_input())
