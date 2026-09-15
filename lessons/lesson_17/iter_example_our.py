import random
from faker import Faker
import time

faker_inst = Faker()



class IteratorByAlsmostRandomValue:


    def __init__(self, number_of_random_els):
        self.__n = number_of_random_els
        self.__current_user_index = 0

    def __next__(self):

        if self.__current_user_index >= self.__n:
            raise StopIteration

        user_id = random.randint(1, 100500)  # генеруємо випадковий id

        if self.__current_user_index %2 == 0:
            user_id = 42

        self.__current_user_index += 1

        return self.__get_user_info(user_id)


    def __get_user_info(self, user_id: int):
        time_of_execution = random.choice(range(100, 300))/100  # wait for 1-3 sec
        print(f'Sending request for getting info about {user_id}')
        time.sleep(time_of_execution)

        # поверну словник інформації про юзера
        return {'id': user_id, 'name': faker_inst.name(), 'age': random.choice(range(18, 100))}


class GetUsersInfo:
    """Мoже отрирмувати інформацію про n юзерів послідовно(ітерабельнго)"""

    def __init__(self, n: int):
        """
        n param: кількість юзерів про яких можна отримати інформацію
        """

        self.__n = n


    def __iter__(self):
        return IteratorByAlsmostRandomValue(self.__n)


    def show_information_about_endpoint(self):
        return 'Some additional information'


for user in GetUsersInfo(n=2):  # GetUsersInfo(n=2) --> GetUsersInfo(n=2).__iter__()
    print(user)
    print('\n')

show_user_info = GetUsersInfo(n=5)
print(show_user_info.show_information_about_endpoint())