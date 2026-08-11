#all()
#any()

one_false = [1, 5, True, 'asd', '']
all_true = [1, 5, True, 'asd']

res_all_one_false = all(one_false)

# print('all one_false', res_all_one_false)  # False
# print('all all_true', all(all_true))  # True
#
# print('any one_false', any(one_false))  # True
# print('any all_true', any(all_true))  # True


# sent = "Виконує вираз Python з довільними глобальними та локальними змінними.".split()

# for index_of_w, word in enumerate(sent): # == > [(0, Виконує), (1, вираз), (2, Python)]
#     print(f'word {word} has in index {index_of_w}')

expected_user_ids = [11,33,44,55,7789]
actual_user_ids = [11,33,44,56,7789]


def comparing_2_lists_el_by_element(lst_1, slt_2):

    if lst_1 == slt_2:
        return

    for user_index, expected_id in enumerate(lst_1):
        actual_id = slt_2[user_index]
        if expected_id != slt_2[user_index]:
            res = f'[{user_index}]   ===>   {expected_id} | {actual_id}   <== actual'
            print(res)


comparing_2_lists_el_by_element(expected_user_ids, actual_user_ids)
comparing_2_lists_el_by_element([1,2,777], [55,6,4])

