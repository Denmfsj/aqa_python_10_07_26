

my_tuple_of_tuples = (1, 2, 'asdasd', None, False, 3.13, (1, 2, 'asdasd'), 3, 'asdasd', 3)

print(my_tuple_of_tuples[2])  # asdasd
print(my_tuple_of_tuples[3])  # None
print(my_tuple_of_tuples[6])  # (1,2, 'asdasd')

inside_tuple = my_tuple_of_tuples[6]

print(inside_tuple[2])  # asdasd


print(my_tuple_of_tuples[6][2])  # -> (1,2, 'asdasd')[2]  -> asdasd


print(my_tuple_of_tuples.count(88))

# True = bool(1)
# False = bool(0)

print(my_tuple_of_tuples.index(3, 8))