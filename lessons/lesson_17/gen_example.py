import time
import random
from faker import Faker

faker_inst = Faker()

def get_user_info(number_of_user: int):

    for _ in range(number_of_user):

        user_id = random.randint(1, 100500)
        time_of_execution = random.choice(range(100, 300))/100  # wait for 1-3 sec
        print(f'Sending request for getting info about {user_id}')
        time.sleep(time_of_execution)
        print(f'Information about user {user_id} returned')

        # поверну словник інформації про юзера
        yield {'id': user_id, 'name': faker_inst.name(), 'age': random.choice(range(18, 100))}



# users = get_user_info(2)
#
# print(next(users))
# print(next(users))
# print(next(users))
# print(next(users))

for user in get_user_info(3):
    print(user)

