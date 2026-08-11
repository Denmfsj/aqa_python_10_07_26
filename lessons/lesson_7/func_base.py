

def greetings(name):
    print(f'Hello {name}')


# name = 'Oleh'
# my_friend_name = 'Olha'
#
# print('First row')
# greetings(my_friend_name)
# print('-'*79)
# greetings('Ihor')
# print(f'name from base level is {name}')

# -----------------------------

def print_user_info(user_name, user_last_name, user_age):
    print(f'This is {user_name}({user_last_name}). He is {user_age} years old')

fr_name = 'Ihor'
fr_second_name = 'Iv'
fr_age = 30

print_user_info(user_age=fr_age, user_name=fr_name, user_last_name=fr_second_name)

print_user_info('Alex', user_age=35, user_last_name='Pr')


my_name = 'Denys'
my_second_name = 'Mer'
my_age = 33

print_user_info(my_name, my_second_name, my_age)
