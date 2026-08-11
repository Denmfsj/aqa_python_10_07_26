

class Engine:
    def __init__(self, number, volume, fuel_type):
        self.number = number
        self.volume = volume
        self.fuel_type = fuel_type


class ClassCar:
    def __init__(self, name, number_of_dynamic):
        self.name = name
        self.number_of_dynamic = number_of_dynamic



class Car:

    def __init__(self, model, year, engine: Engine, class_type: ClassCar):
        self.model = model
        self.year = year
        self.engine = engine
        self.class_type = class_type


td42 = Engine(number='td42', volume=4199, fuel_type='d')
clas_car = ClassCar(name='default', number_of_dynamic=2)

patrol_y60 = Car(model='Patrol', year=2020, engine=td42, class_type=clas_car)

print(patrol_y60.model)
print(patrol_y60.engine.number)
print(patrol_y60.class_type.name)