
def get_user_info(user_name, user_address):

    return f'User name is {user_name}. He-She lives at {user_address}'

def print_user_info(user_name, user_last_name, user_age):
    res = f'This is {user_name}({user_last_name}). He is {user_age} years old'
    print(res)  # no return ==> return None


user_add = get_user_info('Den', 'Kharkiv')

user_2_info = print_user_info('Yur', 'Kr', 88)

print(user_add)
print(user_2_info)  # print(None)

