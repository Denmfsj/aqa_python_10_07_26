

class Nissan:


    def __init__(self, model, color, tank: int=50):  # magic function, constructor
        self.model = model
        self.color = color
        self.tank = tank
        self.l_per_km = 0.1  #


    def traveling(self, city: str, distance: int):  # method, метод ... функція(не вірно семантично)

        need_fuel = distance * self.l_per_km  # с кільки палива потрібно

        print(f'For traveling we need distance * self.l_per_km => {need_fuel}')
        print(f'Tank has {self.tank}')

        if need_fuel <= self.tank:
            print('I am traveling to ' + city)

            self.tank -= need_fuel  # self.tank = self.tank - need_fuel
            print(f'We have left {self.tank} fuel')
        else:
            print('You have not enough fuel to travel to ' + city)


my_car = Nissan(model='Juke', color='Black', tank=40)

my_car.l_per_km = 0.05  #

my_car.traveling(city='Kharkiv', distance=300)
my_car.traveling(city='Kharkiv', distance=300)
#Nissan.traveling(self=my_car, city='Kharkiv', distance=300)

print('-'*80)



