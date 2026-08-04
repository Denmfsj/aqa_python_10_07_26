

class Nissan:

    model = 'Juke'  #  атрибут

    @staticmethod
    def traveling(city: str):  # method, метод ... функція(не вірно семантично)
        print('I am traveling to ' + city)


my_car = Nissan()   # instance, екземпляр, об'єкт
my_friend_car = Nissan()

print(my_car.model)
print(my_friend_car.model)

Nissan.traveling('NY')

my_car.traveling('Kyiv')
my_friend_car.traveling('Kharkiv')
