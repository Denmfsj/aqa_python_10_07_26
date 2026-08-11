
date_1 = '2025-10-10'
date_2 = '10-10-2025'

class DateTimeUtils:

    _JAPAN_DATA_FORMAT = "YYYY-mm-dd"
    _CLINET_X_DATE_FORMAT = "YYYY-mm-ddYHH:mm"



class Car:

    def __init__(self, make, model):

        self.make = make          # Public attribute

        self._model = model        # Protected attribute

        self.__year = 2022         # Private attribute

    def display_model(self):   # Public  method
        print(f"Model: {self._model}")

    def update_year(self, new_year):
        self.__year = new_year

    def get_year(self):
        return self.__year

# Створення об'єкта та використання атрибутів та методів
my_car = Car("Toyota", "Camry")

my_car._Car__year = 10
print(my_car.get_year())

# print(my_car.make)              # Public attribute, виведе: Toyota
# my_car.display_model()          # Protected method, виведе: Model: Camry
# print('_model', my_car._model)  # Protected method, виведе: Model: Camry
# # print('__year', my_car.__year)  # Private attribute, буде помилка
# print(my_car.get_year())        # Private attribute update
# my_car.update_year(2023)        # Private attribute update
# print(my_car.get_year())         # Private attribute update

