with open("advent_06_input.txt", "r") as raw_input:
    INPUT = raw_input.read().split("\n\n")

for i in range(len(INPUT)):
    INPUT[i] = INPUT[i].replace("\n", " ")


def unique_answers(group_list):
    total_answers = 0

    for group_answer in range(len(group_list)):
        valid_chars = group_list[group_answer].replace(" ", "")
        valid_chars = len(set(valid_chars))
        total_answers += valid_chars

    return total_answers


# region ---- my original function for the second star ----
# def same_answer(group_list):
#     total_answers = 0
#
#     for group_answer in range(len(group_list)):
#         split_list = group_list[group_answer].split()
#
#         for char in split_list[0]:
#             occurrence = 0
#             for j in split_list:
#                 if char in j:
#                     occurrence += 1
#
#             if occurrence == len(split_list):
#                 total_answers += 1
#
#     return total_answers
# endregion -----------------------------------------------


# improved function with a set intersection
def same_answer(group_list):
    """Given a list where elements are group answers, split by a space
    returns the compound number of elements that appear on all answers of each group.
    input = ['f f f f', 'dbifho zmdh hobd']
    1 element is common to all answers of the first group
    2 elements (h, d) are common to all answers of the second group
    function returns 3 (1 + 2)
    """
    total_answers = 0

    for group_answer in range(len(group_list)):
        split_list = group_list[group_answer].split()

        answers = split_list[0]
        for answer in split_list:
            answers = set(answers).intersection(answer)  # set intersection preserves repeated values (Boolean)

        total_answers += len(answers)

    return total_answers


print("First part:", unique_answers(INPUT))  # 6437
print("Second part:", same_answer(INPUT))  # 3229
