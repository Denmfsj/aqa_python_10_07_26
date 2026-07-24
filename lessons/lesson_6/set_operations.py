# set_names = {'Denys', 'Alex', 'Sofa'}
#
# list_of_friends = ['Denys', 'Ivan', 'Olha']
#
#
# union = set_names.union(list_of_friends)  # всі елементи
# difference = set_names.difference(list_of_friends)  # тільки те що є в set_names
# sym_difference = set_names.symmetric_difference(list_of_friends)  # тільки те що є в set_names
# intersection = set_names.intersection(list_of_friends)
#
#
# print('union', union)
# print('intersection', intersection)
# print('difference', difference)
# print('sym_difference', sym_difference)
#
#
# list_of_ids_page_1 = [1,2,4,7,8,44,100]
# list_of_ids_page_2 = [33,55,4,22,66,88]
#
# has_the_same_ids_on_diff_pages = set(list_of_ids_page_1).intersection(list_of_ids_page_2)
#
# pages_intersection = set(list_of_ids_page_1) & set(list_of_ids_page_2)
#
# print('els from page 1 on page 2:', pages_intersection)

set_names = {'Denys', 'Alex', 'Sofa'}
print(set_names)

set_names.add('Ivan')  # альтернатива append в списках
print(set_names)

set_names.update(['Denys 1', 'Olha'])  # альтернатива extend в списках
print(set_names)

set_names.remove('Denys 1')
print(set_names)

random_el = set_names.pop()
print(f'{random_el} was removed from the set')
print(set_names)

