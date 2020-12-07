import re

with open("advent_07_input.txt", "r") as raw_input:
    INPUT = raw_input.read().split("\n")

MY_BAG = "shiny gold"
my_dict = {}

for regulation in INPUT:
    key = re.match("(\w+ \w+) bag", regulation).group(1)
    values = re.findall("(\d+) (\w+ \w+) bag", regulation)
    my_dict[key] = values  # "dotted gray" : [('1', 'dull tomato'), ('1', 'posh yellow')]


# How many bag colors can eventually contain at least one shiny gold bag?
def can_contain_my_bag(bags_dict):
    can_contain_my_bag_list = []
    # FIRST LEVEL OF BAGS
    for bag in bags_dict:
        for contained_bag in bags_dict[bag]:
            if MY_BAG in contained_bag:
                if bag not in can_contain_my_bag_list:
                    can_contain_my_bag_list.append(bag)
                    # print(bag, "can contain my bag")
    # RECURSIVE SEARCH
    recursive = True
    while recursive:
        nr_bags = 0
        for container in can_contain_my_bag_list:
            for bag in bags_dict:
                for contained_bag in bags_dict[bag]:
                    if container in contained_bag:
                        if bag not in can_contain_my_bag_list:
                            can_contain_my_bag_list.append(bag)
                            nr_bags += 1
                            # print(bag, "can contain a bag that can contain my bag")
        if nr_bags == 0:
            recursive = False

    return len(can_contain_my_bag_list)


# How many individual bags are required inside your single shiny gold bag?
def contained_in_my_bag(bags_dict):
    number_contained = 0
    bags_contained = bags_dict[MY_BAG]

    while len(bags_contained) != 0:
        times = int(bags_contained[0][0])
        number_contained += times
        for element in bags_dict[bags_contained[0][1]]:
            for i in range(times):
                bags_contained.append(element)
        bags_contained.pop(0)

    return number_contained


print("First Part:", can_contain_my_bag(my_dict))  # 289
print("Second Part:", contained_in_my_bag(my_dict))  # 30055
