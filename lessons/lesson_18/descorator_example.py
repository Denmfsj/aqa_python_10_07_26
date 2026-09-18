import random
import time


def print_timing_of_execution(fn):

    def wrapper(*args, **kwargs):
        start_time = time.time()  # float - sec,  from 1-1-1970
        res = fn(*args, **kwargs)
        execution_time = time.time() - start_time  # float - sec
        print(f'Execution time is {execution_time}')
        return res

    return wrapper

@print_timing_of_execution
def send_request_to_users():
    time_of_ex = random.choice(range(100, 120*100))/100  # від 1 до 120 секунд
    time.sleep(time_of_ex)
    return 'Done'

@print_timing_of_execution
def send_request_to_wallets():
    time.sleep(random.choice(range(50))/100)

@print_timing_of_execution
def send_request_to_user_details(user_id):
    time.sleep(random.choice(range(100, 150))/100)
    return {'id': user_id}

# send_request_to_wallets()
# send_request_to_user_details(user_id=24)
# user_id_data = send_request_to_user_details(12)

print('run send_request_to_users')
# print_timing_of_execution(send_request_to_users)
print(send_request_to_users())

print('run send_request_to_wallets')
send_request_to_wallets()
print('run send_request_to_user_details')
send_request_to_user_details(user_id=24)



