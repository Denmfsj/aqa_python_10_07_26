my_friends_list = ['John', 'Alex', 'John', 'Alex', 'Michael']


# Знайти і використати юзера з іменем = Alex
search_user_name = 'Alex'

# Знайти чи є юзер з іменем = Alex
print(f'we are working with user {search_user_name}')

is_user_exist_in_the_list = search_user_name in my_friends_list
print(f'Is user exist:  {is_user_exist_in_the_list}')

# знайти індекс юзера з name = 'Alex'
index_of_alex = None
if is_user_exist_in_the_list:
    index_of_alex = my_friends_list.index(search_user_name)

print(f'index of user is {index_of_alex}')


# Знайти і використати юзера з іменем = Alex

# [що_я_буду_додавати_в_новий_список for елемент_списка in список if умова]
alex_user_comr = [user for user in my_friends_list if user == search_user_name]
print(alex_user_comr)


alex_user = []
for user in my_friends_list:  #  ['John', 'Alex', 'John', 'Michael']
    if user == search_user_name:
        alex_user.append(search_user_name)  # ['Alex']

 # alex_user = ['Alex', 'Alex']

alex_user = alex_user[0]  # 'Alex'
print(f'we\'ve found user {alex_user.upper()}')  # 'Alex'.upper()

# перевірка чи відсортовані значення
api_response_of_ides = [1,2,5,6,3,4,99,8,6,7]

sorted_value = sorted(api_response_of_ides)
is_sorted = api_response_of_ides == sorted_value

print(f'Data is sorted: {is_sorted}')


