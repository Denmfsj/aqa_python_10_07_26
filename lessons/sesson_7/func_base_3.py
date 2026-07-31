


def print_user_info(user_name,
                    user_last_name=None, user_age=None, user_city=None):

    base_row = f'Hello this is infor about user\nName is {user_name}'

    if user_last_name:
        base_row = f'{base_row}({user_last_name})'
    if user_age:
        base_row = f'{base_row}\nAge is {user_age}'
    if user_city:
        base_row = f'{base_row}\nCity is {user_city}'

    print(base_row)


print_user_info(user_name='Den', user_age=33)
print_user_info(user_name='Yur', user_last_name='Pr')
print_user_info(user_name='Yur', user_last_name='Pr', user_age=55)





