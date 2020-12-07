with open("advent_06_input.txt", "r") as raw_input:
    INPUT = raw_input.read().replace(" ", "\n")
    INPUT = INPUT.split("\n\n")

for i in range(len(INPUT)):
    INPUT[i] = INPUT[i].replace("\n", " ")


def unique_answers(group_list):
    total_answers = 0

    for group_answer in range(len(group_list)):
        valid_chars = group_list[group_answer].replace(" ", "")
        valid_chars = len(list(set(valid_chars)))
        total_answers += valid_chars

    return total_answers


def same_answer(group_list):
    total_answers = 0

    for group_answer in range(len(group_list)):
        split_list = group_list[group_answer].split()
        valid_chars = group_list[group_answer].replace(" ", "")
        valid_chars = list(set(valid_chars))
        # print(split_list, "-", valid_chars)

        for char in valid_chars:
            occurrence = 0
            for j in split_list:
                if char in j:
                    occurrence += 1

            if occurrence == len(split_list):
                total_answers += 1

    return total_answers


print("First part:", unique_answers(INPUT))  # 6437
print("Second part:", same_answer(INPUT))  # 3229
