my_friends_list = ['John', 'Alex', 'John', 'Alex', 'Michael']

search_user_name = 'John'

# [що_я_буду_додавати_в_новий_список for елемент_списка in список if умова]
alex_user_comr = [user for user in my_friends_list if user == search_user_name]
print(alex_user_comr)


# range() - генератор(генерує числа)

# my_list_of_number = list(range(0, 40, 3))  # [0,3,6,....,39]
# my_list_of_negative_number = range(-100, 40, 3)  # [-100, -97,...,5,....,38]
# print(my_list_of_negative_number, type(my_list_of_negative_number))
# print(my_list_of_number)

my_list_of_number = list(range(0, 40, 2))

# фільтрація, ми ВІДфільтрували всі числа які зінчуться на 10
my_updated_list_of_numbers = [n for n in my_list_of_number if n%10 != 0]
print(my_updated_list_of_numbers)

my_updated_list_of_numbers = [n**2 for n in my_updated_list_of_numbers]  # піднесення в квадрат
print(my_updated_list_of_numbers)


# [(id, name), (...), ...]
api_response = [(1, 'A'), (2, 'Alex'), (3 ,''), (4, 'Yr')]

valid_users = ([user for user in api_response
                if (user[1] != '') and (user[1] is not None) 
                ])

print(valid_users)