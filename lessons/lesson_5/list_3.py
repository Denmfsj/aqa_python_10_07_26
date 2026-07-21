my_friends_list = ['Alex', 'John', 'Michael']

# my_friends_list.insert(-555, 'lolo')  # --> insert в самий початок
# my_friends_list.insert(-1, 'lolo')  # --> insert(2, 'lolo')
# print(my_friends_list)  # ['Alex', 'John', 'lolo', 'Michael']

# insert, remove, pop

my_friends_list.insert(0, 'Yur')  # спочатку індекс, потім значення
# print(my_friends_list)  # ['Yur', 'Alex', 'John', 'Michael']

my_friends_list.insert(2, 'Lesia')  # спочатку індекс, потім значення
# print(my_friends_list)  # ['Yur', 'Alex', 'Lesia', 'John', 'Michael']

my_friends_list.insert(444, 'Viktoria')  # спочатку індекс, потім значення
print(my_friends_list)  # ['Yur', 'Alex', 'Lesia', 'John', 'Michael', 'Viktoria']
# print(my_friends_list[5])

# -------------------------

my_friends_list.insert(555, 'Lesia')  # спочатку індекс, потім значення
my_friends_list.remove('Lesia')
print(my_friends_list)  # ['Yur', 'Alex', 'John', 'Michael', 'Viktoria']
# print(my_friends_list[4])

# -------------------
last_element = my_friends_list.pop()  # видаляє і повертає останній елемент
#print('last_element', last_element)
#print(my_friends_list)

second_element = my_friends_list.pop(1)  # index 1 = element 2
print('second_element', second_element)  # Alex
#print(my_friends_list)  # ['Yur', 'John', 'Michael', 'Viktoria']

index_second_el = my_friends_list.index('John')
print(index_second_el)

# my_friends_list.insert(555, 'Alex')
# print(my_friends_list)
#
# for index in range(0,len(my_friends_list)):  # від 0 до довжини списка -1б від 0 до 4х включно
#     name = my_friends_list.pop()
#     if name == 'Alex':
#         print('first Alex was found')
#         break
#
# print(my_friends_list)