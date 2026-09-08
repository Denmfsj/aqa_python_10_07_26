

def greetings(name):
    print(f'Hello {name}')


def print_user_info(user_name, user_last_name, user_age):
    print(f'This is {user_name}({user_last_name}). He is {user_age} years old')




if __name__ == '__main__':

    fr_name = 'Ihor'
    fr_second_name = 'Iv'
    fr_age = 30

    print_user_info(user_age=fr_age, user_name=fr_name, user_last_name=fr_second_name)
    print_user_info('Alex', user_age=35, user_last_name='Pr')


    my_name = 'Denys'
    my_second_name = 'Mer'
    my_age = 33

    print_user_info(my_name, my_second_name, my_age)