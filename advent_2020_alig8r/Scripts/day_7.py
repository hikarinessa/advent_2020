import os
import sys
import math
with open(os.path.join(sys.path[0], "../Inputs/input_day_7.txt"), "r") as my_input:
    _INPUT_1 = my_input.read().replace(".", "")
    _INPUT_1 = _INPUT_1.replace(" bags", "").replace(" bag", "").split("\n")
    _INPUT_1 = [i.split(" contain ") for i in _INPUT_1]
    #print(_INPUT_1)

final_gold_bags = 0
_OUTPUT_1 = 0
bag_dictionary = {}
bags_that_directly_contain_shiny_gold = []
contain_shiny_gold = []

def get_contains_bag(bag_to_scan, bag_to_look_for):
    #compare if bag_to_scan is same as bag_to_look_for
    if bag_to_scan[0] == bag_to_look_for[0] and bag_to_scan[1] == bag_to_look_for[1]:
        print("FOUND ONE!:", bag_to_scan, "IN: ", bag_to_look_for)
        return True
    else:
        return False


for i in _INPUT_1:
    #returns dict of bags AND initial bags that contain "shiny gold" 
    # DICT: bags_dictionary
    # 1st layer ShinyGolds: bags_that_directly_contain_shiny_gold
    contents_dict = []
    main_bag = i[:1]

    for contents in i[1:]:
        contents = contents.strip().split(", ")
        for bag in contents:
            if bag == "no other":
                contents_dict.append("None")
                contents_dict.append(0)
            else:
                amount = bag[:1]
                bag_type = bag[2:].split(" ")
                if get_contains_bag(bag_type, ["shiny", "gold"]):
                    print(bag, bag_type, i)
                    bags_that_directly_contain_shiny_gold.append(main_bag[0])
                    _OUTPUT_1 += 1

                contents_dict.append(bag_type)#("{} {}".format(bag_type[0], bag_type[1]))
                contents_dict.append(int(amount))
    
    bag_dictionary[main_bag[0]] = contents_dict

#print(bag_dictionary)
contain_shiny_gold_list = bags_that_directly_contain_shiny_gold
recurse = True

print(1 % 2) # returns 1
print(0 % 2) # returns 0
print(2 % 2) # returns 0

recurse = True
while recurse:
    for contained_bag in contain_shiny_gold_list:
        for key in bag_dictionary:
            for content_index in range(0, len(bag_dictionary[key])):
                if content_index % 2 == 0: # to remove the bag count from the list
                    bag = bag_dictionary[key][content_index]
                    if get_contains_bag(bag, contained_bag.split(" ")):
                        print("--DIE INSIDE--", bag, contained_bag.split(" "))
                        _OUTPUT_1 += 1
                        if key not in contain_shiny_gold_list:
                            contain_shiny_gold_list.append(key)
                            recurse = True
                        else:
                            recurse = False




print(_OUTPUT_1)
print(contain_shiny_gold)


