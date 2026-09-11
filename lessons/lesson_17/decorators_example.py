import random
import time
import logging

# 19:44:06 [    INFO] send request to  /users
# 19:44:07 [    INFO] getting answer


def logging_time(fn):  # fn - стандартна нахва змінної, можде бути будь яка

    def wrapper(*args, **kwargs):  # wrapper - станзартне ім'я, *args, **kwargs - дуь яка кількість аргументів
        print(f'start execution wrapper before {fn.__name__}')
        start_time = time.time()

        data = fn(*args, **kwargs)

        time_of_execution = time.time() - start_time
        print(f'time of executions of {fn.__name__} is {time_of_execution}')
        return data

    return wrapper


def log_res_of_fn(fn):

    def wrapper(*args, **kwargs):

        print(f'{fn.__name__} start logging')
        print(f'{fn.__name__} has args: {args}')
        print(f'{fn.__name__} has kwargs: {kwargs}')
        return fn(*args, **kwargs)

    return wrapper


@logging_time
def send_request_to_users():
    time.sleep(random.choice(range(100))/100)

@log_res_of_fn
@logging_time
def send_request_to_wallets():
    time.sleep(random.choice(range(50))/100)

@log_res_of_fn
@logging_time
def send_request_to_user_details(user_id):
    time.sleep(random.choice(range(100, 150))/100)
    return {'id': user_id}

send_request_to_wallets()
send_request_to_user_details(user_id=24)
user_id_data = send_request_to_user_details(12)
print(user_id_data)

def calculation_of_smth():
    time.sleep(random.choice(range(100, 200))/100)


