set_of_els = {'str', 1, None, False, ('tuple', 'tuple')}

set_names = {'Denys', 'Alex', 'Sofa', "Denys"}

list_of_companies = ['apple', 'oracle', 'google']  # len(list_of_companies) = 3

set_of_companies = set(list_of_companies)  # перетворення set

print(list_of_companies)
print(set_of_companies)

has_no_duplicates = len(set_of_companies) == len(list_of_companies)
print('has_no_duplicates', has_no_duplicates)


# for name in set_names:
#     print(hash(name), name)
#
# print(1, 'hash of 1 =', hash(1))
# print(10, 'hash of 10 =', hash(10))
# print(353263245, 'hash of 353263245 =', hash(353263245))
# print('Denys', 'hash of Denys', hash('Denys'))
#
#
# print('Denys' in set_names)

