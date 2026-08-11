


class Tesla:

    brand = 'Tesla'  # class attribute

    def __init__(self, model):
        self.model = model  # instance attribute

    def drive(self, destination):  # instance method
        print(f'{self.model} is driving to {destination}')


    @classmethod
    def get_brand(cls):  # class method
        random_number = cls.get_max_battery_size(3)
        return f'Attribute of class is {cls.brand}, {random_number}'

    @staticmethod
    def get_max_battery_size(multiplier):  # static method
        return 1000 * multiplier


model_y = Tesla('modelY')
model_x = Tesla('modelX')
model_y.drive('NY')
model_x.drive('NY')

Tesla.brand = 'Modern Tesla'

print('model_y:brand --> ', model_y.brand, '--->', id(model_y.brand))
print('model_x:brand --> ', model_x.brand, '--->', id(model_x.brand))
print('Tesla:brand --> ', Tesla.brand, '--->', id(Tesla.brand))

print('-'*80)
print('model_x:get_brand --> ', model_x.get_brand(), '--->', id(model_x.get_brand()))
print('Tesla:get_brand --> ', Tesla.get_brand(), '--->', id(Tesla.get_brand()))

print('-'*80)
print('model_x:get_max_battery_size --> ', model_x.get_max_battery_size(2))
print('Tesla:get_max_battery_size --> ', Tesla.get_max_battery_size(4))




