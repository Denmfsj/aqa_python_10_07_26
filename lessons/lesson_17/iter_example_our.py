import random
from faker import Faker
import time

faker_inst = Faker()


class GetUsersInfo:
    """Мoже отрирмувати інформацію про n юзерів послідовно(ітерабельнго)"""

    def __init__(self, n: int):
        """
        n param: кількість юзерів про яких можна отримати інформацію
        """

        self.__n = n
        self.__current_user_index = 0



    def __iter__(self):
        return self

    def __next__(self):

        if self.__current_user_index >= self.__n:
            raise StopIteration

        user_id = random.randint(1, 100500)  # генеруємо випадковий id

        self.__current_user_index += 1

        return self.__get_user_info(user_id)


    def __get_user_info(self, user_id: int):
        time_of_execution = random.choice(range(100, 300))/100  # wait for 1-3 sec
        print(f'Sending request for getting info about {user_id}')
        time.sleep(time_of_execution)

        # поверну словник інформації про юзера
        return {'id': user_id, 'name': faker_inst.name(), 'age': random.choice(range(18, 100))}



for user in GetUsersInfo(n=3):
    print(user)
    print('\n')
