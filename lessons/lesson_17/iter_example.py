name = 'den'
list_numbers = [1,2,3,4,5]
cities = {'Kharkiv', 'Kyiv', 'Lviv'}


print('-------')
for el in name:
    print(el)

print('-------')
iter_onj_of_str = iter(name)  # функція iter поверне ітерабельний об'єкт  name.__iter__()

print(next(iter_onj_of_str))  # d   iter_onj_of_str.__next__()
print(next(iter_onj_of_str))  # e
print(next(iter_onj_of_str))  # n


print('-------')
iter_onj_of_str_for_while = iter(name)  # name.__iter__()
while True:
    try:
        print(next(iter_onj_of_str_for_while))  # iter_onj_of_str_for_while.__next__()
    except StopIteration:
        break

list_numbers = [1,2,3,4,5]

iter_1 = iter(list_numbers)
iter_2 = iter(list_numbers)

print(next(iter_1))  # 1
print(next(iter_2))  # 1
print(next(iter_1))  # 2
print(next(iter_1))  # 3