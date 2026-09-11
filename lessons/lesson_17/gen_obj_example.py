import time
import random
from faker import Faker

faker_inst = Faker()

def get_user_info(user_id: int):
    time_of_execution = random.choice(range(100, 300))/100  # wait for 1-3 sec
    print(f'Sending request for getting info about {user_id}')
    time.sleep(time_of_execution)

    # поверну словник інформації про юзера
    return {'id': user_id, 'name': faker_inst.name(), 'age': random.choice(range(18, 100))}

users = (get_user_info(user_id) for user_id in range(55,59))  # (k for k in ....)  - генераторний вираз


print(users)

for user in users:
    print(user)